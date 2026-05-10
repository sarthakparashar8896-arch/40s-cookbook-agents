"""Central data store for the 40's Cookbook brand dashboard."""

BRAND = {
    "name": "The 40's Cookbook by Madhu",
    "tagline": "Old recipe. New table.",
    "positioning": "The pickle brand built on a 100-year-old family recipe — first made by Madhu, now bottled for today.",
    "category": "Heritage Indian pickles, modern packaging",
    "founder": "Madhu",
    "origin": "Banaras",
    "est": "est. 1960",
}

BRAND_STORY = """Some recipes don't get invented. They get inherited.

The pickles in this jar were born in Banaras — a city older than most countries, where food has always been a kind of devotion. The recipe traces back over a hundred years, through Madhu's hands, through her mother's, and through generations before.

For sixty-five years, Madhu has been the keeper of this recipe. She perfected it. She taught it. She fed it to children, to grandchildren, to anyone who walked through her door hungry.

Now, for the first time, it leaves her kitchen — made at scale, but never compromised.

The 40's Cookbook isn't a new pickle. It's a hundred-year-old recipe in a bottle built for the table you set today. Because heritage doesn't have to look dusty. And good recipes, when they're really good, deserve a second life."""

MISSION = "To bring a hundred-year-old family pickle recipe to modern Indian homes, in packaging that earns its place on your table — not your back shelf."
VISION = "To make heritage Indian food the most exciting category on the shelf — proving that the oldest recipes deserve the boldest design."
PROMISE = "A pickle that tastes the way it has for a hundred years, in a bottle you'd be proud to put on the table when guests arrive."

VALUES = [
    ("Recipe first, always.", "The product is sacred. We do not modernize the food. The recipe stays exactly as Madhu perfected it."),
    ("Design as respect.", "Beautiful packaging is not decoration. It is how we honor a 100-year-old recipe and give it a place on the modern table."),
    ("Made for today's table.", "Built for how customers actually eat, entertain, and live now. Not aimed at the back shelf — aimed at the centerpiece."),
    ("Heritage without nostalgia.", "We do not dwell in the past. We bring the past forward. No sepia tones, no rural-kitchen tropes. Heritage made current."),
]

FLAVORS = [
    {"flavor": "Mango", "name": "Golden Hour", "rationale": "Warm, golden, the foundational pickle. Most Indian households recognize first."},
    {"flavor": "Lemon", "name": "Zest", "rationale": "Sharp, awakening, cuts through. One-word punchy."},
    {"flavor": "Chili", "name": "Ember", "rationale": "Controlled intensity. Heat that has been mastered, not raw."},
    {"flavor": "Mixed", "name": "Alchemy", "rationale": "Where all of Madhu's skills converge into one jar."},
]

AUDIENCE = {
    "Age": "26 and above. Sweet spot 28–40.",
    "Geography": "Gurgaon, Delhi NCR, Mumbai (Tier 1). Spillover: Bangalore, Hyderabad, Pune.",
    "Profession": "Corporate professionals or upper-middle-class households.",
    "Income": "Upper-middle class. Disposable income for premium grocery.",
    "Shopping": "Modern Bazaar, Nature's Basket, Le Marché. Heavy Blinkit/Zepto/Instamart users.",
    "Mindset": "Aesthetic-driven. Entertain at home. Will pay for design + provenance.",
    "Buying intent": "Self-consumption AND gifting. Premium gifting is a key use case.",
}

import pandas as pd

# ── Pricing data ──────────────────────────────────────────────────────────────

