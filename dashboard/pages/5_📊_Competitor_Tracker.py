"""Competitor Price Tracker — The 40's Cookbook"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta
import anthropic
import styles, db

st.set_page_config(page_title="Competitor Tracker — 40's Cookbook", layout="wide", page_icon="📊")
styles.inject()

# ── Helpers ────────────────────────────────────────────────────────────────────
def this_monday() -> date:
    today = date.today()
    return today - timedelta(days=today.weekday())


def price_per_100g(price_inr: float, pack_size_g: float) -> float:
    if pack_size_g and pack_size_g > 0:
        return round(price_inr / pack_size_g * 100, 2)
    return 0.0


def get_anthropic_client():
    api_key = st.secrets.get("ANTHROPIC_API_KEY", "") or os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.error("ANTHROPIC_API_KEY not set. Add it to `.streamlit/secrets.toml`.")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def run_ai_research() -> list:
    client  = get_anthropic_client()
    today   = date.today().isoformat()
    brands  = ", ".join(db.COMPETITOR_BRANDS)
    prompt  = f"""You are researching current Indian pickle prices as of {today}.

For each of these brands: {brands}

Find the most commonly sold pickle SKU (mango or mixed pickle), its pack size in grams,
current price in INR, and which platform (Blinkit, Zepto, Amazon, Flipkart, BigBasket).

Return ONLY a JSON array, no other text, in exactly this format:
[
  {{"brand": "Mother's Recipe", "product_name": "Mango Pickle", "pack_size_g": 400, "price_inr": 89, "platform": "Amazon"}},
  ...
]

