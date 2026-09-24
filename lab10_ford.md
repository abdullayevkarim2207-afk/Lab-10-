# Lab 10 — Ford Motor Company (`F`)

All financial statement amounts are USD millions unless noted otherwise. This is an educational valuation, not investment advice.

## D — the question

**What are five years of Ford Motor Company's statements worth, built from assumptions I can defend?**

My company is **Ford Motor Company** and its NYSE ticker is **`F`**.

### The line that makes Ford different

Ford Credit is the line that makes Ford different. Ford has no ABG-style dealer floor-plan liability; instead, Ford Credit holds **$139.119 billion of finance receivables and operating-lease assets** and funds them with **$141.417 billion of Ford Credit debt** at December 31, 2025. Treating that debt as ordinary automaker debt while ignoring the matched finance assets would badly understate equity value, so my model grows the finance assets and links Ford Credit debt to them.

**Partner explanation:** Ford Credit makes Ford's consolidated balance sheet look much more leveraged than the industrial company alone. In my model, that means I forecast finance assets and Ford Credit debt together and keep Company debt separate.

**Partner's question:** “Why can’t Ford Credit’s debt be treated the same way as Ford’s regular automotive debt?”

**My answer:** Ford Credit borrows mainly to fund customer loans, dealer financing, and vehicle leases, so its debt is supported by corresponding finance receivables and lease assets that generate repayments. Ford's regular automotive debt funds the industrial business and must be serviced by automotive operating cash flow, so subtracting Ford Credit debt without also recognizing its matched earning assets would make Ford appear more leveraged than it is economically.

## R — history, sources, and assumptions

### Three-year history grid

Gross profit is calculated as total revenue less cost of sales because Ford does not print a subtotal called “gross profit.” PP&E means Ford's “Net property.” Shareholders' equity means equity attributable to Ford Motor Company, excluding noncontrolling interests.

