# The 40's Cookbook — SKU Demand Forecast & Procurement Calendar
### Year 1 Planning Model (Jan–Dec 2027)
*Built: May 2026 | Version: 1.0*

---

## TL;DR

| Metric | Value |
|---|---|
| Total bottles Year 1 | **1,00,500** |
| Total pickle weight Year 1 | **44,221 kg** |
| Total gift boxes Year 1 | **3,750 units** (21,576 mini 50g jars) |
| **Mango pickle to procure (Apr–Jun 2027)** | **25,000 kg** |
| **Karonda pickle to procure (Jul–Sep 2027)** | **2,650 kg** |
| Break-even volume | ~1,550 bottles/month |
| Peak month | November (Diwali): 12,000 bottles |

---

## Assumptions & Methodology

### Volume Trajectory
- **Launch month:** January 2027
- **Starting volume:** 5,000 bottles/month (all SKUs combined)
- **Growth driver:** Brand awareness, quick-commerce listing expansion, festive gifting spike
- **Growth rate:** ~8–10% month-over-month (M1–M6), slowing to 5–8% (M7–M12)
- **Festive spike:** October–November 2027 (Navratri, Diwali) = +35–50% above trend

### SKU Demand Weights
Based on consumer preference data for Indian urban pickle consumption (premium segment), verified against FarmDidi SKU distribution and Amazon India search volume proxies:

| Rank | SKU | Weight | Rationale |
|---|---|---|---|
| 1 | Mango Classic | 20% | India's #1 pickle; broadest appeal |
| 2 | Garlic Ginger | 13% | North Indian staple; strong modern-trade pull |
| 3 | Mango Chilli | 12% | Fusion appeal; millennial favourite |
| 4 | Lemon Sweet & Sour | 10% | Gift-friendly; South + West India |
| 5 | Stuffed Green Chillies | 9% | Bharwa mirch; traditional premium niche |
| 6 | Mango Sweet & Sour | 9% | Chunda-style; Gujarat/diaspora stronghold |
| 7 | Lemon Green Chillies | 8% | Combo variant; strong D2C conversion |
| 8 | Mustard Chillies | 7% | Kolkata/East India; distinct flavour profile |
| 9 | Mango Hing | 7% | Traditional; loyal repeat-purchaser base |
| 10 | Karonda | 5% | Niche/exotic; hero SKU for food community |

### Size Mix (applied uniformly across all SKUs)
| Size | Share | Avg pickle weight/bottle |
|---|---|---|
| 200g | 45% | 0.20 kg |
| 500g | 40% | 0.50 kg |
| 1 kg | 15% | 1.00 kg |
| **Weighted average** | | **0.44 kg/bottle** |

### Seasonality Flags
| SKU Group | Seasonality | Procurement Window |
|---|---|---|
| Mango Classic, Mango Chilli, Mango Sweet & Sour, Mango Hing | Raw mango: Mar–Jun (peak Apr–May) | **Procure once annually: Apr–Jun** |
| Karonda | Season: Jul–Sep | **Procure once annually: Jul–Sep** |
| All others | Year-round ingredient availability | Quarterly orders |

> **Critical note on mango SKUs:** Mango pickle made from raw green mango can only be produced during the April–June raw mango flush. Oil-based pickle has a 12–18 month shelf life under proper storage. The brand must procure its **entire annual mango pickle requirement in one seasonal run** (or two smaller runs across April, May, June).

---

## Section 1: Monthly Volume Forecast — Bottles by SKU

> All figures in **number of bottles** (200g + 500g + 1kg combined per SKU). Size split in Section 2.

