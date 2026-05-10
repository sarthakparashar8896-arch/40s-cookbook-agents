"""Vendor Pipeline Tracker — The 40's Cookbook"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import styles, db

st.set_page_config(page_title="Vendors — 40's Cookbook", layout="wide", page_icon="🏭")
styles.inject()

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    styles.sidebar_brand("Vendor Pipeline")
    author = styles.author_input()
    st.divider()

    st.markdown("### Add Vendor")
    with st.form("add_vendor_form", clear_on_submit=True):
        v_name     = st.text_input("Vendor name *")
        v_cat      = st.selectbox("Category *", db.VENDOR_CATEGORIES)
        v_stage    = st.selectbox("Initial stage", db.VENDOR_STAGES)
        v_contact  = st.text_input("Contact name")
        v_email    = st.text_input("Email")
        v_phone    = st.text_input("Phone")
        v_location = st.text_input("Location / City")
        v_notes    = st.text_area("Initial notes", height=80)
        submitted  = st.form_submit_button("Add Vendor", type="primary", use_container_width=True)

    if submitted:
        if not v_name:
            st.error("Vendor name is required.")
        else:
            vendor = db.add_vendor(
                name=v_name, category=v_cat, stage=v_stage,
                contact_name=v_contact, contact_email=v_email,
                contact_phone=v_phone, location=v_location,
                notes=v_notes, created_by=author,
            )
            db.add_vendor_update(
                vendor_id=vendor["id"], stage_from="", stage_to=v_stage,
                notes=f"Vendor added. {v_notes}".strip(), author=author,
            )
            st.success(f"Added {v_name}!")
            st.rerun()

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Vendor Pipeline</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Track all supplier relationships — from first contact to closed deal</div>', unsafe_allow_html=True)

# ── Filters ────────────────────────────────────────────────────────────────────
f1, f2, f3 = st.columns([2, 2, 3])
with f1:
    filter_cat = st.selectbox("Category", ["All"] + db.VENDOR_CATEGORIES,
                              label_visibility="collapsed", key="fcat")
with f2:
    filter_stage = st.selectbox("Stage", ["All"] + db.VENDOR_STAGES,
                                label_visibility="collapsed", key="fstage")
with f3:
    search = st.text_input("Search", placeholder="Search by name or location…",
                           label_visibility="collapsed")

# ── Load vendors ───────────────────────────────────────────────────────────────
vendors = db.get_vendors(
    category=filter_cat if filter_cat != "All" else None,
    stage=filter_stage if filter_stage != "All" else None,
)
if search:
    q = search.lower()
    vendors = [v for v in vendors
               if q in v["name"].lower() or q in (v.get("location") or "").lower()]

# ── Stage summary bar ──────────────────────────────────────────────────────────
by_stage_count = {s: 0 for s in db.VENDOR_STAGES}
for v in vendors:
    by_stage_count[v["stage"]] = by_stage_count.get(v["stage"], 0) + 1

cols = st.columns(len(db.VENDOR_STAGES))
for col, stage in zip(cols, db.VENDOR_STAGES):
    bg, fg = styles.STAGE_COLORS.get(stage, ("#F5F5F5", "#333"))
    count  = by_stage_count.get(stage, 0)
    col.markdown(f"""
<div style="background:{bg};border-radius:10px;padding:14px 8px;text-align:center;margin-bottom:16px">
    <div style="font-size:1.5rem;font-weight:700;color:{fg}">{count}</div>
    <div style="font-size:0.65rem;font-weight:600;color:{fg};text-transform:uppercase;letter-spacing:0.08em;line-height:1.3">{stage}</div>
