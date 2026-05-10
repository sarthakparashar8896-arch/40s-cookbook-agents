"""Seed competitor prices from May 2026 research into the dashboard database."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import db
from datetime import date

WEEK = date(2026, 5, 4)   # Monday of research week (May 6 2026)

PRICES = [
    # ── Mother's Recipe ────────────────────────────────────────────────────────
    dict(brand="Mother's Recipe", product_name="Mixed Pickle",          pack_size_g=400,  price_inr=135,  platform="Blinkit",       week_of=WEEK, verified=True,  notes="26% off on 1kg; 400g standard price"),
    dict(brand="Mother's Recipe", product_name="Mango Pickle",          pack_size_g=1000, price_inr=190,  platform="Blinkit",       week_of=WEEK, verified=True,  notes="26% off MRP ₹260 — deep discount on large pack"),
    dict(brand="Mother's Recipe", product_name="Punjabi Mango Pickle",  pack_size_g=400,  price_inr=140,  platform="Blinkit",       week_of=WEEK, verified=True),
    dict(brand="Mother's Recipe", product_name="Mixed Pickle",          pack_size_g=400,  price_inr=130,  platform="Zepto",         week_of=WEEK, verified=True,  notes="₹15 off"),
    dict(brand="Mother's Recipe", product_name="Punjabi Mango Pickle",  pack_size_g=400,  price_inr=140,  platform="Zepto",         week_of=WEEK, verified=True),
    dict(brand="Mother's Recipe", product_name="Mixed Pickle",          pack_size_g=300,  price_inr=155,  platform="Flipkart",      week_of=WEEK, verified=True),
    dict(brand="Mother's Recipe", product_name="Mango Pickle",          pack_size_g=1000, price_inr=270,  platform="Flipkart",      week_of=WEEK, verified=True),
    dict(brand="Mother's Recipe", product_name="Mixed Pickle",          pack_size_g=300,  price_inr=135,  platform="Amazon",        week_of=WEEK, verified=True),
    dict(brand="Mother's Recipe", product_name="Mango Pickle",          pack_size_g=1000, price_inr=260,  platform="Amazon",        week_of=WEEK, verified=True),

    # ── Priya ──────────────────────────────────────────────────────────────────
    dict(brand="Priya",           product_name="Cut Mango Pickle",      pack_size_g=300,  price_inr=103,  platform="Blinkit",       week_of=WEEK, verified=True),
    dict(brand="Priya",           product_name="Mango Avakaya",         pack_size_g=300,  price_inr=103,  platform="Blinkit",       week_of=WEEK, verified=True),
    dict(brand="Priya",           product_name="Cut Mango Pickle",      pack_size_g=300,  price_inr=105,  platform="Zepto",         week_of=WEEK, verified=True),
    dict(brand="Priya",           product_name="Mango Avakaya",         pack_size_g=300,  price_inr=96,   platform="Zepto",         week_of=WEEK, verified=True,  notes="Slightly discounted"),
    dict(brand="Priya",           product_name="Mango Pickle",          pack_size_g=300,  price_inr=103,  platform="Flipkart",      week_of=WEEK, verified=True),
    dict(brand="Priya",           product_name="Cut Mango with Garlic", pack_size_g=1000, price_inr=320,  platform="Amazon",        week_of=WEEK, verified=True),

    # ── Patanjali ──────────────────────────────────────────────────────────────
    dict(brand="Patanjali",       product_name="Mango Pickle",          pack_size_g=500,  price_inr=120,  platform="D2C Website",   week_of=WEEK, verified=True,  notes="patanjaliayurved.net / Patanjali store price"),
    dict(brand="Patanjali",       product_name="Mixed Pickle",          pack_size_g=1000, price_inr=206,  platform="D2C Website",   week_of=WEEK, verified=True),
    dict(brand="Patanjali",       product_name="Lemon Pickle",          pack_size_g=500,  price_inr=120,  platform="D2C Website",   week_of=WEEK, verified=True),
    dict(brand="Patanjali",       product_name="Garlic Pickle",         pack_size_g=500,  price_inr=195,  platform="Amazon",        week_of=WEEK, verified=True),
    dict(brand="Patanjali",       product_name="Amla Pickle",           pack_size_g=1000, price_inr=220,  platform="Blinkit",       week_of=WEEK, verified=True,  notes="Partial listing — limited SKUs on Blinkit"),

    # ── FarmDidi ───────────────────────────────────────────────────────────────
    dict(brand="FarmDidi",        product_name="Homemade Mango Pickle", pack_size_g=325,  price_inr=299,  platform="Amazon",        week_of=WEEK, verified=True,  notes="MRP ₹400; no Blinkit/Zepto listing"),
    dict(brand="FarmDidi",        product_name="Punjabi Mango Pickle",  pack_size_g=325,  price_inr=299,  platform="Amazon",        week_of=WEEK, verified=True),
    dict(brand="FarmDidi",        product_name="Green Chilli Pickle",   pack_size_g=325,  price_inr=349,  platform="Amazon",        week_of=WEEK, verified=True),
    dict(brand="FarmDidi",        product_name="Homemade Mango Pickle", pack_size_g=325,  price_inr=299,  platform="D2C Website",   week_of=WEEK, verified=True,  notes="farmdidi.com — matches Amazon pricing exactly"),
    dict(brand="FarmDidi",        product_name="Mango Chunda",          pack_size_g=325,  price_inr=325,  platform="D2C Website",   week_of=WEEK, verified=True),
    dict(brand="FarmDidi",        product_name="Ker Sangri Pickle",     pack_size_g=325,  price_inr=375,  platform="D2C Website",   week_of=WEEK, verified=True,  notes="Premium regional variant"),
    dict(brand="FarmDidi",        product_name="Homemade Mango Pickle", pack_size_g=1000, price_inr=799,  platform="D2C Website",   week_of=WEEK, verified=True),

    # ── Naagin (hot sauce — premium condiment reference) ───────────────────────
    dict(brand="Naagin",          product_name="The Original Hot Sauce",pack_size_g=230,  price_inr=235,  platform="Flipkart",      week_of=WEEK, verified=True,  notes="Condiment category — not traditional achaar"),
    dict(brand="Naagin",          product_name="Smoky Bhoot",           pack_size_g=230,  price_inr=250,  platform="Flipkart",      week_of=WEEK, verified=True),
    dict(brand="Naagin",          product_name="Kantha Bomb",           pack_size_g=230,  price_inr=235,  platform="Amazon",        week_of=WEEK, verified=True),
    dict(brand="Naagin",          product_name="The Original Hot Sauce",pack_size_g=230,  price_inr=235,  platform="Amazon",        week_of=WEEK, verified=True),
]

def seed():
    # Check if already seeded
    existing = db.get_competitor_prices(week_of=WEEK)
    if existing:
        print(f"Already have {len(existing)} entries for week of {WEEK}. Skipping.")
        return

    for p in PRICES:
        db.save_competitor_price(
            brand       = p["brand"],
            product_name= p["product_name"],
            pack_size_g = p["pack_size_g"],
            price_inr   = p["price_inr"],
            platform    = p["platform"],
            week_of     = p["week_of"],
            source      = "research",
            verified    = p.get("verified", True),
            recorded_by = "Research (May 2026)",
            notes       = p.get("notes", ""),
        )
    print(f"Seeded {len(PRICES)} competitor price entries for week of {WEEK}.")

if __name__ == "__main__":
    seed()