Only include entries where you are reasonably confident. Skip brands you have no price data for."""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.content[0].text.strip()
    # Extract JSON array from response
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        return []
    return json.loads(match.group(0))


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    styles.sidebar_brand("Competitor Tracker")
    author = styles.author_input()
    st.divider()

    st.markdown("### Add Price Entry")
    with st.form("add_price_form", clear_on_submit=True):
        brand      = st.selectbox("Brand *", db.COMPETITOR_BRANDS + ["Other"])
        prod_name  = st.text_input("Product name", placeholder="e.g. Mango Pickle 400g")
        pack_size  = st.number_input("Pack size (g) *", min_value=1.0, value=400.0, step=50.0)
        price_inr  = st.number_input("Price (₹) *", min_value=0.0, value=89.0, step=1.0)
        platform   = st.selectbox("Platform", db.COMPETITOR_PLATFORMS)
        week_of    = st.date_input("Week of", value=this_monday())
        p_notes    = st.text_input("Notes", placeholder="Sale price, out of stock, etc.")
        submitted  = st.form_submit_button("Save Price", type="primary", use_container_width=True)

    if submitted:
        if price_inr <= 0 or pack_size <= 0:
            st.error("Price and pack size are required.")
        else:
            db.save_competitor_price(
                brand=brand, product_name=prod_name,
                pack_size_g=pack_size, price_inr=price_inr,
                platform=platform, week_of=week_of,
                source="manual", verified=True,
                recorded_by=author, notes=p_notes,
            )
            st.success("Price saved!")
            st.rerun()

    st.divider()

    # AI research button
    st.markdown("### AI Price Research")
    st.caption("Uses the Market Researcher agent to estimate current prices. Review before saving.")
    if st.button("Research with AI", use_container_width=True, type="primary"):
        st.session_state.ai_research_results = None
        with st.spinner("Researching…"):
            try:
                results = run_ai_research()
                st.session_state.ai_research_results = results
            except Exception as e:
                st.error(f"Research failed: {e}")
        st.rerun()

# ── Header + Last Updated ──────────────────────────────────────────────────────
st.markdown('<div class="page-title">Competitor Price Tracker</div>', unsafe_allow_html=True)

last_updated = db.get_latest_recorded_at()
if last_updated:
    from datetime import datetime
    try:
        dt = datetime.fromisoformat(last_updated.replace("Z", "+00:00"))
        label = dt.strftime("Last updated %d %b %Y, %H:%M")
    except Exception:
        label = f"Last updated {last_updated[:10]}"
    st.markdown(f'<div class="last-updated">🕐 {label}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="last-updated">No data yet — add entries or use AI Research</div>', unsafe_allow_html=True)

st.markdown('<div class="page-subtitle">Weekly price benchmarks across competitors — tracked every Monday</div>', unsafe_allow_html=True)

# ── AI Research results panel ──────────────────────────────────────────────────
if "ai_research_results" in st.session_state and st.session_state.ai_research_results is not None:
    results = st.session_state.ai_research_results
    if results:
        st.info(f"AI found **{len(results)}** price estimates. Review and confirm which to save:")
        monday = this_monday()

        selected_indices = []
        for idx, r in enumerate(results):
            p100 = price_per_100g(r.get("price_inr", 0), r.get("pack_size_g", 0))
            checked = st.checkbox(
                f"**{r['brand']}** — {r.get('product_name', '')} | "
                f"{r.get('pack_size_g', '?')}g | ₹{r.get('price_inr', '?')} | "
                f"₹{p100}/100g | {r.get('platform', '?')}",
                value=True, key=f"ai_check_{idx}",
            )
            if checked:
                selected_indices.append(idx)

        col_save, col_discard = st.columns(2)
        with col_save:
            if st.button("Save selected", type="primary"):
                for idx in selected_indices:
                    r = results[idx]
                    db.save_competitor_price(
                        brand=r["brand"],
                        product_name=r.get("product_name", ""),
                        pack_size_g=r.get("pack_size_g", 0),
                        price_inr=r.get("price_inr", 0),
                        platform=r.get("platform", ""),
                        week_of=monday,
                        source="ai_research",
                        verified=False,
                        recorded_by=author or "AI",
                        notes="AI estimate — verify before use",
                    )
                st.session_state.ai_research_results = None
                st.success(f"Saved {len(selected_indices)} entries.")
                st.rerun()
        with col_discard:
            if st.button("Discard all"):
                st.session_state.ai_research_results = None
                st.rerun()
    else:
        st.warning("AI research returned no results. Try adding prices manually.")
        if st.button("Clear"):
            st.session_state.ai_research_results = None
            st.rerun()
    st.divider()

# ── Load all price data ────────────────────────────────────────────────────────
all_prices = db.get_competitor_prices()

if not all_prices:
    st.info("No competitor prices recorded yet. Use the sidebar to add entries or click 'Research with AI'.")
    st.stop()

# Build DataFrame with computed price/100g
rows = []
for p in all_prices:
    p100 = price_per_100g(p.get("price_inr", 0), p.get("pack_size_g", 0))
    rows.append({
        "id":          p["id"],
        "Brand":       p["brand"],
        "Product":     p.get("product_name", ""),
        "Pack (g)":    p.get("pack_size_g", 0),
        "Price (₹)":   p.get("price_inr", 0),
        "₹/100g":      p100,
        "Platform":    p.get("platform", ""),
        "Week Of":     p.get("week_of", ""),
        "Source":      p.get("source", "manual"),
        "Verified":    p.get("verified", True),
        "Recorded By": p.get("recorded_by", ""),
        "Notes":       p.get("notes", ""),
    })

df = pd.DataFrame(rows)
df["Week Of"] = pd.to_datetime(df["Week Of"])

# ── Brand filter ───────────────────────────────────────────────────────────────
available_brands = sorted(df["Brand"].unique().tolist())
selected_brands  = st.multiselect(
    "Brands to display", available_brands,
    default=available_brands,
    key="brand_filter",
)
df_filtered = df[df["Brand"].isin(selected_brands)] if selected_brands else df

# ── White space banner ─────────────────────────────────────────────────────────
current_week_df = df_filtered[df_filtered["Week Of"] == df_filtered["Week Of"].max()]
if not current_week_df.empty:
    min_p = current_week_df["₹/100g"].min()
    max_p = current_week_df["₹/100g"].max()
    st.markdown(f"""
<div style="background:linear-gradient(135deg,#154360 0%,#1A5276 100%);color:white;
            padding:16px 24px;border-radius:12px;margin-bottom:20px">
    <span style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.15em;color:#BDD7EE">
        Current Week Range
    </span><br>
    <span style="font-size:1.1rem;font-weight:500">
        Competitors: ₹{min_p:.0f}–₹{max_p:.0f}/100g &nbsp;|&nbsp;
        <strong>White space: ₹55–₹90/100g</strong> — unoccupied mid-premium tier
    </span>