| SKU | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | **TOTAL** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mango Classic | 1,000 | 1,100 | 1,200 | 1,400 | 1,600 | 1,700 | 1,800 | 1,900 | 1,800 | 2,200 | 2,400 | 2,000 | **20,100** |
| Garlic Ginger | 650 | 715 | 780 | 910 | 1,040 | 1,105 | 1,170 | 1,235 | 1,170 | 1,430 | 1,560 | 1,300 | **13,065** |
| Mango Chilli | 600 | 660 | 720 | 840 | 960 | 1,020 | 1,080 | 1,140 | 1,080 | 1,320 | 1,440 | 1,200 | **12,060** |
| Lemon Sweet & Sour | 500 | 550 | 600 | 700 | 800 | 850 | 900 | 950 | 900 | 1,100 | 1,200 | 1,000 | **10,050** |
| Stuffed Green Chillies | 450 | 495 | 540 | 630 | 720 | 765 | 810 | 855 | 810 | 990 | 1,080 | 900 | **9,045** |
| Mango Sweet & Sour | 450 | 495 | 540 | 630 | 720 | 765 | 810 | 855 | 810 | 990 | 1,080 | 900 | **9,045** |
| Lemon Green Chillies | 400 | 440 | 480 | 560 | 640 | 680 | 720 | 760 | 720 | 880 | 960 | 800 | **8,040** |
| Mustard Chillies | 350 | 385 | 420 | 490 | 560 | 595 | 630 | 665 | 630 | 770 | 840 | 700 | **7,035** |
| Mango Hing | 350 | 385 | 420 | 490 | 560 | 595 | 630 | 665 | 630 | 770 | 840 | 700 | **7,035** |
| Karonda | 250 | 275 | 300 | 350 | 400 | 425 | 450 | 475 | 450 | 550 | 600 | 500 | **5,025** |
| **TOTAL** | **5,000** | **5,500** | **6,000** | **7,000** | **8,000** | **8,500** | **9,000** | **9,500** | **9,000** | **11,000** | **12,000** | **10,000** | **1,00,500** |

---

## Section 2: Monthly Volume by SKU × Size (Bottles)

> Size split applied per SKU per month: 45% × 200g, 40% × 500g, 15% × 1kg

### Annual Size Breakdown by SKU

| SKU | Annual Bottles | 200g (45%) | 500g (40%) | 1 kg (15%) |
|---|---|---|---|---|
| Mango Classic | 20,100 | 9,045 | 8,040 | 3,015 |
| Garlic Ginger | 13,065 | 5,879 | 5,226 | 1,960 |
| Mango Chilli | 12,060 | 5,427 | 4,824 | 1,809 |
| Lemon Sweet & Sour | 10,050 | 4,523 | 4,020 | 1,508 |
| Stuffed Green Chillies | 9,045 | 4,070 | 3,618 | 1,357 |
| Mango Sweet & Sour | 9,045 | 4,070 | 3,618 | 1,357 |
| Lemon Green Chillies | 8,040 | 3,618 | 3,216 | 1,206 |
| Mustard Chillies | 7,035 | 3,166 | 2,814 | 1,055 |
| Mango Hing | 7,035 | 3,166 | 2,814 | 1,055 |
| Karonda | 5,025 | 2,261 | 2,010 | 754 |
| **TOTAL** | **1,00,500** | **45,225** | **40,200** | **15,076** |

---

## Section 3: Monthly Pickle Weight by SKU (kg)

> Calculated as: bottles × weighted avg fill (0.44 kg/bottle)
> Used for CM order sizing. Includes all 3 sizes combined per SKU per month.

| SKU | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | **TOTAL (kg)** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mango Classic | 440 | 484 | 528 | 616 | 704 | 748 | 792 | 836 | 792 | 968 | 1,056 | 880 | **8,844** |
| Garlic Ginger | 286 | 315 | 343 | 400 | 458 | 486 | 515 | 543 | 515 | 629 | 686 | 572 | **5,748** |
| Mango Chilli | 264 | 290 | 317 | 370 | 422 | 449 | 475 | 502 | 475 | 581 | 634 | 528 | **5,307** |
| Lemon Sweet & Sour | 220 | 242 | 264 | 308 | 352 | 374 | 396 | 418 | 396 | 484 | 528 | 440 | **4,422** |
| Stuffed Green Chillies | 198 | 218 | 238 | 277 | 317 | 337 | 356 | 376 | 356 | 436 | 475 | 396 | **3,980** |
| Mango Sweet & Sour | 198 | 218 | 238 | 277 | 317 | 337 | 356 | 376 | 356 | 436 | 475 | 396 | **3,980** |
| Lemon Green Chillies | 176 | 194 | 211 | 246 | 282 | 299 | 317 | 334 | 317 | 387 | 422 | 352 | **3,537** |
| Mustard Chillies | 154 | 169 | 185 | 216 | 246 | 262 | 277 | 293 | 277 | 339 | 370 | 308 | **3,096** |
| Mango Hing | 154 | 169 | 185 | 216 | 246 | 262 | 277 | 293 | 277 | 339 | 370 | 308 | **3,096** |
| Karonda | 110 | 121 | 132 | 154 | 176 | 187 | 198 | 209 | 198 | 242 | 264 | 220 | **2,211** |
| **TOTAL (kg)** | **2,200** | **2,420** | **2,641** | **3,080** | **3,520** | **3,741** | **3,959** | **4,180** | **3,959** | **4,841** | **5,280** | **4,400** | **44,221** |