</div>""", unsafe_allow_html=True)

st.divider()

# ── Kanban board ───────────────────────────────────────────────────────────────
if not vendors:
    st.info("No vendors yet. Use the sidebar to add your first one.")
    st.stop()

by_stage_vendors = {s: [] for s in db.VENDOR_STAGES}
for v in vendors:
    by_stage_vendors.get(v["stage"], by_stage_vendors["Reached Out"]).append(v)

board_cols = st.columns(len(db.VENDOR_STAGES))
for col, stage in zip(board_cols, db.VENDOR_STAGES):
    bg, fg = styles.STAGE_COLORS.get(stage, ("#F5F5F5", "#333"))
    stage_vendors = by_stage_vendors[stage]
    with col:
        st.markdown(f"""
<div style="background:{bg};border-radius:8px 8px 0 0;padding:8px 12px;margin-bottom:4px">
    <span style="font-size:0.68rem;font-weight:700;color:{fg};text-transform:uppercase;letter-spacing:0.1em">
        {stage} &nbsp;({len(stage_vendors)})
    </span>
</div>""", unsafe_allow_html=True)

        for v in stage_vendors:
            cat_color = styles.CATEGORY_COLORS.get(v["category"], "#7F8C8D")
            note_preview = (v.get("notes") or "")[:70]
            if len(v.get("notes") or "") > 70:
                note_preview += "…"

            with st.expander(v["name"], expanded=False):
                # Category badge
                st.markdown(
                    f'<span style="background:{cat_color}22;color:{cat_color};'
                    f'padding:2px 9px;border-radius:12px;font-size:0.7rem;font-weight:600">'
                    f'{v["category"]}</span>',
                    unsafe_allow_html=True,
                )
                st.markdown("")

                if v.get("location"):
                    st.markdown(f"📍 {v['location']}")
                if v.get("contact_name"):
                    st.markdown(f"👤 {v['contact_name']}")
                if v.get("contact_email"):
                    st.markdown(f"✉️ {v['contact_email']}")
                if v.get("contact_phone"):
                    st.markdown(f"📞 {v['contact_phone']}")
                if note_preview:
                    st.caption(note_preview)

                st.divider()

                # Stage + note update
                current_idx = db.VENDOR_STAGES.index(v["stage"]) if v["stage"] in db.VENDOR_STAGES else 0
                new_stage   = st.selectbox(
                    "Stage", db.VENDOR_STAGES,
                    index=current_idx,
                    key=f"st_{v['id']}",
                )
                new_note = st.text_input(
                    "Add update note", key=f"note_{v['id']}",
                    placeholder="What happened? Pricing discussed, sample received…",
                )
                new_vendor_notes = st.text_area(
                    "Vendor notes", value=v.get("notes") or "",
                    key=f"vnotes_{v['id']}", height=70,
                )

                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button("Save", key=f"save_{v['id']}", use_container_width=True, type="primary"):
                        stage_changed = new_stage != v["stage"]
                        db.update_vendor(v["id"], stage=new_stage, notes=new_vendor_notes)
                        if stage_changed or new_note:
                            db.add_vendor_update(
                                vendor_id=v["id"],
                                stage_from=v["stage"], stage_to=new_stage,
                                notes=new_note, author=author,
                            )
                        st.rerun()
                with btn_col2:
                    if st.button("Delete", key=f"del_{v['id']}", use_container_width=True):
                        db.delete_vendor(v["id"])
                        st.rerun()

                # Timeline
                updates = db.get_vendor_updates(v["id"])
                if updates:
                    st.markdown("**Timeline**")
                    for u in updates[:6]:
                        ts = u["created_at"][:10]
                        sf, st_ = u.get("stage_from", ""), u.get("stage_to", "")
                        moved  = sf and st_ and sf != st_
                        note   = u.get("notes", "")
                        who    = u.get("author") or "?"
                        if moved:
                            line = f"📌 `{ts}` {sf} → **{st_}**"
                        else:
                            line = f"💬 `{ts}`"
                        if note:
                            line += f" — {note}"
                        line += f" · *{who}*"
                        st.markdown(f"<small>{line}</small>", unsafe_allow_html=True)