</div>""", unsafe_allow_html=True)

# ── Charts ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📈 Trends Over Time", "📊 Current Week", "🗃 Raw Data"])

with tab1:
    if df_filtered["Week Of"].nunique() < 2:
        st.info("Need at least 2 weeks of data to show trends. Current data shown as scatter below.")
        fig = px.scatter(
            df_filtered, x="Brand", y="₹/100g",
            color="Brand",
            color_discrete_map=styles.BRAND_COLORS,
            hover_data=["Product", "Pack (g)", "Price (₹)", "Platform", "Week Of"],
            title="Price per 100g — All Entries",
            height=420,
        )
    else:
        weekly_avg = (df_filtered
                      .groupby(["Week Of", "Brand"])["₹/100g"]
                      .mean()
                      .reset_index()
                      .rename(columns={"₹/100g": "Avg ₹/100g"}))
        fig = px.line(
            weekly_avg, x="Week Of", y="Avg ₹/100g",
            color="Brand",
            color_discrete_map=styles.BRAND_COLORS,
            markers=True,
            title="Price per 100g Over Time (weekly average)",
            height=420,
        )

    fig.add_hrect(y0=55, y1=90, fillcolor="#BDD7EE", opacity=0.2, line_width=0,
                  annotation_text="White space ₹55–₹90",
                  annotation_position="top right",
                  annotation_font_color="#154360")
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="Inter", size=12),
        yaxis=dict(gridcolor="#EEE", tickprefix="₹", title="₹ per 100g"),
        xaxis=dict(gridcolor="#EEE", title=""),
        legend=dict(orientation="h", y=-0.2),
        title_font=dict(size=14),
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    if current_week_df.empty:
        st.info("No data for the current week. Select an older week in the filter or add new entries.")
    else:
        brand_avg = (current_week_df
                     .groupby("Brand")["₹/100g"]
                     .mean()
                     .reset_index()
                     .sort_values("₹/100g"))
        fig2 = px.bar(
            brand_avg, x="Brand", y="₹/100g",
            color="Brand",
            color_discrete_map=styles.BRAND_COLORS,
            title=f"Price per 100g — Week of {current_week_df['Week Of'].max().strftime('%d %b %Y')}",
            text="₹/100g",
            height=400,
        )
        fig2.update_traces(texttemplate="₹%{text:.0f}", textposition="outside")
        fig2.add_hrect(y0=55, y1=90, fillcolor="#BDD7EE", opacity=0.2, line_width=0,
                       annotation_text="White space",
                       annotation_font_color="#154360")
        fig2.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=12),
            showlegend=False,
            yaxis=dict(gridcolor="#EEE", tickprefix="₹", title="₹ per 100g"),
            xaxis=dict(title=""),
            title_font=dict(size=14),
        )
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("**Current week detail**")
        show_cols = ["Brand", "Product", "Pack (g)", "Price (₹)", "₹/100g", "Platform", "Verified"]
        st.dataframe(
            current_week_df[show_cols].sort_values("₹/100g"),
            use_container_width=True,
            hide_index=True,
        )

with tab3:
    show_all_cols = ["Brand", "Product", "Pack (g)", "Price (₹)", "₹/100g",
                     "Platform", "Week Of", "Source", "Verified", "Recorded By", "Notes"]
    df_display = df_filtered[show_all_cols].copy()
    df_display["Week Of"] = df_display["Week Of"].dt.strftime("%Y-%m-%d")
    st.dataframe(df_display.sort_values("Week Of", ascending=False), use_container_width=True, hide_index=True)

    csv = df_display.to_csv(index=False)
    st.download_button("Download CSV", data=csv,
                       file_name="competitor_prices.csv", mime="text/csv")

    with st.expander("Delete an entry"):
        del_options = {
            f"{r['Brand']} — {r['Product']} | Week {r['Week Of']}": r["id"]
            for _, r in df_filtered.iterrows()
        }
        if del_options:
            del_choice = st.selectbox("Select", list(del_options.keys()))
            if st.button("Delete", type="primary"):
                db.delete_competitor_price(del_options[del_choice])
                st.rerun()