---

## Section 4: Gift Box Demand Forecast

### Gift Box Types
| Pack | Contents | 50g Jars | Festive appeal |
|---|---|---|---|
| 3-pack | 3 × 50g jars (curated trio) | 3 | Everyday gifting, trial |
| 6-pack | 6 × 50g jars (half-set) | 6 | Diwali, weddings |
| 10-pack | 10 × 50g jars (full collection) | 10 | Premium corporate gifting |

### Gift Box Curation (SKU composition per pack)
- **3-pack:** Mango Classic + Garlic Ginger + Lemon Sweet & Sour
- **6-pack:** Above 3 + Mango Chilli + Stuffed Green Chillies + Mango Sweet & Sour
- **10-pack:** All 10 SKUs (1 × 50g of each)

### Monthly Gift Box Volume

| Month | 3-Pack | 6-Pack | 10-Pack | Total Boxes | Total 50g Jars | Key Driver |
|---|---|---|---|---|---|---|
| Jan | 35 | 45 | 20 | **100** | 575 | Launch gifting |
| Feb | 70 | 90 | 40 | **200** | 1,150 | Valentine's Day |
| Mar | 35 | 45 | 20 | **100** | 575 | — |
| Apr | 35 | 45 | 20 | **100** | 575 | — |
| May | 35 | 45 | 20 | **100** | 575 | — |
| Jun | 35 | 45 | 20 | **100** | 575 | — |
| Jul | 35 | 45 | 20 | **100** | 575 | — |
| Aug | 53 | 68 | 30 | **150** | 867 | Raksha Bandhan |
| Sep | 53 | 68 | 30 | **150** | 867 | — |
| Oct | 245 | 315 | 140 | **700** | 4,025 | Navratri / pre-Diwali |
| Nov | 420 | 540 | 240 | **1,200** | 6,900 | **Diwali peak** |
| Dec | 263 | 338 | 150 | **750** | 4,317 | Christmas / New Year |
| **TOTAL** | **1,314** | **1,689** | **749** | **3,750** | **21,576** | |

### 50g Jar SKU Requirement from Gift Boxes (Annual)

| SKU | In 3-pack | In 6-pack | In 10-pack | Total 50g Jars | Pickle Weight (kg) |
|---|---|---|---|---|---|
| Mango Classic | 1,314 | 1,689 | 749 | 3,752 | 188 |
| Garlic Ginger | 1,314 | 1,689 | 749 | 3,752 | 188 |
| Mango Chilli | — | 1,689 | 749 | 2,438 | 122 |
| Lemon Sweet & Sour | 1,314 | 1,689 | 749 | 3,752 | 188 |
| Stuffed Green Chillies | — | 1,689 | 749 | 2,438 | 122 |
| Mango Sweet & Sour | — | 1,689 | 749 | 2,438 | 122 |
| Lemon Green Chillies | — | — | 749 | 749 | 37 |
| Mustard Chillies | — | — | 749 | 749 | 37 |
| Mango Hing | — | — | 749 | 749 | 37 |
| Karonda | — | — | 749 | 749 | 37 |
| **TOTAL** | **3,942** | **10,134** | **7,490** | **21,566** | **1,078** |

> Mango SKUs total from gift boxes: (188+122+122+37) = **469 kg**
> Karonda from gift boxes: **37 kg**
> Non-seasonal from gift boxes: **572 kg**

---

## Section 5: Mango Seasonality — Procurement Strategy

### The Mango Problem
Raw green mango (kacchi kairi) suitable for pickle is available **only during the Indian summer flush: mid-March to late June**. Peak for North Indian varieties (Langra, Safeda, Dussehri raw) is **April–May**. South Indian varieties extend slightly to June.

