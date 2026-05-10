"""The 40's Cookbook — Agent Hub backend"""

import os, re, json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic

app = FastAPI(title="40's Cookbook — Agent Hub")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

AGENTS_DIR = Path(__file__).parent.parent / ".claude" / "agents"
DASHBOARD_DIR = Path(__file__).parent

# ── Agent display config ───────────────────────────────────────────────────────
AGENT_DISPLAY = {
    "business-analyst": {
        "display_name": "Business Analyst",
        "icon": "📊",
        "color": "#E67E22",
        "tagline": "Audits your business honestly. Finds the gaps, risks, and real opportunities.",
        "short_role": "Business audit & risk mapping",
        "starter_prompts": [
            "Give me an honest audit of our current business position and biggest risks before launch",
            "Analyze our unit economics — are the margins viable at ₹60–₹75 per 100g?",
            "What are the 3 biggest things that could kill this launch?",
        ],
    },
    "market-analyst": {
        "display_name": "Market Analyst",
        "icon": "🔍",
        "color": "#2980B9",
        "tagline": "Maps the exact white space competitors haven't claimed in the premium segment.",
        "short_role": "Competitive intelligence & white space",
        "starter_prompts": [
            "Define the exact white space we're entering and why no one owns it yet",
            "Who are our 3 most dangerous competitors and what can we learn from each?",
            "What does the data say about premium pickle demand on Blinkit and Zepto?",
        ],
    },
    "brand-strategist": {
        "display_name": "Brand Strategist",
        "icon": "🎯",
        "color": "#C0392B",
        "tagline": "Builds positioning, values, tone of voice, brand archetype, and manifesto.",
        "short_role": "Positioning & verbal identity",
        "starter_prompts": [
            "Define our brand archetype and what it means for how we communicate",
            "Write a brand manifesto — what The 40's Cookbook truly stands for",
            "Build our complete messaging framework: hero message, proof points, what we never say",
        ],
    },
    "creative-director": {
        "display_name": "Creative Director",
        "icon": "🎨",
        "color": "#8E44AD",
        "tagline": "Creates 3 distinct visual concepts with ready-to-use GPT Image 2, Higgsfield & Seedance prompts.",
        "short_role": "Visual identity & AI generation briefs",
        "starter_prompts": [
            "Create 3 distinct visual direction concepts for the brand — each with AI generation prompts",
            "Write detailed GPT Image 2 prompts for our hero product photography",
            "Design the visual brief for our Instagram grid aesthetic",
        ],
    },
    "content-strategist": {
        "display_name": "Content Strategist",
        "icon": "📅",
        "color": "#27AE60",
        "tagline": "Plans your content pillars, platform strategy, and a 30-day calendar with specific topics.",
        "short_role": "Content planning & platform strategy",
        "starter_prompts": [
            "Build our complete 30-day pre-launch content calendar with specific post topics",
            "Define our content pillars and what each one stands for strategically",
            "Create our platform strategy — what do we post on Instagram vs LinkedIn vs WhatsApp?",
        ],
    },
    "content-writer": {
        "display_name": "Content Writer",
        "icon": "✍️",
        "color": "#16A085",
        "tagline": "Writes all copy in the brand's authentic voice — social, web, email, and blog.",
        "short_role": "Copy & creative writing",
        "starter_prompts": [
            "Write 5 Instagram captions for our mango pickle launch — different tonal angles",
            "Write the homepage hero headline + subhead variants for our website",
            "Create a 3-email launch sequence: pre-launch tease, launch day, post-purchase",
        ],
    },
    "brand-manager": {
        "display_name": "Brand Manager",
        "icon": "👑",
        "color": "#F39C12",
        "tagline": "Coordinates the team, tracks progress, and delivers weekly reports and full exports.",
        "short_role": "Coordination & progress tracking",
        "starter_prompts": [
            "Give me a weekly brand report — what's done, what's pending, what's at risk",
            "What's the critical path to launch and what's blocking us right now?",
            "Prioritize the next 5 tasks across all departments in order of urgency",
        ],
    },
}

AGENT_ORDER = [
    "business-analyst",
    "market-analyst",
    "brand-strategist",
    "creative-director",
    "content-strategist",
    "content-writer",
    "brand-manager",
]


def get_client() -> anthropic.Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise HTTPException(400, "ANTHROPIC_API_KEY environment variable is not set. Run: export ANTHROPIC_API_KEY=your-key")
    return anthropic.Anthropic(api_key=api_key)


def load_system_prompt(agent_id: str) -> str:
    path = AGENTS_DIR / f"{agent_id}.md"
    if not path.exists():
        raise HTTPException(404, f"Agent file not found: {agent_id}.md")
    content = path.read_text()
    match = re.match(r"^---\n.*?\n---\n(.*)", content, re.DOTALL)
    return match.group(1).strip() if match else content.strip()


# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/agents")
def list_agents():
    result = []
    for agent_id in AGENT_ORDER:
        path = AGENTS_DIR / f"{agent_id}.md"
        if path.exists() and agent_id in AGENT_DISPLAY:
            info = {"id": agent_id, **AGENT_DISPLAY[agent_id]}
            result.append(info)
    return result


@app.get("/health")
def health():
    has_key = bool(os.getenv("ANTHROPIC_API_KEY"))
    return {"status": "ok", "api_key_set": has_key}


class TaskRequest(BaseModel):
    agent: str
    message: str
    history: list = []


@app.post("/task")
async def run_task(req: TaskRequest):
    client = get_client()

    if req.agent not in AGENT_DISPLAY:
        raise HTTPException(400, f"Unknown agent: {req.agent}")

    system = load_system_prompt(req.agent)
    messages = req.history + [{"role": "user", "content": req.message}]

    def generate():
        try:
            with client.messages.stream(
                model="claude-sonnet-4-6",
                max_tokens=4096,
                system=system,
                messages=messages,
            ) as stream:
                for text in stream.text_stream:
                    yield f"data: {json.dumps({'text': text})}\n\n"
            yield "data: [DONE]\n\n"
        except anthropic.APIStatusError as e:
            yield f"data: {json.dumps({'error': f'API error: {e.status_code} — {e.message}'})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"X-Accel-Buffering": "no", "Cache-Control": "no-cache"},
    )


@app.get("/")
def serve_dashboard():
    html = (DASHBOARD_DIR / "index.html").read_text()
    return HTMLResponse(html)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    print(f"\n  🫙  The 40's Cookbook — Agent Hub")
    print(f"  Open: http://localhost:{port}\n")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