| Item | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Revenue | 176,191 — [2023 10-K, p. 108](https://www.sec.gov/Archives/edgar/data/37996/000003799624000009/f-20231231.htm) | 184,992 — [2024 10-K, p. 107](https://www.sec.gov/Archives/edgar/data/37996/000003799625000013/f-20241231.htm) | 187,267 — [2025 10-K, p. 111](https://www.sec.gov/Archives/edgar/data/37996/000003799626000015/f-20251231.htm) |
| Gross profit (derived) | 25,641 = 176,191 − 150,550 — 2023 10-K, p. 108 | 26,558 = 184,992 − 158,434 — 2024 10-K, p. 107 | 12,801 = 187,267 − 174,466 — 2025 10-K, p. 111 |
| SG&A | 10,702 — 2023 10-K, p. 108 | 10,287 — 2024 10-K, p. 107 | 10,849 — 2025 10-K, p. 111 |
| Net income attributable to Ford | 4,347 — 2023 10-K, p. 108 | 5,879 — 2024 10-K, p. 107 | (8,182) — 2025 10-K, p. 111 |
| Inventory | 15,651 — 2023 10-K, p. 109 | 14,951 — 2024 10-K, p. 108 | 15,285 — 2025 10-K, p. 112 |
| PP&E / net property | 40,821 — 2023 10-K, p. 109 | 41,928 — 2024 10-K, p. 108 | 37,288 — 2025 10-K, p. 112 |
| Shareholders' equity attributable to Ford | 42,773 — 2023 10-K, p. 109 | 44,835 — 2024 10-K, p. 108 | 35,952 — 2025 10-K, p. 112 |

No history item is unresolved. The gross-profit rows are derived rather than directly reported, and that distinction is preserved.

### Student hand-check required

I must personally open and check at least two facts before submission. Suggested checks:

- [x] Opened the 2025 10-K and confirmed FY2025 revenue is **187,267** in Item 7's Company Key Metrics table.
- [x] Opened the 2024 10-K and confirmed FY2024 inventory is **14,951** in Item 7's Selected Balance Sheet Information.

Do not mark these boxes until the filing has actually been opened and checked.

### Three-year ratio table

| Measure | FY2023 | FY2024 | FY2025 | Calculation / source note |
|---|---:|---:|---:|---|
| Reported revenue growth | 11.5% | 5.0% | 1.2% | Current-year total revenue ÷ prior-year total revenue − 1; comparative income statements in the respective 10-Ks |
| Organic / same-store / comparable growth | Not disclosed | Not disclosed | Not disclosed | Ford's MD&A discusses wholesales, mix, pricing, and segment growth, but does not disclose an ABG-like consolidated organic or same-store measure |
| Gross margin | 14.6% | 14.4% | 6.8% | Derived gross profit ÷ total revenue |
| SG&A ÷ gross profit | 41.7% | 38.7% | 84.8% | SG&A ÷ derived gross profit |
| Inventory days | 37.9 | 34.4 | 32.0 | Ending inventory ÷ cost of sales × 365 |
| Depreciation ÷ PP&E | 18.8% | 18.0% | 21.0% | Depreciation and tooling amortization ÷ ending net property; cash-flow statement and balance sheet |
| Capital spending — filing | 8,236 | 8,684 | 8,815 | Investing cash outflow; 2023 10-K p. 107, 2024 10-K p. 109, 2025 10-K p. 113 |
| Capital expenditures — data provider | 8,236 | 8,684 | 8,815 | [StockAnalysis / S&P Global Market Intelligence field](https://stockanalysis.com/stocks/f/financials/cash-flow-statement/); sign displayed as an outflow |
| Effective tax rate | (9.1%) | 18.5% | 31.0% | Tax provision/(benefit) ÷ pretax income/(loss); 2023 contains a tax benefit despite positive pretax income, and 2025 is a benefit divided by a loss |

The filing and provider capital-spending figures agree in every year. Ford's 2025 gross margin and SG&A/gross-profit ratio are not a normal run rate because cost of sales includes large EV asset impairment and program-cancellation charges.

### Assumption set

Each row has exactly the requested fields: value, label, and reason. “History” means carried mechanically from the opening filing, “guidance” means management's published outlook, and “judgment” is my forecast decision.

| Value | Label | Reason |
|---|---|---|
| Revenue growth — 2.0%, 2.5%, 2.5%, 2.5%, 2.0% for 2026–2030 | Judgment | I use low-single-digit growth because reported growth slowed from 11.5% to 5.0% to 1.2%; I do not assume Ford returns to the post-shortage growth rate. |
| Gross margin — 14.5%, 14.6%, 14.7%, 14.8%, 14.8% | Judgment | I used approximately 14.5% because it is consistent with Ford’s historical margins before the unusual EV-related charges in 2025. |
| SG&A ÷ gross profit — 40.0% | Judgment | I round the undistorted 2023–2024 range of 38.7%–41.7%; using 2025's 84.8% would capitalize an impaired gross-profit denominator. |
| Ford Credit expense ÷ consolidated revenue — 5.9% | Judgment | This holds Ford Credit's expense burden close to the 2024–2025 consolidated relationship rather than dropping the finance business from the income statement. |
| Depreciation ÷ opening PP&E — 19.0% | Judgment | This is near the three-year range of 18.0%–21.0% and is applied to opening PP&E so depreciation and the PP&E roll-forward remain linked. |
| Capital spending — $10.0B, $9.8B, $10.0B, $10.2B, $10.4B | Guidance / judgment | The 2026 value is the midpoint of Ford's $9.5B–$10.5B outlook; later years stay near that level because Ford is capital intensive rather than assuming a sharp drop after guidance ends. |
| Tax rate — 21.0% | Judgment | Historical effective rates are distorted by discrete items and losses, so I use a normalized rate near the U.S. statutory rate rather than averaging (9.1%), 18.5%, and 31.0%. |
| Inventory days — 34.0 | Judgment | This is the middle FY2024 observation and sits inside the falling 37.9, 34.4, and 32.0-day history. |
| Trade receivables ÷ revenue — 8.22% | History | This is the FY2025 balance-sheet relationship, 15,398 ÷ 187,267. |
| Other assets ÷ revenue — 23.27% | History | This carries the FY2025 relationship for the aggregated remaining asset lines rather than typing an asset plug. |
| Payable days — 54.0 | History | This is FY2025 payables of 25,809 ÷ cost of sales of 174,466 × 365, consistent with Ford's discussion of roughly 45-day supplier terms plus year-end timing. |
| Other liabilities ÷ revenue — 34.19% | History | This carries the FY2025 relationship for the aggregated remaining liability lines. |
| Ford Credit finance-asset growth — 2.0% | Judgment | I grow the finance book at the first-year consolidated revenue rate; a faster assumption would require a separate origination and credit-quality case. |
| Ford Credit debt ÷ finance assets — 101.65% | History | The link is 141,417 of Ford Credit debt ÷ 139,119 of finance receivables and operating-lease assets at FY2025. |
| Company debt repayments — $2.2B in 2026, then $0.5B annually | Guidance / judgment | The first year reflects Ford's reported 2026 debt reduction; later repayments are deliberately modest so I do not assume management rapidly eliminates industrial debt. |
| Company debt interest rate — 5.7% | History | FY2025 Company interest expense of 1,254 divided by opening Company debt is approximately this rate. |
| Other income ÷ revenue — 1.0% | Judgment | Other income is volatile; 1.0% is below FY2024 and FY2025 experience and avoids forecasting another large investment gain. |
| Dividends — $2.4B annually | History / judgment | This approximates FY2025 regular common dividends and holds the cash distribution flat; supplemental dividends are not assumed. |
| Marketable securities — $15.131B | History | The model carries the FY2025 balance without assuming liquidation to fund operations. |
| Company cash floor — $20.0B | Guidance | Ford states that it targets an ongoing Company cash balance at or above $20B; the check uses cash plus marketable securities as the model's liquid-company-cash proxy. |
| Revolver limit — $18.0B | Judgment | This is a conservative rounded capacity for the model's emergency funding check; the base case draws none. |
| Cost of equity — 10.0% | Judgment | I use a round required return that reflects Ford's cyclical operating and financing risk and matches the prior Ford DCF base convention. |
| Terminal growth — 2.0% | Judgment | I keep perpetual growth below nominal economic growth and below the explicit forecast rate. |
| Shares — 3,979 million | History | This is Ford's FY2025 diluted weighted-average share count; the same count is used for model value per share. |

The latest 2026 guidance used above is from Ford's [Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/37996/000003799626000156/f-20260630.htm). It reports adjusted EBIT of $10B–$11B and adjusted free cash flow of $6B–$7B; those non-GAAP figures are reference checks, not substitutes for the model's linked GAAP-style statements.

### Opening FY2025 balance sheet used by the engine

| Assets | Value | Liabilities and equity | Value |
|---|---:|---|---:|
| Cash | 23,356 | Payables | 25,809 |
| Marketable securities | 15,131 | Other liabilities and deferred tax liabilities | 64,035 |
| Ford Credit finance receivables + operating leases | 139,119 | Company debt | 21,919 |
| Trade and other receivables | 15,398 | Ford Credit debt | 141,417 |
| Inventory | 15,285 | Revolver | 0 |
| Net PP&E | 37,288 | Total equity | 35,980 |
| Other assets | 43,583 |  |  |
| **Total assets** | **289,160** | **Total liabilities and equity** | **289,160** |

Source: Ford's [2025 Form 10-K, consolidated balance sheet, p. 112](https://www.sec.gov/Archives/edgar/data/37996/000003799626000015/f-20251231.htm). Aggregations are shown in the Python comments and reconcile to the face statements.

## I — Ford through the engine

Run:

```bash
python3 Lab-10-Ford/lab10_ford_proforma.py
```

The engine prints five linked years, a balance/check block, FCFE, and value per share. To prove that it refuses a broken statement, run:

```bash
python3 Lab-10-Ford/lab10_ford_proforma.py --break-check
```

That deliberate test changes FY2028 cash by $100 million and raises: `ValueError: FY2028E balance-sheet gap: 100.0`.

## V — checks and price

The base run produces zero balance-sheet gaps in every year and passes the $20 billion cash-pool floor in every year. It does **not** draw the revolver in any year.

| Output | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Balance-sheet gap | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash + marketable securities | 34,290.7 | 34,700.5 | 35,597.1 | 36,949.1 | 38,536.6 |
| FCFE | **(1,796.3)** | 2,809.8 | 3,296.5 | 3,752.0 | 3,987.5 |

**Negative FCFE:** FY2026E is marked negative and excluded from explicit-period value. A terminal value on a negative cash flow is not an economic number because the perpetuity formula would capitalize cash destruction rather than cash available to shareholders; this model uses a terminal value only because FY2030E FCFE is positive.

The model value is **$10.41 per share** on 3,979 million shares. Ford traded at **$12.86 at 9:55 a.m. EDT on September 24, 2026** according to the timestamped [StockAnalysis price history](https://stockanalysis.com/stocks/f/history/).

**Required comparison sentence:** The model says **$10.41**, while the market says **$12.86 on September 24, 2026**, on the model's 3,979-million-share convention; what operating result would justify the market's higher value?

This is a question, not a recommendation.

## E — fresh eyes

### Partner attack on my model

**Attack received:** “I’m not totally sure about the 10% cost of equity. Why did you pick 10%, and is there anything in Ford’s actual risk or market data that would make you change it?”

**My two-sentence answer:** I used 10% because the 10-year Treasury yield was 5.11% on September 23, 2026, and an additional risk premium is appropriate for Ford’s cyclical vehicle demand, 2025 loss, and Ford Credit exposure. I would increase the rate if Ford’s market volatility, credit spreads, leverage, or operating risk rose, and decrease it if those risks fell while cash flow became more stable.

### My attack on my partner's model

**My attack on the Tesla (`TSLA`) model:** “Your model assumes energy revenue growth of 20%, 18%, 15%, 12%, and 10%, mainly because 2025 growth was 27%. Why should one strong year remain durable, and what evidence about deployments, customer backlog, factory capacity, or pricing would make you increase or reduce those growth rates?”

**Partner's answer:** “I do not assume the 27% growth rate remains durable; I step it down each year to 10% by 2030 as the energy-storage revenue base becomes larger. I would increase the rates if Tesla reports sustained Megapack and Powerwall deployment growth, capacity expansion, healthy backlog conversion, and stable energy margins; I would reduce them if deployments slow, backlog weakens, pricing falls, or tariffs and competition pressure margins.”

## Organic growth — learn on my own

1. **What is it?** Organic growth is the change generated by operations already owned, excluding acquisitions, divestitures, and often currency effects. Same-store or comparable growth is a retailer-specific version that holds the store base broadly constant.
2. **How does Ford disclose it?** Ford does not disclose a consolidated organic, same-store, or comparable-growth percentage. Its MD&A explains changes using vehicle wholesales, mix, net pricing, exchange, and segment results, so I show reported growth and mark organic/same-store growth “not disclosed.”
3. **Why did the video carry 1.8% for ABG when reported growth was 4.7%?** The 4.7% reported figure included growth from the whole company, including acquired operations. The 1.8% measure isolated growth from stores already owned, so it was the cleaner repeatable driver for a forecast that did not separately model future acquisitions.

## Reflection

1. I would defend the **Ford Credit debt-to-finance-assets** history label the longest because both sides come from the same FY2025 balance sheet and the linkage prevents me from treating financing debt as if it funded only the automaker.
2. The number that surprised me was the **$8.182 billion FY2025 net loss** alongside **$21.282 billion of operating cash flow**; the gap shows how strongly noncash EV write-downs and financing working-capital movements affected reported earnings and cash differently.

## Before submission

- [x] Personally opened and confirmed the two filing facts above.
- [x] Reviewed every judgment reason and confirmed that the reasons reflect my view.
- [x] Completed the real partner question, received attack, two-sentence answer, and my attack on the partner.
- [x] Ran the base file and the deliberate refusal test; the broken run refused with an FY2028E $100.0 million gap.
- [ ] Commit both files and paste their GitHub links.