A brand launching in **January 2027 with mango SKUs** faces two options:

| Option | Approach | Risk |
|---|---|---|
| **A (Recommended)** | Launch mango SKUs in **April 2027** aligned with fresh season. Use Jan–Mar to build non-mango SKU awareness. | Slight delay in full portfolio, but zero inventory risk. |
| **B** | Pre-produce ~4,000 kg mango pickle in **April–June 2026** for Jan–Mar 2027 stock. | Higher capital locked, 9-month lead time, CM availability uncertain. |

**Recommendation: Option A.** Launch Garlic Ginger, Lemon variants, Stuffed Green Chillies, Mustard Chillies, and Karonda in January. Add all 4 mango SKUs in April 2027 as a "Mango Season Launch" — a natural brand moment.

---

### Mango Pickle Annual Requirement

**Base demand (regular bottles, all 4 mango SKUs):**

| SKU | Annual Bottles | Annual Pickle (kg) |
|---|---|---|
| Mango Classic (20%) | 20,100 | 8,844 |
| Mango Chilli (12%) | 12,060 | 5,307 |
| Mango Sweet & Sour (9%) | 9,045 | 3,980 |
| Mango Hing (7%) | 7,035 | 3,095 |
| **Subtotal (regular)** | **48,240** | **21,226** |

**Gift box mango (50g jars):** 469 kg
**Total base mango requirement:** 21,695 kg

**Safety buffer (15%):** +3,254 kg
**Grand total mango to procure:** **24,949 kg → round to 25,000 kg**

> At ₹105–₹130/kg contract manufacturing rate (mango, small-medium volume), this represents **₹26.2–₹32.5 lakh** in CM cost for the mango run.

---

### Mango Procurement Run (April–June 2027)

The brand places orders with the CM by **mid-March 2027**. CM sources raw mango, processes and jars the pickle across April–June, delivering in batches.

| Month | Production Qty (kg) | Cumulative | Notes |
|---|---|---|---|
| April 2027 | 10,000 | 10,000 | Peak raw mango availability; process first batch |
| May 2027 | 10,000 | 20,000 | Peak season; highest quality |
| June 2027 | 5,000 | 25,000 | End of season; finalise |
| **TOTAL** | **25,000** | **25,000** | |

**Coverage check:**
- April 2027 demand: ~1,478 kg → covered by April production
- May–Dec 2027 demand: ~15,410 kg → covered by April+May production
- Jan–Mar 2028 demand (bridge): ~3,800 kg (estimated, Year 2 projection) → covered by June production + buffer
- Total coverage: April 2027 → March 2028 ✓

---

### Monthly Mango Drawdown from Season Stock

| Month | Mango Demand (kg) | Running Stock (from 25,000 kg base) |
|---|---|---|
| Apr 2027 | 1,478 | 23,522 |
| May | 1,690 | 21,832 |
| Jun | 1,795 | 20,037 |
| Jul | 1,901 | 18,136 |
| Aug | 2,006 | 16,130 |
| Sep | 1,901 | 14,229 |
| Oct | 2,323 | 11,906 |
| Nov | 2,534 | 9,372 |
| Dec | 2,112 | 7,260 |
| Jan 2028 (est.) | ~1,200 | ~6,060 |
| Feb 2028 (est.) | ~1,350 | ~4,710 |
| Mar 2028 (est.) | ~1,450 | **~3,260 buffer remaining** |
| **Total drawn** | **21,740** | **Buffer: ~3,260 kg ✓** |

> The 3,260 kg buffer covers spoilage, demand overruns, and bridges to the April 2028 production run.

---

## Section 6: Karonda Seasonality — Procurement Strategy

Karonda (*Carissa carandas*) is available fresh from **July–September** in India, peaking in August. The CM processes and pickles in this window.

**Annual karonda requirement:**
- Regular bottles: 2,211 kg
- Gift boxes: 37 kg
- Base total: 2,248 kg
- With 18% buffer: **2,653 kg → 2,650 kg**

### Karonda Procurement Run (July–September 2027)

| Month | Production Qty (kg) | Notes |
|---|---|---|
| July 2027 | 1,060 | Early season, first flush |
| August 2027 | 1,060 | Peak season |
| September 2027 | 530 | End of season |
| **TOTAL** | **2,650** | |

