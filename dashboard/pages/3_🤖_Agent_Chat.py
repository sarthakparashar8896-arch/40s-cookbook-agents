"""Agent Chat — The 40's Cookbook"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from pathlib import Path
import anthropic
import styles, db

st.set_page_config(page_title="Agent Chat — 40's Cookbook", layout="wide", page_icon="🤖")
styles.inject()

# ── Agent definitions ──────────────────────────────────────────────────────────
ALL_AGENTS = {
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
        info = ALL_AGENTS.get(agent_id, {})
        return (f"You are the {info.get('display_name', agent_id)} for The 40's Cookbook, "
                f"a premium Indian pickle brand with a 100-year-old Banaras family recipe. "
                f"Help with: {info.get('tagline', '')}.")
    content = path.read_text()
    match = re.match(r"^---\n.*?\n---\n(.*)", content, re.DOTALL)
    return match.group(1).strip() if match else content.strip()


def get_anthropic_client():
    try:
        secrets_key = st.secrets.get("ANTHROPIC_API_KEY", "")
    except Exception:
        secrets_key = ""
    api_key = os.getenv("ANTHROPIC_API_KEY", "") or secrets_key or st.session_state.get("api_key", "")
    if not api_key:
        st.warning("Enter your Anthropic API key in the sidebar to start chatting.")
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


# ── Session state defaults ─────────────────────────────────────────────────────
if "active_agent"   not in st.session_state: st.session_state.active_agent   = "brand-strategist"
if "active_session" not in st.session_state: st.session_state.active_session = None
if "messages"       not in st.session_state: st.session_state.messages       = []
if "history_agent"  not in st.session_state: st.session_state.history_agent  = "All"


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    styles.sidebar_brand("Agent Chat")

    # API key (if not in env)
    if not os.getenv("ANTHROPIC_API_KEY"):
        api_key_val = st.text_input(
            "Anthropic API key",
            type="password",
            placeholder="sk-ant-…",
            value=st.session_state.get("api_key", ""),
        )
        st.session_state["api_key"] = api_key_val

    author = styles.author_input()
    st.divider()

    # ── New chat button ────────────────────────────────────────────────────────
    if st.button("＋ New chat", use_container_width=True, type="primary"):
        st.session_state.active_session = None
        st.session_state.messages       = []
        st.rerun()

    st.markdown("### Agents")
    for aid, info in ALL_AGENTS.items():
        is_active = st.session_state.active_agent == aid
        label = f"{info['icon']} {info['display_name']}"
        if st.button(label, key=f"pick_{aid}", use_container_width=True,
                     help=info["tagline"]):
            if st.session_state.active_agent != aid:
                st.session_state.active_agent   = aid
                st.session_state.active_session = None
                st.session_state.messages       = []
            st.rerun()

    st.divider()

    # ── Saved conversations panel ──────────────────────────────────────────────
    st.markdown("### Saved Chats")

    history_filter = st.selectbox(
        "Show", ["All agents"] + [f"{v['icon']} {v['display_name']}" for v in ALL_AGENTS.values()],
        label_visibility="collapsed",
    )
    filter_aid = None
    if history_filter != "All agents":
        for aid, info in ALL_AGENTS.items():
            if f"{info['icon']} {info['display_name']}" == history_filter:
                filter_aid = aid
                break

    sessions = db.get_chat_sessions(agent_id=filter_aid)

    if not sessions:
        st.caption("No saved chats yet.")
    else:
        for s in sessions:
            info      = ALL_AGENTS.get(s["agent_id"], {})
            icon      = info.get("icon", "🤖")
            color     = info.get("color", "#888")
            ts        = s["updated_at"][:10]
            n_msgs    = s.get("message_count", 0)
            is_cur    = st.session_state.active_session == s["id"]
            border    = f"border-left:3px solid {color}" if is_cur else "border-left:3px solid transparent"

            col_a, col_b = st.columns([5, 1])
            with col_a:
                st.markdown(
                    f'<div style="padding:6px 8px;border-radius:6px;{border};'
                    f'background:{"#1e1e1e" if is_cur else "transparent"};'
                    f'cursor:pointer;margin-bottom:2px">'
                    f'<div style="font-size:0.78rem;font-weight:600;color:#eee;'
                    f'white-space:nowrap;overflow:hidden;text-overflow:ellipsis">'
                    f'{icon} {s["title"]}</div>'
                    f'<div style="font-size:0.67rem;color:#888">'
                    f'{ts} · {s.get("author","?")} · {n_msgs} msgs</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                if st.button("Load", key=f"load_{s['id']}", use_container_width=True):
                    msgs = db.get_chat_messages(s["id"])
                    st.session_state.active_session = s["id"]
                    st.session_state.active_agent   = s["agent_id"]
                    st.session_state.messages       = [
                        {"role": m["role"], "content": m["content"]} for m in msgs
                    ]
                    st.rerun()
            with col_b:
                if st.button("🗑", key=f"del_{s['id']}",
                             help="Delete this conversation"):
                    db.delete_chat_session(s["id"])
                    if st.session_state.active_session == s["id"]:
                        st.session_state.active_session = None
                        st.session_state.messages       = []
                    st.rerun()


# ── Main area ──────────────────────────────────────────────────────────────────
agent_id   = st.session_state.active_agent
agent_info = ALL_AGENTS[agent_id]

# Header
h1, h2 = st.columns([1, 6])
with h1:
    st.markdown(
        f'<div style="font-size:2.8rem;text-align:center;padding-top:10px">'
        f'{agent_info["icon"]}</div>',
        unsafe_allow_html=True,
    )
with h2:
    st.markdown(
        f'<div class="page-title" style="color:{agent_info["color"]}">'
        f'{agent_info["display_name"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="page-subtitle">{agent_info["tagline"]}</div>',
        unsafe_allow_html=True,
    )

# Rename current session inline
if st.session_state.active_session:
    sessions_all = db.get_chat_sessions()
    cur = next((s for s in sessions_all if s["id"] == st.session_state.active_session), None)
    if cur:
        rc1, rc2 = st.columns([5, 1])
        with rc1:
            new_title = st.text_input(
                "Conversation title", value=cur["title"],
                label_visibility="collapsed",
                placeholder="Name this conversation…",
                key="session_title",
            )
        with rc2:
            if st.button("Rename", use_container_width=True):
                db.rename_chat_session(st.session_state.active_session, new_title)
                st.rerun()

# Starter prompts shown only when chat is empty
if not st.session_state.messages:
    st.markdown("**Try asking:**")
    for prompt in agent_info["starter_prompts"]:
        if st.button(prompt, key=f"sp_{prompt[:30]}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.rerun()
    st.divider()

# Render message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input(f"Ask {agent_info['display_name']}…")

if user_input:
    # Create a new DB session on the first message
    if st.session_state.active_session is None:
        sid = db.create_chat_session(
            agent_id=agent_id,
            author=author or "Unknown",
            title=user_input[:60],
        )
        st.session_state.active_session = sid
    else:
        sid = st.session_state.active_session

    # Save + display user message
    db.append_chat_message(sid, "user", user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream + save assistant response
    api_messages = [{"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages]
    with st.chat_message("assistant"):
        response = st.write_stream(stream_response(agent_id, api_messages))

    db.append_chat_message(sid, "assistant", response)
    st.session_state.messages.append({"role": "assistant", "content": response})
