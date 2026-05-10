"""Shared visual styles for The 40's Cookbook dashboard."""
import streamlit as st

STAGE_COLORS = {
    "Reached Out":   ("#E8EAF6", "#3949AB"),
    "In Discussion": ("#FFF3E0", "#E65100"),
    "Negotiation":   ("#FFF8E1", "#F57F17"),
    "Sampling":      ("#E8F5E9", "#2E7D32"),
    "Closed Won":    ("#EFEBE9", "#4E342E"),
    "Closed Lost":   ("#F5F5F5", "#9E9E9E"),
}

CATEGORY_COLORS = {
    "Pickle Manufacturing": "#C0392B",
    "Glass Jars":           "#2980B9",
    "Labels & Printing":    "#27AE60",
    "Packaging":            "#8E44AD",
    "Logistics":            "#D68910",
    "Other":                "#7F8C8D",
}

BRAND_COLORS = {
    "Mother's Recipe": "#2E86C1",
    "Tops":            "#27AE60",
    "FarmDidi":        "#D68910",
    "Bombucha":        "#8E44AD",
    "Naagin":          "#C0392B",
    "Priya":           "#16A085",
    "Patanjali":       "#2ECC71",
}


def inject():
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

section[data-testid="stSidebar"] {
    background: #1A1A1A !important;
    border-right: 3px solid #C0392B;
}

/* All text in sidebar is light */
section[data-testid="stSidebar"] * { color: #F5F5F5 !important; }
section[data-testid="stSidebar"] a { color: #F5F5F5 !important; }
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stTextInput label {
    color: #999 !important;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* Sidebar buttons — dark background, light text */
section[data-testid="stSidebar"] .stButton > button {
    background: #2A2A2A !important;
    color: #E8E8E8 !important;
    border: 1px solid #3A3A3A !important;
    border-radius: 8px !important;
    font-size: 0.85rem !important;
    text-align: left !important;
    padding: 8px 12px !important;
    width: 100% !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: #333 !important;
    border-color: #C0392B !important;
    color: #fff !important;
}

/* Primary buttons in sidebar stay red */
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: #C0392B !important;
    border-color: #C0392B !important;
    color: #fff !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
    background: #A93226 !important;
}

/* Radio buttons in sidebar */
section[data-testid="stSidebar"] .stRadio label {
    color: #E8E8E8 !important;
    font-size: 0.9rem !important;
}
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 4px !important;
}

/* Input fields in sidebar */
section[data-testid="stSidebar"] input {
    background: #2A2A2A !important;
    color: #F5F5F5 !important;
    border-color: #3A3A3A !important;
}

/* Selectbox in sidebar */
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #2A2A2A !important;
    color: #F5F5F5 !important;
    border-color: #3A3A3A !important;
}

/* Dividers */
section[data-testid="stSidebar"] hr {
    border-color: #333 !important;
}

.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: var(--red);
    margin-bottom: 4px;
    line-height: 1.2;
}
.page-subtitle {
    font-size: 1rem;
    color: var(--mid);
    margin-bottom: 28px;
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
.card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.metric-card {
    background: white;
    border: 1px solid var(--border);
    border-top: 3px solid var(--red);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    margin-bottom: 16px;
}
.last-updated {
    display: inline-block;
    background: #FDF6F0;
    border: 1px solid #E8D5C8;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.8rem;
    color: #C0392B;
    font-weight: 500;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


def sidebar_brand(subtitle="Brand Hub"):
    st.markdown(f"""
<div style="padding:8px 0 20px;border-bottom:1px solid #333;margin-bottom:20px">
    <div style="font-family:'Playfair Display',serif;font-size:1.2rem;color:#C0392B;font-weight:600">
        The 40's Cookbook
    </div>
    <div style="font-size:0.75rem;color:#888;font-style:italic;margin-top:4px">by Madhu · {subtitle}</div>
</div>
""", unsafe_allow_html=True)


def author_input():
    if "author" not in st.session_state:
        st.session_state.author = ""
    name = st.text_input("Your name", value=st.session_state.author,
                         placeholder="e.g. Sarthak", key="_author_input")
    st.session_state.author = name
    return name