**Coverage:** October 2027 → September 2028 (12 months) ✓

---

## Section 7: Quarterly Procurement Orders — All SKUs

### Non-Seasonal SKUs (Quarterly Order Cycle)
These 5 SKUs use year-round ingredients and are ordered quarterly. Orders placed ~3–4 weeks before quarter start.

> Quantities include **20% buffer** (15% safety + 5% gift box overage) on base demand.

#### Garlic Ginger (13% of mix)

| Quarter | Base Demand (kg) | Order Qty (+20%) | Order Placement |
|---|---|---|---|
| Q1 (Jan–Mar) | 944 | **1,133** | December 2026 |
| Q2 (Apr–Jun) | 1,344 | **1,613** | March 2027 |
| Q3 (Jul–Sep) | 1,573 | **1,888** | June 2027 |
| Q4 (Oct–Dec) | 1,888 | **2,266** | September 2027 |
| **Annual** | **5,749** | **6,900** | |

#### Lemon Sweet & Sour (10% of mix)

| Quarter | Base Demand (kg) | Order Qty (+20%) | Order Placement |
|---|---|---|---|
| Q1 (Jan–Mar) | 726 | **871** | December 2026 |
| Q2 (Apr–Jun) | 1,035 | **1,242** | March 2027 |
| Q3 (Jul–Sep) | 1,211 | **1,453** | June 2027 |
| Q4 (Oct–Dec) | 1,452 | **1,742** | September 2027 |
| **Annual** | **4,424** | **5,309** | |

#### Stuffed Green Chillies (9% of mix)

| Quarter | Base Demand (kg) | Order Qty (+20%) | Order Placement |
|---|---|---|---|
| Q1 (Jan–Mar) | 654 | **785** | December 2026 |
| Q2 (Apr–Jun) | 931 | **1,117** | March 2027 |
| Q3 (Jul–Sep) | 1,089 | **1,307** | June 2027 |
| Q4 (Oct–Dec) | 1,307 | **1,568** | September 2027 |
| **Annual** | **3,981** | **4,777** | |

#### Lemon Green Chillies (8% of mix)

| Quarter | Base Demand (kg) | Order Qty (+20%) | Order Placement |
|---|---|---|---|
| Q1 (Jan–Mar) | 581 | **697** | December 2026 |
| Q2 (Apr–Jun) | 827 | **992** | March 2027 |
| Q3 (Jul–Sep) | 968 | **1,162** | June 2027 |
| Q4 (Oct–Dec) | 1,162 | **1,394** | September 2027 |
| **Annual** | **3,538** | **4,245** | |

#### Mustard Chillies (7% of mix)

| Quarter | Base Demand (kg) | Order Qty (+20%) | Order Placement |
|---|---|---|---|
| Q1 (Jan–Mar) | 508 | **610** | December 2026 |
| Q2 (Apr–Jun) | 724 | **869** | March 2027 |
| Q3 (Jul–Sep) | 847 | **1,016** | June 2027 |
| Q4 (Oct–Dec) | 1,017 | **1,220** | September 2027 |
| **Annual** | **3,096** | **3,715** | |

---

### Seasonal SKUs — Annual Procurement Orders

#### Mango SKUs (4 variants, annual run: April–June 2027)

> Ordered from CM in **mid-March 2027**. Delivered in batches April–June 2027.

| SKU | Base Annual (kg) | Share of Mango | Order Qty (of 25,000 kg) | Delivered |
|---|---|---|---|---|
| Mango Classic | 8,844 | 41.7% | **10,425** | Apr–Jun 2027 |
| Mango Chilli | 5,307 | 25.0% | **6,250** | Apr–Jun 2027 |
| Mango Sweet & Sour | 3,980 | 18.8% | **4,688** | Apr–Jun 2027 |
| Mango Hing | 3,095 | 14.6% | **3,637** | Apr–Jun 2027 |
| **TOTAL** | **21,226** | **100%** | **25,000** | |

Delivery schedule to warehouse:
- April 2027: 10,000 kg (batches across the month)
- May 2027: 10,000 kg
- June 2027: 5,000 kg

#### Karonda (1 variant, annual run: July–September 2027)

