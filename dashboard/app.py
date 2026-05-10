"""The 40's Cookbook — Brand & Research Dashboard"""

import streamlit as st

st.set_page_config(
    page_title="The 40's Cookbook — Brand Hub",
    page_icon="🫙",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --red: #C0392B;
    --red-light: #F5CCC2;
    --cream: #FDF6F0;
    --dark: #1A1A1A;
    --mid: #555;
    --border: #E8E0D8;
}

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1A1A1A !important;
    border-right: 3px solid #C0392B;
}
section[data-testid="stSidebar"] * { color: #F5F5F5 !important; }
section[data-testid="stSidebar"] .stSelectbox label { color: #999 !important; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; }
section[data-testid="stSidebar"] .stRadio label { color: #E8E8E8 !important; font-size: 0.9rem !important; }
section[data-testid="stSidebar"] .stButton > button {
    background: #2A2A2A !important; color: #E8E8E8 !important;
    border: 1px solid #3A3A3A !important; border-radius: 8px !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: #333 !important; border-color: #C0392B !important; color: #fff !important;
}
section[data-testid="stSidebar"] hr { border-color: #333 !important; }

/* Cards */
.card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.card-red {
    background: #FDF6F0;
    border-left: 4px solid var(--red);
    border-radius: 0 12px 12px 0;
    padding: 20px 24px;
    margin-bottom: 16px;
}
.metric-card {
    background: white;
    border: 1px solid var(--border);
    border-top: 3px solid var(--red);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

/* Typography */
.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: var(--red);
    margin-bottom: 4px;
    line-height: 1.2;
}
.page-subtitle {
    font-size: 1rem;
    color: var(--mid);
    margin-bottom: 32px;
    font-weight: 300;
}
.section-label {
    font-size: 0.7rem;
    font-weight: 600;
    color: var(--red);
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 8px;
}
.tagline {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-style: italic;
    color: var(--dark);
}
.quote-block {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #333;
    border-left: 4px solid var(--red);
    padding: 16px 24px;
    background: #FDF6F0;
    border-radius: 0 8px 8px 0;
    margin: 16px 0;
    line-height: 1.8;
}
.urgency-high { color: #C0392B; font-weight: 600; font-size: 0.8rem; }
.urgency-medium { color: #D68910; font-weight: 600; font-size: 0.8rem; }
.urgency-low { color: #27AE60; font-weight: 600; font-size: 0.8rem; }

.learning-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 20px;
    border-left: 5px solid var(--red);
}
.learning-num {
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--red);
    letter-spacing: 0.15em;
    text-transform: uppercase;
}
.learning-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2rem;
    color: var(--dark);
    margin: 4px 0 12px 0;
}
.insight-label { font-weight: 600; color: var(--mid); font-size: 0.85rem; margin-bottom: 4px; }
.insight-text { font-size: 0.95rem; color: var(--dark); line-height: 1.6; }
.impl-text { font-size: 0.95rem; color: var(--dark); line-height: 1.6; font-style: italic; }

.tier-budget { background: #C6EFCE; color: #276221; padding: 3px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; }
.tier-mainstream { background: #FFEB9C; color: #7D6608; padding: 3px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; }
.tier-premium { background: #FDBF8E; color: #784212; padding: 3px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; }
.tier-gap { background: #BDD7EE; color: #154360; padding: 3px 10px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; display: inline-block; }

.gap-banner {
    background: linear-gradient(135deg, #154360 0%, #1A5276 100%);
    color: white;
    padding: 20px 28px;
    border-radius: 12px;
    margin: 24px 0;
}
.gap-banner h3 { color: #BDD7EE; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 6px; }
.gap-banner p { font-size: 1.1rem; font-weight: 500; margin: 0; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 24px 0; border-bottom: 1px solid #333; margin-bottom: 24px;">
        <div style="font-family:'Playfair Display',serif; font-size:1.3rem; color:#C0392B; font-weight:600;">
            The 40's Cookbook
        </div>
        <div style="font-size:0.75rem; color:#888; font-style:italic; margin-top:4px;">by Madhu · Brand Hub</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠  Brand Foundation", "📊  Competitor Intelligence", "💡  Key Learnings", "🗺️  Go-to-Market", "✅  Open Questions"],
        label_visibility="collapsed"
    )

    st.markdown("""
    <div style="margin-top:40px; font-size:0.72rem; color:#555; border-top:1px solid #333; padding-top:16px;">
        Research: May 2026<br>
        Version 1.0 · Confidential
    </div>
    """, unsafe_allow_html=True)

from data import (BRAND, BRAND_STORY, MISSION, VISION, PROMISE, VALUES,
                  FLAVORS, AUDIENCE, PRICE_PER_100G, PLATFORM_PRESENCE,
                  COMPETITORS, LEARNINGS, GTM_PHASES, OPEN_QUESTIONS, NEXT_STEPS)
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 · BRAND FOUNDATION
# ─────────────────────────────────────────────────────────────────────────────
if "Brand Foundation" in page:
    st.markdown('<div class="page-title">Brand Foundation</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">The 40\'s Cookbook by Madhu · Source of truth for all brand work</div>', unsafe_allow_html=True)

    # Hero bar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><div class="section-label">Tagline</div><div class="tagline">Old recipe.<br>New table.</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="section-label">Founded</div><div style="font-size:2rem;font-weight:700;color:#C0392B">100+</div><div style="color:#555;font-size:0.9rem">years of recipe heritage</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="section-label">Launch Flavors</div><div style="font-size:2rem;font-weight:700;color:#C0392B">4</div><div style="color:#555;font-size:0.9rem">named SKUs at launch</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="section-label">Target Cities</div><div style="font-size:2rem;font-weight:700;color:#C0392B">Tier 1</div><div style="color:#555;font-size:0.9rem">Delhi NCR · Mumbai · Bangalore</div></div>', unsafe_allow_html=True)

    st.divider()

    left, right = st.columns([3, 2])

    with left:
        st.markdown("#### Brand Story")
        for para in BRAND_STORY.strip().split("\n\n"):
            st.markdown(f'<div class="quote-block">{para}</div>', unsafe_allow_html=True)

    with right:
        st.markdown("#### Positioning")
        st.markdown(f'<div class="card-red"><span class="section-label">Positioning Statement</span><br><br>{BRAND["positioning"]}</div>', unsafe_allow_html=True)

        st.markdown("#### Launch Flavors")
        flavor_colors = {"Mango": "#F39C12", "Lemon": "#F4D03F", "Chili": "#E74C3C", "Mixed": "#8E44AD"}
        for f in FLAVORS:
            col = flavor_colors.get(f["flavor"], "#C0392B")
            st.markdown(f"""
            <div class="card" style="padding:16px 20px; margin-bottom:10px; border-left: 4px solid {col}">
                <span style="font-weight:700;color:{col};font-size:0.9rem">{f["flavor"]}</span>
                <span style="margin:0 8px;color:#ccc">·</span>
                <span style="font-family:'Playfair Display',serif;font-size:1.1rem;font-style:italic">{f["name"]}</span>
                <div style="font-size:0.85rem;color:#666;margin-top:6px">{f["rationale"]}</div>
            </div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("#### Mission · Vision · Brand Promise")
    mc, vc, pc = st.columns(3)
    with mc:
        st.markdown(f'<div class="card" style="border-top:3px solid #C0392B"><div class="section-label">Mission</div><p style="font-style:italic;color:#333;line-height:1.7;font-size:0.95rem">{MISSION}</p></div>', unsafe_allow_html=True)
    with vc:
        st.markdown(f'<div class="card" style="border-top:3px solid #27AE60"><div class="section-label">Vision</div><p style="font-style:italic;color:#333;line-height:1.7;font-size:0.95rem">{VISION}</p></div>', unsafe_allow_html=True)
    with pc:
        st.markdown(f'<div class="card" style="border-top:3px solid #2980B9"><div class="section-label">Brand Promise</div><p style="font-style:italic;color:#333;line-height:1.7;font-size:0.95rem">{PROMISE}</p></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("#### Core Values")
    v1, v2 = st.columns(2)
    for i, (val, desc) in enumerate(VALUES):
        col = v1 if i % 2 == 0 else v2
        with col:
            st.markdown(f'<div class="card"><div style="font-weight:700;color:#C0392B;margin-bottom:8px">{val}</div><div style="color:#444;font-size:0.9rem;line-height:1.6">{desc}</div></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("#### Target Audience")
    a1, a2 = st.columns(2)
    items = list(AUDIENCE.items())
    for i, (k, v) in enumerate(items):
        col = a1 if i % 2 == 0 else a2
        with col:
            st.markdown(f'<div style="padding:12px 0;border-bottom:1px solid #EEE"><span style="font-weight:600;color:#C0392B;font-size:0.85rem">{k}</span><br><span style="color:#333;font-size:0.9rem">{v}</span></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2 · COMPETITOR INTELLIGENCE
# ─────────────────────────────────────────────────────────────────────────────
elif "Competitor" in page:
    st.markdown('<div class="page-title">Competitor Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Pricing benchmarks across Blinkit, Zepto, Amazon, Flipkart · May 2026</div>', unsafe_allow_html=True)

    # White space banner
    st.markdown("""
    <div class="gap-banner">
        <h3>🎯 White Space Alert</h3>
        <p>No brand sits at <strong>₹55–₹90/100g</strong>. The mid-premium tier is completely unoccupied.
        A 300g pack at <strong>₹180–₹225</strong> (₹60–₹75/100g) would own this position with zero direct competition.</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📈 Price Landscape", "🗺️ Platform Coverage", "🔍 Brand Deep Dive"])

    with tab1:
        tier_filter = st.multiselect(
            "Filter by tier",
            ["Budget", "Mainstream", "Premium"],
            default=["Budget", "Mainstream", "Premium"],
        )
        df = PRICE_PER_100G[PRICE_PER_100G["Tier"].isin(tier_filter)]

        tier_colors = {"Budget": "#C6EFCE", "Mainstream": "#FFEB9C", "Premium": "#FDBF8E"}
        brand_colors = {
            "Mother's Recipe": "#2E86C1",
            "Patanjali":       "#27AE60",
            "Priya":           "#8E44AD",
            "FarmDidi":        "#D68910",
            "Naagin":          "#C0392B",
        }

        # Scatter: price/100g vs brand
        fig = px.strip(
            df, x="Brand", y="₹/100g", color="Tier",
            hover_data=["Variant", "Pack Size", "Price (₹)", "Platform"],
            color_discrete_map=tier_colors,
            stripmode="overlay",
            title="Price per 100g by Brand — All Variants",
            height=420,
        )
        # Add white space zone
        fig.add_hrect(y0=55, y1=90, fillcolor="#BDD7EE", opacity=0.25,
                      line_width=0, annotation_text="White space ₹55–₹90",
                      annotation_position="right", annotation_font_color="#154360")
        fig.update_traces(marker=dict(size=14, line=dict(width=1, color="white")))
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=13),
            xaxis=dict(gridcolor="#EEE", title=""),
            yaxis=dict(gridcolor="#EEE", title="₹ per 100g", tickprefix="₹"),
            legend=dict(orientation="h", y=-0.15),
        )
        st.plotly_chart(fig, use_container_width=True)

        # Bar chart: cheapest entry price per brand
        entry = df.groupby("Brand")["₹/100g"].min().reset_index().sort_values("₹/100g")
        fig2 = px.bar(
            entry, x="Brand", y="₹/100g",
            color="Brand",
            color_discrete_map=brand_colors,
            title="Cheapest Price/100g per Brand (entry-level pack)",
            text="₹/100g",
            height=360,
        )
        fig2.update_traces(texttemplate="₹%{text}", textposition="outside")
        fig2.add_hrect(y0=55, y1=90, fillcolor="#BDD7EE", opacity=0.2, line_width=0)
        fig2.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=13),
            showlegend=False,
            yaxis=dict(gridcolor="#EEE", tickprefix="₹", title="₹ per 100g"),
            xaxis=dict(title=""),
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("##### Full Pricing Data")
        display_df = df[["Brand", "Variant", "Pack Size", "Price (₹)", "₹/100g", "Tier", "Platform"]].sort_values("₹/100g")

        def color_tier(val):
            colors = {"Budget": "background-color:#C6EFCE", "Mainstream": "background-color:#FFEB9C", "Premium": "background-color:#FDBF8E"}
            return colors.get(val, "")

        st.dataframe(
            display_df.style.applymap(color_tier, subset=["Tier"]),
            use_container_width=True, hide_index=True
        )

    with tab2:
        st.markdown("##### Platform Presence Matrix")
        st.caption("✅ Listed  ·  ⚠️ Partial / unconfirmed  ·  ❌ Not listed  ·  🎯 Target (The 40's Cookbook)")
        st.dataframe(PLATFORM_PRESENCE.set_index("Brand"), use_container_width=True)

        st.markdown("---")
        st.markdown("##### Quick Commerce Gap — Premium Brands")
        qc_data = pd.DataFrame([
            {"Brand": "Mother's Recipe", "On Quick Commerce": True},
            {"Brand": "Priya",           "On Quick Commerce": True},
            {"Brand": "Patanjali",       "On Quick Commerce": False},
            {"Brand": "FarmDidi",        "On Quick Commerce": False},
            {"Brand": "Naagin",          "On Quick Commerce": False},
        ])
        fig3 = px.bar(
            qc_data, x="Brand", y=[1]*5, color="On Quick Commerce",
            color_discrete_map={True: "#27AE60", False: "#E74C3C"},
            title="Quick Commerce Presence (Blinkit + Zepto)",
            labels={"y": "", "On Quick Commerce": "Listed"},
            height=280,
        )
        fig3.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=13),
            yaxis=dict(showticklabels=False, showgrid=False),
            xaxis=dict(title=""),
        )
        fig3.update_traces(showlegend=True)
        st.plotly_chart(fig3, use_container_width=True)
        st.info("🎯 **Opportunity:** FarmDidi and Naagin are both absent from Blinkit/Zepto. The 40's Cookbook can be the **first** premium heritage pickle on quick-commerce.")

    with tab3:
        selected = st.selectbox("Select brand", [c["brand"] for c in COMPETITORS])
        comp = next(c for c in COMPETITORS if c["brand"] == selected)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="card"><div class="section-label">Positioning</div><div style="font-size:1rem;color:#333;margin-top:8px">{comp["positioning"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card"><div class="section-label">Price Range (per 100g)</div><div style="font-size:1.4rem;font-weight:700;color:#C0392B;margin-top:8px">{comp["price_per_100g"]}</div><div style="font-size:0.85rem;color:#666">Entry pack: {comp["entry_price"]}</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="card" style="border-left:4px solid #27AE60"><div class="section-label">Strength</div><div style="font-size:0.95rem;color:#333;margin-top:8px">{comp["strength"]}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card" style="border-left:4px solid #C0392B"><div class="section-label">Weakness / Our Opportunity</div><div style="font-size:0.95rem;color:#333;margin-top:8px">{comp["weakness"]}</div></div>', unsafe_allow_html=True)

        qc_val = "✅ Yes" if comp["quick_commerce"] else "❌ No — opportunity for us"
        st.markdown(f'<div class="card-red"><span class="section-label">Platforms</span><br>{comp["platforms"]}<br><br><span class="section-label">Quick Commerce</span><br>{qc_val}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3 · KEY LEARNINGS
# ─────────────────────────────────────────────────────────────────────────────
elif "Learnings" in page:
    st.markdown('<div class="page-title">Key Learnings</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">6 strategic insights from market research · May 2026 · Blinkit, Zepto, Amazon, Flipkart</div>', unsafe_allow_html=True)

    urgency_filter = st.multiselect("Filter by priority", ["High", "Medium", "Low"], default=["High", "Medium", "Low"])
    filtered = [l for l in LEARNINGS if l["urgency"] in urgency_filter]

    for l in filtered:
        urgency_class = f"urgency-{l['urgency'].lower()}"
        st.markdown(f"""
        <div class="learning-card">
            <div class="learning-num">{l["icon"]}  Learning {l["num"]}</div>
            <div class="learning-title">{l["title"]}</div>
            <div style="display:inline-block;margin-bottom:16px">
                <span class="{urgency_class}">● {l["urgency"]} Priority</span>
            </div>
            <div class="insight-label">Insight</div>
            <div class="insight-text" style="margin-bottom:16px">{l["insight"]}</div>
            <div class="insight-label">Implication for The 40's Cookbook</div>
            <div class="impl-text">{l["implication"]}</div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 4 · GO-TO-MARKET
# ─────────────────────────────────────────────────────────────────────────────
elif "Go-to-Market" in page:
    st.markdown('<div class="page-title">Go-to-Market Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Launch sequencing · Channel strategy · Content pillars</div>', unsafe_allow_html=True)

    st.markdown("#### Launch Sequence")
    phase_colors = ["#C0392B", "#E67E22", "#F4D03F", "#27AE60", "#2980B9"]
    for i, phase in enumerate(GTM_PHASES):
        col = phase_colors[i % len(phase_colors)]
        st.markdown(f"""
        <div class="card" style="border-left:5px solid {col};padding:18px 24px;margin-bottom:12px">
            <div style="display:flex;align-items:center;gap:16px">
                <div style="min-width:90px">
                    <div style="font-size:0.7rem;color:#999;text-transform:uppercase;letter-spacing:0.1em">Timeline</div>
                    <div style="font-weight:700;color:{col};font-size:1rem">{phase["Month"]}</div>
                </div>
                <div style="min-width:160px">
                    <div style="font-size:0.7rem;color:#999;text-transform:uppercase;letter-spacing:0.1em">Phase</div>
                    <div style="font-weight:600;color:#333;font-size:0.95rem">{phase["Phase"]}</div>
                </div>
                <div style="flex:1">
                    <div style="font-size:0.7rem;color:#999;text-transform:uppercase;letter-spacing:0.1em">Actions</div>
                    <div style="color:#444;font-size:0.9rem">{phase["Actions"]}</div>
                </div>
                <div style="font-size:1.1rem">{phase["Status"]}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.divider()

    left, right = st.columns(2)

    with left:
        st.markdown("#### Content Pillars")
        pillars = [
            ("🧓 Madhu & Heritage", "The founder, the recipe, Banaras. Emotional, long-form. Used sparingly — high signal.", "#C0392B"),
            ("🍽️ Product on the Table", "Beautiful flat-lays, dinner-party content, pickle as centerpiece.", "#E67E22"),
            ("👨‍🍳 Recipes & Use", "Chefs and creators using the pickle in modern dishes.", "#27AE60"),
            ("🫙 Design & Object", "The bottle as object. Unboxing, shelf shots, gifting.", "#2980B9"),
        ]
        for icon_title, desc, col in pillars:
            st.markdown(f"""
            <div class="card" style="border-top:3px solid {col};margin-bottom:12px;padding:16px 20px">
                <div style="font-weight:700;color:{col};margin-bottom:6px">{icon_title}</div>
                <div style="font-size:0.88rem;color:#555">{desc}</div>
            </div>""", unsafe_allow_html=True)

    with right:
        st.markdown("#### Channel Strategy")
        channels = [
            ("🏪 Retail Stores", "Modern Bazaar, Nature's Basket, Le Marché", "Month 2"),
            ("🍴 Restaurants", "Plate-side condiment, brand proof point", "Month 2"),
            ("⚡ Quick Commerce", "Blinkit, Zepto, Instamart — high-intent metro buyer", "Month 4"),
            ("🌐 D2C Website", "Own channel — full margin, brand control", "Month 4"),
            ("📦 Amazon / Flipkart", "Discovery + gifting. MAP-controlled.", "Month 4"),
            ("💬 Communities", "WhatsApp groups, MyGate societies, Gurgaon DLF", "Day 1"),
        ]
        for ch, desc, timing in channels:
            st.markdown(f"""
            <div style="padding:14px 0;border-bottom:1px solid #EEE">
                <div style="display:flex;justify-content:space-between;align-items:start">
                    <div>
                        <div style="font-weight:600;color:#333;font-size:0.92rem">{ch}</div>
                        <div style="font-size:0.82rem;color:#777;margin-top:3px">{desc}</div>
                    </div>
                    <div style="font-size:0.75rem;color:#C0392B;font-weight:600;white-space:nowrap;padding-left:16px">{timing}</div>
                </div>
            </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 5 · OPEN QUESTIONS
# ─────────────────────────────────────────────────────────────────────────────
elif "Questions" in page:
    st.markdown('<div class="page-title">Open Questions & Next Steps</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Decisions needed before launch · Assign owners and track here</div>', unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        st.markdown("#### Open Questions")
        st.caption("Decisions that are still unresolved")
        for i, q in enumerate(OPEN_QUESTIONS):
            answered = st.checkbox(q, key=f"q_{i}")
            if answered:
                st.markdown(f'<div style="margin:-8px 0 12px 28px"><input type="text" placeholder="Note your answer..." style="width:100%;padding:6px 10px;border:1px solid #ddd;border-radius:6px;font-size:0.85rem;color:#333" /></div>', unsafe_allow_html=True)

    with right:
        st.markdown("#### Next Work Streams")
        st.caption("Ordered by urgency · Check off as complete")
        stream_urgency = ["High", "High", "Medium", "High", "Medium"]
        for i, s in enumerate(NEXT_STEPS):
            done = st.checkbox(f"**{i+1}.** {s}", key=f"ns_{i}")

    st.divider()

    st.markdown("#### Share This Dashboard")
    st.info("""
**To share with partners:**

1. Run `streamlit run app.py` locally and share your screen, **or**
2. Deploy to Streamlit Community Cloud (free):
   - Push this folder to a GitHub repo
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect the repo — get a public URL in ~2 minutes
3. For password protection: add `[passwords]` to `.streamlit/secrets.toml`

**To add partner comments / notes:** Consider connecting a Google Sheet as a backend — I can wire that up in a follow-up session.
    """)

    with st.expander("Version history"):
        st.markdown("""
| Version | Date | Changes |
|---|---|---|
| 1.0 | May 2026 | Initial brand foundation + competitor research |
        """)
