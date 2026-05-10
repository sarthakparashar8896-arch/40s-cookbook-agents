"""Agent Chat — The 40's Cookbook"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from pathlib import Path
import anthropic
import styles

st.set_page_config(page_title="Agent Chat — 40's Cookbook", layout="wide", page_icon="🤖")
styles.inject()

# ── Agent definitions ──────────────────────────────────────────────────────────
ALL_AGENTS = {
    "business-analyst": {
        "display_name": "Business Analyst",
        "icon": "📊",
        "color": "#E67E22",
        "tagline": "Honest business audits — gaps, risks, unit economics, launch readiness.",
        "starter_prompts": [
            "Give me an honest audit of our current business position and biggest risks",
            "Analyze our unit economics at ₹60–₹75 per 100g — are the margins viable?",
            "What are the 3 biggest things that could kill this launch?",
        ],
    },
    "market-researcher": {
        "display_name": "Market Researcher",
        "icon": "🔎",
        "color": "#2980B9",
        "tagline": "Competitor pricing, category research, channel margin benchmarks.",
        "starter_prompts": [
            "Research premium Indian pickle brands on Blinkit and Zepto — who's winning?",
            "What are typical channel margins for pickle brands on quick commerce?",
            "Give me the current price landscape for mango pickle across online platforms",
        ],
    },
    "supplier-scout": {
        "display_name": "Supplier Scout",
        "icon": "🏭",
        "color": "#27AE60",
        "tagline": "Find vendors, evaluate suppliers, draft outreach emails.",
        "starter_prompts": [
            "Find contract manufacturers for pickle production near Delhi NCR",
            "Draft a first outreach email to a glass jar supplier — professional tone",
            "What should I look for when evaluating a pickle co-manufacturer?",
        ],
    },
    "brand-strategist": {
        "display_name": "Brand Strategist",
        "icon": "🎯",
        "color": "#C0392B",
        "tagline": "Brand positioning, values, tone of voice, messaging framework.",
        "starter_prompts": [
            "Define our brand archetype and what it means for how we communicate",
            "Write a brand manifesto for The 40's Cookbook",
            "Build our messaging framework: hero message, proof points, what we never say",
        ],
    },
    "market-analyst": {
        "display_name": "Market Analyst",
        "icon": "🔍",
        "color": "#1A5276",
        "tagline": "White space mapping, competitive positioning, consumer trends.",
        "starter_prompts": [
            "Define the exact white space we're entering and why no brand owns it yet",
            "Who are our 3 most dangerous competitors and what can we learn from each?",
            "Map the premium pickle segment — who's winning, who's failing, and why",
        ],
    },
    "gtm-strategist": {
        "display_name": "GTM Strategist",
        "icon": "🗺️",
        "color": "#16A085",
        "tagline": "Go-to-market planning, channel strategy, launch sequencing.",
        "starter_prompts": [
            "Build our go-to-market launch sequence for the first 90 days",
            "Should we launch on Blinkit or Amazon first — what's the right call?",
            "Map our restaurant partnership strategy for brand proof points",
        ],
    },
    "creative-director": {
        "display_name": "Creative Director",
        "icon": "🎨",
        "color": "#8E44AD",
        "tagline": "Visual direction, packaging aesthetics, AI image generation prompts.",
        "starter_prompts": [
            "Create 3 distinct visual concepts for the brand with AI generation prompts",
            "Write GPT Image 2 prompts for our hero product photography",
            "Brief a packaging designer — what does the bottle need to communicate?",
        ],
    },
    "content-strategist": {
        "display_name": "Content Strategist",
        "icon": "📅",
        "color": "#27AE60",
        "tagline": "Content pillars, platform strategy, 30-day content calendars.",
        "starter_prompts": [
            "Build our 30-day pre-launch content calendar with specific post topics",
            "Define our content pillars — what does each one stand for?",
            "Platform strategy: what do we post on Instagram vs LinkedIn vs WhatsApp?",
        ],
    },
    "content-writer": {
        "display_name": "Content Writer",
        "icon": "✍️",
        "color": "#16A085",
        "tagline": "Social copy, website copy, email sequences — all in the brand voice.",
        "starter_prompts": [
            "Write 5 Instagram captions for our mango pickle launch — different angles",
            "Write homepage hero copy + subhead variants for our website",
            "Create a 3-email launch sequence: tease → launch day → post-purchase",
        ],
    },
    "brand-manager": {
        "display_name": "Brand Manager",
        "icon": "👑",
        "color": "#F39C12",
        "tagline": "Team coordination, weekly progress reports, priority tracking.",
        "starter_prompts": [
            "Give me a weekly brand report — what's done, pending, at risk",
            "What's the critical path to launch and what's blocking us?",
            "Prioritize the next 5 tasks across all departments",
        ],
    },
}

AGENTS_DIR = Path(__file__).parent.parent.parent / ".claude" / "agents"


def load_system_prompt(agent_id: str) -> str:
    path = AGENTS_DIR / f"{agent_id}.md"
    if not path.exists():
        return f"You are the {ALL_AGENTS[agent_id]['display_name']} for The 40's Cookbook, a premium Indian pickle brand founded by Madhu with a 100-year-old family recipe. Help with {ALL_AGENTS[agent_id]['tagline'].lower()}"
    content = path.read_text()
    match = re.match(r"^---\n.*?\n---\n(.*)", content, re.DOTALL)
    return match.group(1).strip() if match else content.strip()


def get_anthropic_client():
    api_key = st.secrets.get("ANTHROPIC_API_KEY", "") or os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.error(
            "**ANTHROPIC_API_KEY not set.** "
            "Add it to `.streamlit/secrets.toml` or set the environment variable."
        )
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def stream_response(agent_id: str, messages: list):
    client = get_anthropic_client()
    system = load_system_prompt(agent_id)
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=system,
        messages=messages,
    ) as stream:
        for text in stream.text_stream:
            yield text


# ── Sidebar — agent picker ─────────────────────────────────────────────────────
with st.sidebar:
    styles.sidebar_brand("Agent Chat")
    st.markdown("### Select Agent")

    if "active_agent" not in st.session_state:
        st.session_state.active_agent = "brand-strategist"

    for agent_id, info in ALL_AGENTS.items():
        is_active = st.session_state.active_agent == agent_id
        border = f"3px solid {info['color']}" if is_active else "1px solid #333"
        bg     = f"{info['color']}22" if is_active else "transparent"
        if st.button(
            f"{info['icon']} {info['display_name']}",
            key=f"pick_{agent_id}",
            use_container_width=True,
            help=info["tagline"],
        ):
            if st.session_state.active_agent != agent_id:
                st.session_state.active_agent = agent_id
                st.session_state.messages     = []
            st.rerun()

    st.divider()
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

agent_id   = st.session_state.active_agent
agent_info = ALL_AGENTS[agent_id]

# ── Header ─────────────────────────────────────────────────────────────────────
h1, h2 = st.columns([1, 4])
with h1:
    st.markdown(f'<div style="font-size:3rem;text-align:center;padding-top:8px">{agent_info["icon"]}</div>', unsafe_allow_html=True)
with h2:
    st.markdown(f'<div class="page-title" style="color:{agent_info["color"]}">{agent_info["display_name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{agent_info["tagline"]}</div>', unsafe_allow_html=True)

# ── Starter prompts (shown when chat is empty) ─────────────────────────────────
if not st.session_state.messages:
    st.markdown("**Try asking:**")
    cols = st.columns(len(agent_info["starter_prompts"]))
    for col, prompt in zip(cols, agent_info["starter_prompts"]):
        with col:
            if st.button(prompt, use_container_width=True, key=f"sp_{prompt[:20]}"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.rerun()
    st.divider()

# ── Render chat history ────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Chat input ─────────────────────────────────────────────────────────────────
user_input = st.chat_input(f"Ask {agent_info['display_name']}…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    api_messages = [{"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages]

    with st.chat_message("assistant"):
        response = st.write_stream(stream_response(agent_id, api_messages))

    st.session_state.messages.append({"role": "assistant", "content": response})
