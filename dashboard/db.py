"""Supabase database layer for The 40's Cookbook dashboard."""

import os
import streamlit as st
from supabase import create_client, Client
from datetime import date, datetime, timezone
from typing import Optional

_client: Optional[Client] = None


def _get_client() -> Client:
    global _client
    if _client is None:
        url = st.secrets.get("SUPABASE_URL", "") or os.getenv("SUPABASE_URL", "")
        key = st.secrets.get("SUPABASE_KEY", "") or os.getenv("SUPABASE_KEY", "")
        if not url or not key:
            st.error(
                "**Supabase not configured.** "
                "Add `SUPABASE_URL` and `SUPABASE_KEY` to `.streamlit/secrets.toml` — "
                "see `.streamlit/secrets.toml.example` for the format."
            )
            st.stop()
        _client = create_client(url, key)
    return _client


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ─── Vendor constants ──────────────────────────────────────────────────────────

VENDOR_STAGES = [
    "Reached Out", "In Discussion", "Negotiation",
    "Sampling", "Closed Won", "Closed Lost",
]
VENDOR_CATEGORIES = [
    "Pickle Manufacturing", "Glass Jars", "Labels & Printing",
    "Packaging", "Logistics", "Other",
]


# ─── Vendors ──────────────────────────────────────────────────────────────────

def get_vendors(category: str = None, stage: str = None) -> list:
    q = _get_client().table("vendors").select("*").order("updated_at", desc=True)
    if category:
        q = q.eq("category", category)
    if stage:
        q = q.eq("stage", stage)
    return q.execute().data or []


def add_vendor(name: str, category: str, stage: str = "Reached Out",
               contact_name: str = "", contact_email: str = "",
               contact_phone: str = "", location: str = "",
               notes: str = "", created_by: str = "") -> dict:
    result = _get_client().table("vendors").insert({
        "name": name, "category": category, "stage": stage,
        "contact_name": contact_name, "contact_email": contact_email,
        "contact_phone": contact_phone, "location": location,
        "notes": notes, "created_by": created_by,
    }).execute()
    return result.data[0]


def update_vendor(vendor_id: str, **kwargs) -> None:
    kwargs["updated_at"] = _now()
    _get_client().table("vendors").update(kwargs).eq("id", vendor_id).execute()


def delete_vendor(vendor_id: str) -> None:
    _get_client().table("vendors").delete().eq("id", vendor_id).execute()


# ─── Vendor timeline ──────────────────────────────────────────────────────────

def add_vendor_update(vendor_id: str, stage_from: str, stage_to: str,
                      notes: str = "", author: str = "") -> None:
    _get_client().table("vendor_updates").insert({
        "vendor_id": vendor_id, "stage_from": stage_from,
        "stage_to": stage_to, "notes": notes, "author": author,
    }).execute()


def get_vendor_updates(vendor_id: str) -> list:
    return (_get_client()
            .table("vendor_updates")
            .select("*")
            .eq("vendor_id", vendor_id)
            .order("created_at", desc=True)
            .execute().data or [])


# ─── Costs ────────────────────────────────────────────────────────────────────

def get_costs(vendor_id: str = None) -> list:
    q = (_get_client()
         .table("vendor_costs")
         .select("*, vendors(name, category)")
         .order("created_at", desc=True))
    if vendor_id:
        q = q.eq("vendor_id", vendor_id)
    return q.execute().data or []


def add_cost(vendor_id: str, item_description: str, unit: str,
             quantity: float, price_per_unit: float, moq: str = "",
             date_quoted: date = None, notes: str = "") -> None:
    today = date.today()
    _get_client().table("vendor_costs").insert({
        "vendor_id": vendor_id,
        "item_description": item_description,
        "unit": unit,
        "quantity": float(quantity),
        "price_per_unit": float(price_per_unit),
        "moq": moq,
        "date_quoted": str(date_quoted or today),
        "notes": notes,
    }).execute()


def delete_cost(cost_id: str) -> None:
    _get_client().table("vendor_costs").delete().eq("id", cost_id).execute()


# ─── Notes ────────────────────────────────────────────────────────────────────

def get_notes(search: str = None) -> list:
    q = _get_client().table("notes").select("*").order("updated_at", desc=True)
    if search:
        q = q.ilike("title", f"%{search}%")
    return q.execute().data or []


def save_note(title: str, content: str, author: str, tags: list = None) -> None:
    _get_client().table("notes").insert({
        "title": title, "content": content,
        "author": author, "tags": tags or [],
    }).execute()


def update_note(note_id: str, title: str, content: str, tags: list = None) -> None:
    _get_client().table("notes").update({
        "title": title, "content": content,
        "tags": tags or [], "updated_at": _now(),
    }).eq("id", note_id).execute()


def delete_note(note_id: str) -> None:
    _get_client().table("notes").delete().eq("id", note_id).execute()


# ─── Competitor Prices ────────────────────────────────────────────────────────

COMPETITOR_BRANDS = [
    "Mother's Recipe", "Tops", "FarmDidi", "Bombucha",
    "Naagin", "Priya", "Patanjali",
]
COMPETITOR_PLATFORMS = [
    "Blinkit", "Zepto", "Amazon", "Flipkart",
    "BigBasket", "D2C Website", "Retail Store",
]


def get_competitor_prices(week_of: date = None, brand: str = None) -> list:
    q = (_get_client()
         .table("competitor_prices")
         .select("*")
         .order("week_of", desc=True)
         .order("brand"))
    if week_of:
        q = q.eq("week_of", str(week_of))
    if brand:
        q = q.eq("brand", brand)
    return q.execute().data or []


def save_competitor_price(brand: str, product_name: str, pack_size_g: float,
                          price_inr: float, platform: str, week_of: date,
                          source: str = "manual", verified: bool = True,
                          recorded_by: str = "", notes: str = "") -> None:
    _get_client().table("competitor_prices").insert({
        "brand": brand, "product_name": product_name,
        "pack_size_g": float(pack_size_g), "price_inr": float(price_inr),
        "platform": platform, "week_of": str(week_of),
        "source": source, "verified": verified,
        "recorded_by": recorded_by, "notes": notes,
    }).execute()


def delete_competitor_price(price_id: str) -> None:
    _get_client().table("competitor_prices").delete().eq("id", price_id).execute()


def get_latest_recorded_at() -> Optional[str]:
    result = (_get_client()
              .table("competitor_prices")
              .select("recorded_at")
              .order("recorded_at", desc=True)
              .limit(1)
              .execute())
    return result.data[0]["recorded_at"] if result.data else None