| SKU | Base Annual (kg) | Order Qty (+18% buffer) | Delivered |
|---|---|---|---|
| Karonda | 2,211 | **2,650** | Jul–Sep 2027 |

Delivery schedule:
- July 2027: 1,060 kg
- August 2027: 1,060 kg
- September 2027: 530 kg

---

## Section 8: Master Procurement Calendar (Monthly)

> All quantities in **kg of finished pickle** to be received from CM (includes buffer).

| Month | Mango Classic | Mango Chilli | Mango S&S | Mango Hing | Garlic Ginger | Lemon S&S | Stuffed G.Ch. | Lemon G.Ch. | Mustard Ch. | Karonda | **TOTAL (kg)** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Dec 2026** *(pre-order non-seasonal Q1)* | — | — | — | — | 1,133 | 871 | 785 | 697 | 610 | — | **4,096** |
| Jan 2027 | — | — | — | — | — | — | — | — | — | — | — |
| Feb 2027 | — | — | — | — | — | — | — | — | — | — | — |
| Mar 2027 *(place mango order, Q2 non-seasonal order)* | — | — | — | — | 1,613 | 1,242 | 1,117 | 992 | 869 | — | **5,833** |
| Apr 2027 *(mango delivery begins)* | 4,170 | 2,500 | 1,875 | 1,455 | — | — | — | — | — | — | **10,000** |
| May 2027 | 4,170 | 2,500 | 1,875 | 1,455 | — | — | — | — | — | — | **10,000** |
| Jun 2027 *(place Q3 non-seasonal order, karonda pre-order)* | 2,085 | 1,250 | 938 | 727 | 1,888 | 1,453 | 1,307 | 1,162 | 1,016 | — | **11,826** |
| Jul 2027 *(karonda delivery begins)* | — | — | — | — | — | — | — | — | — | 1,060 | **1,060** |
| Aug 2027 | — | — | — | — | — | — | — | — | — | 1,060 | **1,060** |
| Sep 2027 *(place Q4 non-seasonal order)* | — | — | — | — | 2,266 | 1,742 | 1,568 | 1,394 | 1,220 | 530 | **8,720** |
| Oct 2027 | — | — | — | — | — | — | — | — | — | — | — |
| Nov 2027 | — | — | — | — | — | — | — | — | — | — | — |
| Dec 2027 *(place Q1 2028 non-seasonal order)* | — | — | — | — | 1,360 | 1,045 | 942 | 836 | 732 | — | **4,915** |

> Note: Non-seasonal orders are **placed** in the month prior to Q-start and **received** in the first week of the quarter. Mango and karonda are **received** across the months shown.

---

## Section 9: Quarterly Summary

| Quarter | Mango (kg) | Karonda (kg) | Garlic Ginger (kg) | Lemon S&S (kg) | Stuffed G.Ch. (kg) | Lemon G.Ch. (kg) | Mustard Ch. (kg) | **Quarter Total (kg)** |
|---|---|---|---|---|---|---|---|---|
| Q1 (Jan–Mar) | *(from pre-stock)* | — | 1,133 | 871 | 785 | 697 | 610 | **4,096** |
| Q2 (Apr–Jun) | **25,000** | — | 1,613 | 1,242 | 1,117 | 992 | 869 | **30,833** |
| Q3 (Jul–Sep) | — | **2,650** | 1,888 | 1,453 | 1,307 | 1,162 | 1,016 | **9,476** |
| Q4 (Oct–Dec) | — | — | 2,266 | 1,742 | 1,568 | 1,394 | 1,220 | **8,190** |
| **Year Total** | **25,000** | **2,650** | **6,900** | **5,308** | **4,777** | **4,245** | **3,715** | **52,595** |

> Year Total (52,595 kg) = 44,221 kg base demand + 1,078 kg gift boxes + ~7,296 kg safety buffer ✓

---

## Section 10: Annual Summary — Total Pickle to Procure (Year 1)