PRICE_PER_100G = pd.DataFrame([
    {"Brand": "Mother's Recipe", "Variant": "Mango Pickle 1kg", "Pack Size": "1kg", "Price (₹)": 190, "₹/100g": 19, "Tier": "Budget", "Platform": "Blinkit"},
    {"Brand": "Patanjali", "Variant": "Mixed Pickle 1kg", "Pack Size": "1kg", "Price (₹)": 206, "₹/100g": 21, "Tier": "Budget", "Platform": "Official Site"},
    {"Brand": "Patanjali", "Variant": "Mango Pickle 500g", "Pack Size": "500g", "Price (₹)": 120, "₹/100g": 24, "Tier": "Budget", "Platform": "Official Site"},
    {"Brand": "Priya", "Variant": "Cut Mango 1kg", "Pack Size": "1kg", "Price (₹)": 320, "₹/100g": 32, "Tier": "Mainstream", "Platform": "Amazon"},
    {"Brand": "Mother's Recipe", "Variant": "Mixed Pickle 400g", "Pack Size": "400g", "Price (₹)": 135, "₹/100g": 34, "Tier": "Mainstream", "Platform": "Blinkit"},
    {"Brand": "Priya", "Variant": "Mango Pickle 300g", "Pack Size": "300g", "Price (₹)": 103, "₹/100g": 34, "Tier": "Mainstream", "Platform": "Blinkit"},
    {"Brand": "Mother's Recipe", "Variant": "Mixed Pickle 300g", "Pack Size": "300g", "Price (₹)": 155, "₹/100g": 52, "Tier": "Mainstream", "Platform": "Flipkart"},
    {"Brand": "FarmDidi", "Variant": "Mango Pickle 325g", "Pack Size": "325g", "Price (₹)": 299, "₹/100g": 92, "Tier": "Premium", "Platform": "D2C / Amazon"},
    {"Brand": "FarmDidi", "Variant": "Avakaya Pickle 325g", "Pack Size": "325g", "Price (₹)": 325, "₹/100g": 100, "Tier": "Premium", "Platform": "D2C / Amazon"},
    {"Brand": "Naagin", "Variant": "Original Hot Sauce 230g", "Pack Size": "230g", "Price (₹)": 235, "₹/100g": 102, "Tier": "Premium", "Platform": "Flipkart"},
    {"Brand": "FarmDidi", "Variant": "Garlic Pickle 325g", "Pack Size": "325g", "Price (₹)": 349, "₹/100g": 107, "Tier": "Premium", "Platform": "D2C / Amazon"},
    {"Brand": "FarmDidi", "Variant": "Ker Sangri Pickle 325g", "Pack Size": "325g", "Price (₹)": 375, "₹/100g": 115, "Tier": "Premium", "Platform": "D2C / Amazon"},
])

PLATFORM_PRESENCE = pd.DataFrame([
    {"Brand": "Mother's Recipe", "Blinkit": "✅", "Zepto": "✅", "Flipkart": "✅", "Amazon": "✅", "D2C": "✅", "Swiggy": "✅"},
    {"Brand": "Priya",           "Blinkit": "✅", "Zepto": "✅", "Flipkart": "✅", "Amazon": "✅", "D2C": "❌", "Swiggy": "❌"},
    {"Brand": "Patanjali",       "Blinkit": "⚠️", "Zepto": "❌", "Flipkart": "✅", "Amazon": "✅", "D2C": "✅", "Swiggy": "❌"},
    {"Brand": "FarmDidi",        "Blinkit": "❌", "Zepto": "❌", "Flipkart": "✅", "Amazon": "✅", "D2C": "✅", "Swiggy": "❌"},
    {"Brand": "Naagin",          "Blinkit": "⚠️", "Zepto": "⚠️", "Flipkart": "✅", "Amazon": "✅", "D2C": "✅", "Swiggy": "✅"},
    {"Brand": "The 40's Cookbook","Blinkit": "🎯", "Zepto": "🎯", "Flipkart": "🎯", "Amazon": "🎯", "D2C": "🎯", "Swiggy": "🎯"},
])

COMPETITORS = [
    {
        "brand": "Mother's Recipe",
        "positioning": "Mass-market / mainstream",
        "entry_price": "₹85",
        "price_per_100g": "₹19–₹52",
        "strength": "Distribution, trust, scale",
        "weakness": "Visually dated. No design appeal for Gen Z.",
        "platforms": "All platforms",
        "quick_commerce": True,
    },
    {
        "brand": "Priya",
        "positioning": "Value / South Indian",
        "entry_price": "₹96",
        "price_per_100g": "₹32–₹35",
        "strength": "Authenticity, regional depth",
        "weakness": "Plastic jars, dated branding.",
        "platforms": "All platforms",
        "quick_commerce": True,
    },
    {
        "brand": "Patanjali",
        "positioning": "Value / mass",
        "entry_price": "₹75",
        "price_per_100g": "₹19–₹37",
        "strength": "Price, reach, own store network",
        "weakness": "Zero design consideration.",
        "platforms": "Amazon, Flipkart, own stores",
        "quick_commerce": False,
    },
    {
        "brand": "FarmDidi",
        "positioning": "Premium / artisan D2C",
        "entry_price": "₹299",
        "price_per_100g": "₹79–₹116",
        "strength": "Amazon #1 pickle. Clean label. Shark Tank.",
        "weakness": "No quick-commerce. No physical retail.",
        "platforms": "Amazon, Flipkart, D2C",
        "quick_commerce": False,
    },
    {
        "brand": "Naagin",
        "positioning": "Premium / modern hot sauce",
        "entry_price": "₹235",
        "price_per_100g": "₹94–₹109",
        "strength": "Bold design, Gen Z love",
        "weakness": "Hot sauce, not achaar. Different category.",
        "platforms": "Amazon, Flipkart, Swiggy",
        "quick_commerce": False,
    },
]

