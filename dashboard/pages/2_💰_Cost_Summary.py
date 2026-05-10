"""Cost Summary — The 40's Cookbook"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import styles, db

st.set_page_config(page_title="Cost Summary — 40's Cookbook", layout="wide", page_icon="💰")
styles.inject()

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    styles.sidebar_brand("Cost Summary")
    author = styles.author_input()
    st.divider()

    vendors = db.get_vendors()
    vendor_options = {v["name"]: v["id"] for v in vendors}

    st.markdown("### Add Cost Entry")
    with st.form("add_cost_form", clear_on_submit=True):
        if not vendor_options:
            st.info("Add vendors first in the Vendors tab.")
            st.form_submit_button("Add Cost", disabled=True, use_container_width=True)
        else:
            sel_vendor = st.selectbox("Vendor *", list(vendor_options.keys()))
            item_desc  = st.text_input("Item / SKU *", placeholder="e.g. 500ml Glass Jar")
            unit       = st.text_input("Unit", placeholder="per piece, per kg, per carton…")
            quantity   = st.number_input("Quantity", min_value=0.0, value=1.0, step=1.0)
            price_unit = st.number_input("Price per unit (₹) *", min_value=0.0, step=0.5)
            moq        = st.text_input("MOQ", placeholder="e.g. 500 pieces")
            dq         = st.date_input("Date quoted", value=date.today())
            cost_notes = st.text_area("Notes", height=60)
            submitted  = st.form_submit_button("Add Cost", type="primary", use_container_width=True)

    if vendor_options and submitted:
        if not item_desc or price_unit <= 0:
            st.error("Item description and price are required.")
        else:
            db.add_cost(
                vendor_id=vendor_options[sel_vendor],
                item_description=item_desc,
                unit=unit,
                quantity=quantity,
                price_per_unit=price_unit,
                moq=moq,
                date_quoted=dq,
                notes=cost_notes,
            )
            st.success("Cost entry added!")
            st.rerun()

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Cost Summary</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">All vendor quotes in one place — compare, filter, export</div>', unsafe_allow_html=True)

# ── Load data ──────────────────────────────────────────────────────────────────
costs_raw = db.get_costs()

if not costs_raw:
    st.info("No cost entries yet. Add vendors first, then log quotes using the sidebar.")
    st.stop()

# Build flat DataFrame
rows = []
for c in costs_raw:
    vendor_info = c.get("vendors") or {}
    vendor_name = vendor_info.get("name", "Unknown") if isinstance(vendor_info, dict) else "Unknown"
    vendor_cat  = vendor_info.get("category", "Other") if isinstance(vendor_info, dict) else "Other"
    total       = (c.get("quantity") or 1) * (c.get("price_per_unit") or 0)
    rows.append({
        "id":           c["id"],
        "Vendor":       vendor_name,
        "Category":     vendor_cat,
        "Item":         c.get("item_description", ""),
        "Unit":         c.get("unit", ""),
        "Qty":          c.get("quantity", 1),
        "₹ / Unit":     c.get("price_per_unit", 0),
        "Total (₹)":    total,
        "MOQ":          c.get("moq", ""),
        "Date Quoted":  c.get("date_quoted", ""),
        "Notes":        c.get("notes", ""),
    })

df = pd.DataFrame(rows)

# ── Summary metrics ────────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f'<div class="metric-card"><div class="section-label">Total Entries</div><div style="font-size:2rem;font-weight:700;color:#C0392B">{len(df)}</div></div>', unsafe_allow_html=True)
with m2:
    unique_vendors = df["Vendor"].nunique()
    st.markdown(f'<div class="metric-card"><div class="section-label">Vendors Quoted</div><div style="font-size:2rem;font-weight:700;color:#C0392B">{unique_vendors}</div></div>', unsafe_allow_html=True)
with m3:
    total_cost = df["Total (₹)"].sum()
    st.markdown(f'<div class="metric-card"><div class="section-label">Total Quoted</div><div style="font-size:1.6rem;font-weight:700;color:#C0392B">₹{total_cost:,.0f}</div></div>', unsafe_allow_html=True)
with m4:
    avg_per_vendor = total_cost / unique_vendors if unique_vendors else 0
    st.markdown(f'<div class="metric-card"><div class="section-label">Avg / Vendor</div><div style="font-size:1.6rem;font-weight:700;color:#C0392B">₹{avg_per_vendor:,.0f}</div></div>', unsafe_allow_html=True)

st.divider()

# ── Charts ─────────────────────────────────────────────────────────────────────
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    cat_totals = df.groupby("Category")["Total (₹)"].sum().reset_index().sort_values("Total (₹)", ascending=False)
    fig1 = px.bar(
        cat_totals, x="Category", y="Total (₹)",
        color="Category",
        color_discrete_map=styles.CATEGORY_COLORS,
        title="Total Cost by Vendor Category",
        text="Total (₹)",
        height=360,
    )
    fig1.update_traces(texttemplate="₹%{text:,.0f}", textposition="outside")
    fig1.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="Inter", size=12),
        showlegend=False,
        yaxis=dict(gridcolor="#EEE", tickprefix="₹", title=""),
        xaxis=dict(title=""),
        title_font=dict(size=14),
    )
    st.plotly_chart(fig1, use_container_width=True)

with chart_col2:
    vendor_totals = df.groupby("Vendor")["Total (₹)"].sum().reset_index().sort_values("Total (₹)", ascending=False)
    fig2 = px.pie(
        vendor_totals, names="Vendor", values="Total (₹)",
        title="Cost Share by Vendor",
        hole=0.4,
        height=360,
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig2.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="Inter", size=12),
        title_font=dict(size=14),
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── Filter + table ─────────────────────────────────────────────────────────────
st.markdown("### All Cost Entries")

t1, t2 = st.columns([2, 2])
with t1:
    filter_vendor = st.multiselect("Filter by vendor", df["Vendor"].unique().tolist())
with t2:
    filter_cat2 = st.multiselect("Filter by category", df["Category"].unique().tolist())

display_df = df.copy()
if filter_vendor:
    display_df = display_df[display_df["Vendor"].isin(filter_vendor)]
if filter_cat2:
    display_df = display_df[display_df["Category"].isin(filter_cat2)]

# Display without the id column
display_cols = ["Vendor", "Category", "Item", "Unit", "Qty", "₹ / Unit", "Total (₹)", "MOQ", "Date Quoted", "Notes"]
st.dataframe(
    display_df[display_cols].style.format({"₹ / Unit": "₹{:.2f}", "Total (₹)": "₹{:,.0f}"}),
    use_container_width=True,
    hide_index=True,
)

# Export
csv = display_df[display_cols].to_csv(index=False)
st.download_button(
    "Download CSV",
    data=csv,
    file_name="40s_cookbook_costs.csv",
    mime="text/csv",
)

# ── Delete entries ─────────────────────────────────────────────────────────────
with st.expander("Delete a cost entry"):
    if display_df.empty:
        st.caption("No entries to delete.")
    else:
        del_options = {
            f"{r['Vendor']} — {r['Item']} (₹{r['₹ / Unit']})": r["id"]
            for _, r in display_df.iterrows()
        }
        del_choice = st.selectbox("Select entry to delete", list(del_options.keys()))
        if st.button("Delete entry", type="primary"):
            db.delete_cost(del_options[del_choice])
            st.success("Deleted.")
            st.rerun()