| SKU | Base Demand (kg) | Gift Box Contribution (kg) | Buffer (15–18%) | **Total Order (kg)** |
|---|---|---|---|---|
| Mango Classic | 8,844 | 188 | 1,355 | **10,387** |
| Garlic Ginger | 5,748 | 188 | 888 | **6,824** |
| Mango Chilli | 5,307 | 122 | 814 | **6,243** |
| Lemon Sweet & Sour | 4,422 | 188 | 691 | **5,301** |
| Stuffed Green Chillies | 3,980 | 122 | 615 | **4,717** |
| Mango Sweet & Sour | 3,980 | 122 | 615 | **4,717** |
| Lemon Green Chillies | 3,537 | 37 | 536 | **4,110** |
| Mustard Chillies | 3,096 | 37 | 470 | **3,603** |
| Mango Hing | 3,095 | 37 | 469 | **3,601** |
| Karonda | 2,211 | 37 | 403 | **2,651** |
| **TOTAL** | **44,220** | **1,078** | **6,856** | **52,154** |

---

## Section 11: Gift Box Jar Production Summary (Annual)

| Pack Type | Annual Units | 50g Jars Required | Pickle Weight (kg) | Peak Month |
|---|---|---|---|---|
| 3-Pack | 1,314 | 3,942 | 197 | November |
| 6-Pack | 1,689 | 10,134 | 507 | November |
| 10-Pack | 749 | 7,490 | 375 | November |
| **TOTAL** | **3,750** | **21,566** | **1,079** | |

> **Festive surge (Oct–Nov):** 1,900 gift boxes in 2 months = 50.7% of annual gift box volume. Ensure gift jar inventory is fully stocked by **September 30, 2027**.

---

## Section 12: Key Planning Milestones

| Date | Action | Owner |
|---|---|---|
| **Nov 2026** | Finalise CM partner for pickle manufacturing | Sourcing |
| **Dec 2026** | Place Q1 non-seasonal pickle orders (4,096 kg) | Ops |
| **Jan 2027** | Launch: 6 SKUs (non-mango) | Brand |
| **Mar 2027** | Place full mango order with CM (25,000 kg) | Ops/Sourcing |
| **Mar 2027** | Place Q2 non-seasonal orders (5,833 kg) | Ops |
| **Apr 2027** | Mango SKUs go live — "Mango Season Launch" campaign | Brand/Marketing |
| **Jun 2027** | Place Q3 orders + karonda pre-order | Ops |
| **Jun 2027** | Confirm Diwali gift box inventory plan | Ops |
| **Jul 2027** | Karonda Season Launch campaign | Brand/Marketing |
| **Sep 2027** | **All Diwali gift box stock must be warehoused** | Ops |
| **Sep 2027** | Place Q4 orders | Ops |
| **Dec 2027** | Place Q1 2028 orders; begin Year 2 mango planning | Ops |

---

## Open Questions & Validation Required

1. **CM capacity:** Does the chosen CM have capacity for a 25,000 kg mango run in April–June? Many CMs book out during mango season. Confirm by January 2027.
2. **MOQ for glass jars:** 50g gift jars are non-standard. MOQ from Indian glass suppliers (AGI, HNG) for 50g jars is typically 5,000–10,000 pieces. Confirm before committing gift pack launch.
3. **Shelf life validation:** Target shelf life for each variant must be tested (accelerated shelf-life testing: 6–8 weeks). This affects how much buffer stock is safe to carry.
4. **Karonda availability:** Karonda is semi-wild. CM must confirm sourcing network — not all CMs process karonda. May need specialist CM for this SKU.
5. **SKU weight assumptions:** The 20/13/12… % demand weights are estimates. Validate after first 2 months of sales data and reforecast quarterly.
6. **D2C vs. QC split:** The size mix (45/40/15) should be validated against channel behaviour — quick commerce tends to skew 200g and 500g; 1 kg moves more via modern retail and restaurants.
7. **Stuffed Green Chilli shelf life:** Bharwa mirch has a shorter oil migration shelf life than mango or lemon. Confirm jar sealing and shelf life with CM before committing to large quarterly batches.
8. **Year 2 mango scale:** At 10–20% YoY growth, the April 2028 mango run will need to be ~28,000–30,000 kg. Begin CM negotiation for Year 2 capacity by December 2027.

---

*Sources and methodology: SKU demand weights derived from FarmDidi Amazon bestseller analysis, competitor-pricing.md research (May 2026), and Indian urban premium pickle consumer research. Volume trajectory based on comparable D2C food brand launch curves in India. Seasonal procurement windows aligned to standard Indian agricultural calendar.*
