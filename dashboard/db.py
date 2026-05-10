"""SQLite database layer for The 40's Cookbook dashboard."""

import sqlite3
import uuid
import json
from contextlib import contextmanager
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).parent / "40s_cookbook.db"

# ─── Connection ────────────────────────────────────────────────────────────────

@contextmanager
def _conn():
    con = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA foreign_keys=ON")
    try:
        yield con
        con.commit()
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def _row(r) -> dict:
    return dict(r) if r else {}


def _rows(rs) -> list:
    return [dict(r) for r in rs]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _uid() -> str:
    return str(uuid.uuid4())


# ─── Schema ────────────────────────────────────────────────────────────────────

def init_db():
    with _conn() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS vendors (
            id            TEXT PRIMARY KEY,
            name          TEXT NOT NULL,
            category      TEXT NOT NULL,
            stage         TEXT NOT NULL DEFAULT 'Reached Out',
            contact_name  TEXT DEFAULT '',
            contact_email TEXT DEFAULT '',
            contact_phone TEXT DEFAULT '',
            location      TEXT DEFAULT '',
            notes         TEXT DEFAULT '',
            created_by    TEXT DEFAULT '',
            created_at    TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at    TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS vendor_updates (
            id          TEXT PRIMARY KEY,
            vendor_id   TEXT NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
            stage_from  TEXT DEFAULT '',
            stage_to    TEXT DEFAULT '',
            notes       TEXT DEFAULT '',
            author      TEXT DEFAULT '',
            created_at  TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS vendor_costs (
            id               TEXT PRIMARY KEY,
            vendor_id        TEXT NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
            item_description TEXT NOT NULL,
            unit             TEXT DEFAULT '',
            quantity         REAL DEFAULT 1,
            price_per_unit   REAL NOT NULL,
            currency         TEXT DEFAULT 'INR',
            moq              TEXT DEFAULT '',
            date_quoted      TEXT DEFAULT CURRENT_DATE,
            notes            TEXT DEFAULT '',
            created_at       TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS notes (
            id         TEXT PRIMARY KEY,
            title      TEXT NOT NULL,
            content    TEXT DEFAULT '',
            author     TEXT DEFAULT '',
            tags       TEXT DEFAULT '[]',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS competitor_prices (
            id           TEXT PRIMARY KEY,
            brand        TEXT NOT NULL,
            product_name TEXT DEFAULT '',
            pack_size_g  REAL NOT NULL,
            price_inr    REAL NOT NULL,
            platform     TEXT DEFAULT '',
            week_of      TEXT NOT NULL,
            source       TEXT DEFAULT 'manual',
            verified     INTEGER DEFAULT 1,
            recorded_by  TEXT DEFAULT '',
            notes        TEXT DEFAULT '',
            recorded_at  TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS chat_sessions (
            id            TEXT PRIMARY KEY,
            title         TEXT DEFAULT 'Untitled',
            agent_id      TEXT NOT NULL,
            author        TEXT DEFAULT '',
            created_at    TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at    TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS chat_messages (
            id         TEXT PRIMARY KEY,
            session_id TEXT NOT NULL REFERENCES chat_sessions(id) ON DELETE CASCADE,
            role       TEXT NOT NULL,
            content    TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)


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
    sql = "SELECT * FROM vendors WHERE 1=1"
    params = []
    if category:
        sql += " AND category=?"
        params.append(category)
    if stage:
        sql += " AND stage=?"
        params.append(stage)
    sql += " ORDER BY updated_at DESC"
    with _conn() as c:
        return _rows(c.execute(sql, params).fetchall())


def add_vendor(name: str, category: str, stage: str = "Reached Out",
               contact_name: str = "", contact_email: str = "",
               contact_phone: str = "", location: str = "",
               notes: str = "", created_by: str = "") -> dict:
    vid = _uid()
    now = _now()
    with _conn() as c:
        c.execute(
            """INSERT INTO vendors
               (id,name,category,stage,contact_name,contact_email,
                contact_phone,location,notes,created_by,created_at,updated_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (vid, name, category, stage, contact_name, contact_email,
             contact_phone, location, notes, created_by, now, now),
        )
    return {"id": vid, "name": name, "category": category, "stage": stage,
            "contact_name": contact_name, "contact_email": contact_email,
            "contact_phone": contact_phone, "location": location,
            "notes": notes, "created_by": created_by}


def update_vendor(vendor_id: str, **kwargs) -> None:
    kwargs["updated_at"] = _now()
    sets = ", ".join(f"{k}=?" for k in kwargs)
    with _conn() as c:
        c.execute(f"UPDATE vendors SET {sets} WHERE id=?",
                  list(kwargs.values()) + [vendor_id])


def delete_vendor(vendor_id: str) -> None:
    with _conn() as c:
        c.execute("DELETE FROM vendors WHERE id=?", (vendor_id,))


# ─── Vendor timeline ──────────────────────────────────────────────────────────

def add_vendor_update(vendor_id: str, stage_from: str, stage_to: str,
                      notes: str = "", author: str = "") -> None:
    with _conn() as c:
        c.execute(
            "INSERT INTO vendor_updates (id,vendor_id,stage_from,stage_to,notes,author,created_at) VALUES (?,?,?,?,?,?,?)",
            (_uid(), vendor_id, stage_from, stage_to, notes, author, _now()),
        )


def get_vendor_updates(vendor_id: str) -> list:
    with _conn() as c:
        return _rows(c.execute(
            "SELECT * FROM vendor_updates WHERE vendor_id=? ORDER BY created_at DESC",
            (vendor_id,),
        ).fetchall())


# ─── Costs ────────────────────────────────────────────────────────────────────

def get_costs(vendor_id: str = None) -> list:
    sql = """
        SELECT vc.*, v.name AS vendor_name, v.category AS vendor_category
        FROM vendor_costs vc
        LEFT JOIN vendors v ON v.id = vc.vendor_id
        WHERE 1=1
    """
    params = []
    if vendor_id:
        sql += " AND vc.vendor_id=?"
        params.append(vendor_id)
    sql += " ORDER BY vc.created_at DESC"
    with _conn() as c:
        rows = _rows(c.execute(sql, params).fetchall())
    for r in rows:
        r["vendors"] = {"name": r.pop("vendor_name", ""), "category": r.pop("vendor_category", "")}
    return rows


def add_cost(vendor_id: str, item_description: str, unit: str,
             quantity: float, price_per_unit: float, moq: str = "",
             date_quoted: date = None, notes: str = "") -> None:
    today = date.today() if date_quoted is None else date_quoted
    with _conn() as c:
        c.execute(
            """INSERT INTO vendor_costs
               (id,vendor_id,item_description,unit,quantity,price_per_unit,moq,date_quoted,notes,created_at)
               VALUES (?,?,?,?,?,?,?,?,?,?)""",
            (_uid(), vendor_id, item_description, unit, float(quantity),
             float(price_per_unit), moq, str(today), notes, _now()),
        )


def delete_cost(cost_id: str) -> None:
    with _conn() as c:
        c.execute("DELETE FROM vendor_costs WHERE id=?", (cost_id,))


# ─── Notes ────────────────────────────────────────────────────────────────────

def get_notes(search: str = None) -> list:
    sql = "SELECT * FROM notes WHERE 1=1"
    params = []
    if search:
        sql += " AND title LIKE ?"
        params.append(f"%{search}%")
    sql += " ORDER BY updated_at DESC"
    with _conn() as c:
        rows = _rows(c.execute(sql, params).fetchall())
    for r in rows:
        try:
            r["tags"] = json.loads(r.get("tags") or "[]")
        except Exception:
            r["tags"] = []
    return rows


def save_note(title: str, content: str, author: str, tags: list = None) -> None:
    with _conn() as c:
        c.execute(
            "INSERT INTO notes (id,title,content,author,tags,created_at,updated_at) VALUES (?,?,?,?,?,?,?)",
            (_uid(), title, content, author, json.dumps(tags or []), _now(), _now()),
        )


def update_note(note_id: str, title: str, content: str, tags: list = None) -> None:
    with _conn() as c:
        c.execute(
            "UPDATE notes SET title=?,content=?,tags=?,updated_at=? WHERE id=?",
            (title, content, json.dumps(tags or []), _now(), note_id),
        )


def delete_note(note_id: str) -> None:
    with _conn() as c:
        c.execute("DELETE FROM notes WHERE id=?", (note_id,))


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
    sql = "SELECT * FROM competitor_prices WHERE 1=1"
    params = []
    if week_of:
        sql += " AND week_of=?"
        params.append(str(week_of))
    if brand:
        sql += " AND brand=?"
        params.append(brand)
    sql += " ORDER BY week_of DESC, brand ASC"
    with _conn() as c:
        return _rows(c.execute(sql, params).fetchall())


def save_competitor_price(brand: str, product_name: str, pack_size_g: float,
                          price_inr: float, platform: str, week_of: date,
                          source: str = "manual", verified: bool = True,
                          recorded_by: str = "", notes: str = "") -> None:
    with _conn() as c:
        c.execute(
            """INSERT INTO competitor_prices
               (id,brand,product_name,pack_size_g,price_inr,platform,week_of,
                source,verified,recorded_by,notes,recorded_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (_uid(), brand, product_name, float(pack_size_g), float(price_inr),
             platform, str(week_of), source, 1 if verified else 0,
             recorded_by, notes, _now()),
        )


def delete_competitor_price(price_id: str) -> None:
    with _conn() as c:
        c.execute("DELETE FROM competitor_prices WHERE id=?", (price_id,))


def get_latest_recorded_at() -> Optional[str]:
    with _conn() as c:
        row = c.execute(
            "SELECT recorded_at FROM competitor_prices ORDER BY recorded_at DESC LIMIT 1"
        ).fetchone()
    return row["recorded_at"] if row else None


# ─── Chat sessions ────────────────────────────────────────────────────────────

def create_chat_session(agent_id: str, author: str, title: str = "") -> str:
    sid = _uid()
    now = _now()
    with _conn() as c:
        c.execute(
            "INSERT INTO chat_sessions (id,title,agent_id,author,created_at,updated_at) VALUES (?,?,?,?,?,?)",
            (sid, title or "New conversation", agent_id, author, now, now),
        )
    return sid


def rename_chat_session(session_id: str, title: str) -> None:
    with _conn() as c:
        c.execute(
            "UPDATE chat_sessions SET title=?, updated_at=? WHERE id=?",
            (title, _now(), session_id),
        )


def delete_chat_session(session_id: str) -> None:
    with _conn() as c:
        c.execute("DELETE FROM chat_sessions WHERE id=?", (session_id,))


def get_chat_sessions(agent_id: str = None, author: str = None) -> list:
    sql = """
        SELECT cs.*,
               COUNT(cm.id) AS message_count
        FROM chat_sessions cs
        LEFT JOIN chat_messages cm ON cm.session_id = cs.id
        WHERE 1=1
    """
    params = []
    if agent_id:
        sql += " AND cs.agent_id=?"
        params.append(agent_id)
    if author:
        sql += " AND cs.author=?"
        params.append(author)
    sql += " GROUP BY cs.id ORDER BY cs.updated_at DESC"
    with _conn() as c:
        return _rows(c.execute(sql, params).fetchall())


def append_chat_message(session_id: str, role: str, content: str) -> None:
    now = _now()
    with _conn() as c:
        c.execute(
            "INSERT INTO chat_messages (id,session_id,role,content,created_at) VALUES (?,?,?,?,?)",
            (_uid(), session_id, role, content, now),
        )
        c.execute(
            "UPDATE chat_sessions SET updated_at=? WHERE id=?",
            (now, session_id),
        )


def get_chat_messages(session_id: str) -> list:
    with _conn() as c:
        return _rows(c.execute(
            "SELECT * FROM chat_messages WHERE session_id=? ORDER BY created_at ASC",
            (session_id,),
        ).fetchall())


# ─── Auto-init + seed ─────────────────────────────────────────────────────────
init_db()

def _auto_seed():
    """Re-seed competitor prices if the table is empty (e.g. fresh Streamlit Cloud deploy)."""
    with _conn() as c:
        count = c.execute("SELECT COUNT(*) FROM competitor_prices").fetchone()[0]
    if count == 0:
        try:
            import importlib, sys, os
            seed_path = os.path.join(os.path.dirname(__file__), "seed_competitor_prices.py")
            if os.path.exists(seed_path):
                spec = importlib.util.spec_from_file_location("seed", seed_path)
                mod  = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                mod.seed()
        except Exception:
            pass  # seeding is best-effort

_auto_seed()
