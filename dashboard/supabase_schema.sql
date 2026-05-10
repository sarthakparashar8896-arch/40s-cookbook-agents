-- The 40's Cookbook — Supabase Schema
-- Run this in your Supabase project: SQL Editor → New Query → Paste → Run

-- Extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ─── Vendors ─────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS vendors (
    id            UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name          TEXT NOT NULL,
    category      TEXT NOT NULL,
    stage         TEXT NOT NULL DEFAULT 'Reached Out',
    contact_name  TEXT DEFAULT '',
    contact_email TEXT DEFAULT '',
    contact_phone TEXT DEFAULT '',
    location      TEXT DEFAULT '',
    notes         TEXT DEFAULT '',
    created_by    TEXT DEFAULT '',
    created_at    TIMESTAMPTZ DEFAULT NOW(),
    updated_at    TIMESTAMPTZ DEFAULT NOW()
);

-- ─── Vendor stage timeline ────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS vendor_updates (
    id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    vendor_id   UUID NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
    stage_from  TEXT DEFAULT '',
    stage_to    TEXT DEFAULT '',
    notes       TEXT DEFAULT '',
    author      TEXT DEFAULT '',
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ─── Vendor costs ─────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS vendor_costs (
    id               UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    vendor_id        UUID NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
    item_description TEXT NOT NULL,
    unit             TEXT DEFAULT '',
    quantity         NUMERIC DEFAULT 1,
    price_per_unit   NUMERIC NOT NULL,
    currency         TEXT DEFAULT 'INR',
    moq              TEXT DEFAULT '',
    date_quoted      DATE DEFAULT CURRENT_DATE,
    notes            TEXT DEFAULT '',
    created_at       TIMESTAMPTZ DEFAULT NOW()
);

-- ─── Collaborative notes ──────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS notes (
    id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title      TEXT NOT NULL,
    content    TEXT DEFAULT '',
    author     TEXT DEFAULT '',
    tags       TEXT[] DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ─── Competitor prices (weekly snapshots) ─────────────────────────────────────
CREATE TABLE IF NOT EXISTS competitor_prices (
    id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    brand        TEXT NOT NULL,
    product_name TEXT DEFAULT '',
    pack_size_g  NUMERIC NOT NULL,
    price_inr    NUMERIC NOT NULL,
    platform     TEXT DEFAULT '',
    week_of      DATE NOT NULL,
    source       TEXT DEFAULT 'manual',
    verified     BOOLEAN DEFAULT TRUE,
    recorded_by  TEXT DEFAULT '',
    notes        TEXT DEFAULT '',
    recorded_at  TIMESTAMPTZ DEFAULT NOW()
);

-- ─── Indexes ──────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_vendors_stage      ON vendors(stage);
CREATE INDEX IF NOT EXISTS idx_vendors_category   ON vendors(category);
CREATE INDEX IF NOT EXISTS idx_vendor_updates_vid ON vendor_updates(vendor_id);
CREATE INDEX IF NOT EXISTS idx_vendor_costs_vid   ON vendor_costs(vendor_id);
CREATE INDEX IF NOT EXISTS idx_notes_updated      ON notes(updated_at DESC);
CREATE INDEX IF NOT EXISTS idx_prices_week        ON competitor_prices(week_of DESC);
CREATE INDEX IF NOT EXISTS idx_prices_brand       ON competitor_prices(brand);

-- ─── Row Level Security (open access — add auth later if needed) ───────────────
ALTER TABLE vendors           ENABLE ROW LEVEL SECURITY;
ALTER TABLE vendor_updates    ENABLE ROW LEVEL SECURITY;
ALTER TABLE vendor_costs      ENABLE ROW LEVEL SECURITY;
ALTER TABLE notes             ENABLE ROW LEVEL SECURITY;
ALTER TABLE competitor_prices ENABLE ROW LEVEL SECURITY;

CREATE POLICY "public_read_write" ON vendors           FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "public_read_write" ON vendor_updates    FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "public_read_write" ON vendor_costs      FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "public_read_write" ON notes             FOR ALL USING (true) WITH CHECK (true);
CREATE POLICY "public_read_write" ON competitor_prices FOR ALL USING (true) WITH CHECK (true);