LEARNINGS = [
    {
        "num": "01",
        "title": "Pricing White Space at Mid-Premium",
        "icon": "💰",
        "insight": "No brand occupies ₹60–₹75/100g. Budget clusters at ₹19–₹25, mainstream at ₹30–₹55, premium at ₹90–₹120. The gap is wide open.",
        "implication": "Price entry pack at ₹180–₹225 for 300g (₹60–₹75/100g) to own the accessible premium tier with zero direct competition.",
        "urgency": "High",
    },
    {
        "num": "02",
        "title": "Quick Commerce Gap Among Premium Brands",
        "icon": "⚡",
        "insight": "FarmDidi is absent from Blinkit and Zepto (May 2026). Naagin only on Swiggy Instamart. Premium pickle is invisible on quick-commerce.",
        "implication": "Be the first premium heritage pickle natively on Blinkit and Zepto. This distribution advantage must be captured before FarmDidi moves.",
        "urgency": "High",
    },
    {
        "num": "03",
        "title": "Price Integrity = Brand Integrity",
        "icon": "🎯",
        "insight": "FarmDidi holds identical pricing on D2C and Amazon (₹299 for 325g). Mother's Recipe shows wide variance. Price consistency signals premium.",
        "implication": "Set a firm MAP policy from launch. Never discount on any channel — consistent pricing across D2C, Amazon, and quick-commerce is non-negotiable.",
        "urgency": "Medium",
    },
    {
        "num": "04",
        "title": "Curation Over Breadth at Launch",
        "icon": "✂️",
        "insight": "Mother's Recipe has the widest portfolio. FarmDidi has 6 mango SKUs alone. Neither brand won through variety — flagship SKUs drove initial awareness.",
        "implication": "Launch with 4 curated named flavors (Golden Hour, Zest, Ember, Alchemy). Depth comes later. The story sells the first jar.",
        "urgency": "Medium",
    },
    {
        "num": "05",
        "title": "Gifting Is an Underserved Occasion",
        "icon": "🎁",
        "insight": "FarmDidi trial packs (4×75g at ₹349; 8×75g at ₹599) serve as gifting SKUs. Premium pickle as a gift is culturally resonant but underdeveloped.",
        "implication": "Design a multi-flavor gift box SKU from the start. Target Diwali 2026 as the first gifting moment. Gifting puts product in new households.",
        "urgency": "Medium",
    },
    {
        "num": "06",
        "title": "Deep Discounting Destroys Premium Signals",
        "icon": "🚫",
        "insight": "Mother's Recipe discounts 1kg packs up to 26% on Blinkit. This works for a mass brand. For a premium entrant, it signals the price wasn't justified.",
        "implication": "No promotions in Year 1 beyond gifting bundles. Let the product and story sell at full price.",
        "urgency": "Low",
    },
]

GTM_PHASES = [
    {"Month": "Month 1", "Phase": "Foundation", "Actions": "Lock brand identity, packaging, manufacturer. Launch website.", "Status": "🔲 Planned"},
    {"Month": "Month 2", "Phase": "Credibility Build", "Actions": "Place in 5–10 restaurants + 5–10 retail stores. Build proof points.", "Status": "🔲 Planned"},
    {"Month": "Month 3", "Phase": "Story Amplification", "Actions": "Influencer + chef content. Founder story. Activate Banaras angle.", "Status": "🔲 Planned"},
    {"Month": "Month 4", "Phase": "Scale", "Actions": "D2C live. Blinkit + Zepto listings. Capture social demand.", "Status": "🔲 Planned"},
    {"Month": "Ongoing", "Phase": "Hyperlocal", "Actions": "WhatsApp / MyGate in Gurgaon + Delhi NCR societies from Day 1.", "Status": "🔲 Planned"},
]

OPEN_QUESTIONS = [
    "Confirm the actual year Madhu started making pickles — est. 1960 is a placeholder.",
    "Confirm Madhu's full name and family details for packaging / About page.",
    "Decide flavor lineup at launch — all four, or stagger?",
    "Set price-point band: recommend ₹180–₹225 for 300g (₹60–₹75/100g).",
    "Bottle size SKU strategy — single size at launch, or multiple?",
]

NEXT_STEPS = [
    "Visual identity: Designer to produce final logo, color, type, packaging.",
    "Brand voice: Full voice document — do's, don'ts, sample copy.",
    "Supplier sourcing: Contract manufacturers, glass suppliers, label printers.",
    "Quick-commerce listings: Get on Blinkit and Zepto before FarmDidi does.",
    "Gifting SKU design: Multi-flavor sampler box for Diwali 2026.",
]
