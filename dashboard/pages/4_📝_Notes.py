"""Collaborative Notes — The 40's Cookbook"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import styles, db

st.set_page_config(page_title="Notes — 40's Cookbook", layout="wide", page_icon="📝")
styles.inject()

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    styles.sidebar_brand("Notes")
    author = styles.author_input()
    st.divider()

    st.markdown("### New Note")
    with st.form("new_note_form", clear_on_submit=True):
        n_title   = st.text_input("Title *")
        n_content = st.text_area("Content (markdown supported)", height=180,
                                 placeholder="Write anything — meeting notes, decisions, action items…")
        n_tags_raw = st.text_input("Tags", placeholder="vendor, pricing, design  (comma separated)")
        submitted  = st.form_submit_button("Save Note", type="primary", use_container_width=True)

    if submitted:
        if not n_title:
            st.error("Title is required.")
        elif not author:
            st.error("Enter your name at the top before saving.")
        else:
            tags = [t.strip() for t in n_tags_raw.split(",") if t.strip()]
            db.save_note(title=n_title, content=n_content, author=author, tags=tags)
            st.success("Note saved!")
            st.rerun()

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Notes</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Shared notes from every meeting, call, and decision — visible to your whole team</div>', unsafe_allow_html=True)

# ── Search + filters ───────────────────────────────────────────────────────────
s1, s2 = st.columns([3, 2])
with s1:
    search = st.text_input("Search", placeholder="Search by title…", label_visibility="collapsed")
with s2:
    filter_author = st.text_input("Filter by author", placeholder="Filter by author name…",
                                  label_visibility="collapsed")

# ── Load notes ─────────────────────────────────────────────────────────────────
notes = db.get_notes(search=search if search else None)

if filter_author:
    fa = filter_author.lower()
    notes = [n for n in notes if fa in (n.get("author") or "").lower()]

# ── Summary ────────────────────────────────────────────────────────────────────
st.caption(f"{len(notes)} note{'s' if len(notes) != 1 else ''}")

if not notes:
    st.info("No notes yet. Add the first one using the sidebar.")
    st.stop()

# ── Notes grid ─────────────────────────────────────────────────────────────────
if "editing_note" not in st.session_state:
    st.session_state.editing_note = None

cols_per_row = 2
for i in range(0, len(notes), cols_per_row):
    row_notes = notes[i:i + cols_per_row]
    cols = st.columns(cols_per_row)

    for col, note in zip(cols, row_notes):
        with col:
            # Tag pills
            tags_html = ""
            for tag in (note.get("tags") or []):
                tags_html += (
                    f'<span style="background:#FDF0EC;color:#C0392B;'
                    f'padding:2px 8px;border-radius:12px;font-size:0.7rem;'
                    f'font-weight:600;margin-right:4px">{tag}</span>'
                )

            updated = (note.get("updated_at") or note.get("created_at") or "")[:10]
            author_name = note.get("author") or "Unknown"

            # Card header
            st.markdown(f"""
<div style="background:white;border:1px solid #E8E0D8;border-radius:12px;
            padding:18px 20px;margin-bottom:8px;
            box-shadow:0 2px 6px rgba(0,0,0,0.04);">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px">
        <div style="font-family:'Playfair Display',serif;font-size:1.05rem;
                    font-weight:600;color:#1A1A1A;line-height:1.3">{note['title']}</div>
        <div style="font-size:0.72rem;color:#999;white-space:nowrap;padding-left:12px">{updated}</div>
    </div>
    <div style="font-size:0.78rem;color:#888;margin-bottom:10px">by {author_name}</div>
    {tags_html}
</div>""", unsafe_allow_html=True)

            # Content preview or edit mode
            is_editing = st.session_state.editing_note == note["id"]

            if is_editing:
                with st.form(f"edit_note_{note['id']}"):
                    edit_title   = st.text_input("Title", value=note["title"])
                    edit_content = st.text_area("Content", value=note.get("content") or "", height=200)
                    edit_tags_raw = st.text_input("Tags", value=", ".join(note.get("tags") or []))
                    c1, c2, c3 = st.columns(3)
                    save_btn   = c1.form_submit_button("Save", type="primary", use_container_width=True)
                    cancel_btn = c2.form_submit_button("Cancel", use_container_width=True)
                    delete_btn = c3.form_submit_button("Delete", use_container_width=True)

                if save_btn:
                    new_tags = [t.strip() for t in edit_tags_raw.split(",") if t.strip()]
                    db.update_note(note["id"], title=edit_title, content=edit_content, tags=new_tags)
                    st.session_state.editing_note = None
                    st.rerun()
                if cancel_btn:
                    st.session_state.editing_note = None
                    st.rerun()
                if delete_btn:
                    db.delete_note(note["id"])
                    st.session_state.editing_note = None
                    st.rerun()

            else:
                content = note.get("content") or ""
                with st.expander("Read note", expanded=False):
                    st.markdown(content if content else "*No content.*")

                if st.button("Edit", key=f"edit_{note['id']}", use_container_width=True):
                    st.session_state.editing_note = note["id"]
                    st.rerun()

    # Pad the row if odd number of notes
    if len(row_notes) < cols_per_row:
        for _ in range(cols_per_row - len(row_notes)):
            st.columns(cols_per_row)[len(row_notes)].empty()
