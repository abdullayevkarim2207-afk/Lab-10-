# Lab 11 — Ford Pro-Forma Sensitivity

All financial-statement amounts are USD millions unless noted otherwise. This
is an educational sensitivity analysis, not investment advice.

## D — the question

**Which assumptions drive Ford Motor Company's forecast and estimated value,
and what explains their effects through Ford's linked income statement,
balance sheet, FCFE, and valuation?**

## R — locked changed-input record

This record was completed before the sensitivity analysis was run.

**Timestamp:** September 29, 2026, 1:50 p.m.

| Driver | Lower | Base path, FY2026E–FY2030E | Higher | Years | Range reason |
|---|---:|---|---:|---|---|
| Revenue growth | 1.0% in each year | 2.0%, 2.5%, 2.5%, 2.5%, 2.0% | 3.5% in each year | 2026–2030 | Ford's recent revenue growth has slowed. The lower case represents weaker growth, while 3.5% represents stronger growth without being too aggressive. |
| Gross margin | 13.5% in each year | 14.5%, 14.6%, 14.7%, 14.8%, 14.8% | 15.5% in each year | 2026–2030 | Ford's margin can vary with pricing, production costs, and product mix. The cases test a reasonable lower and higher margin around the base path. |

**Locked prediction:** Changing revenue growth from the base path to 3.5% in
every year will increase operating income, FCFE, and value per share by about
5%–10%, because higher revenue should increase gross profit and operating
income while other independent assumptions remain at base. Increasing gross
margin to 15.5% in every year will also increase all three outputs. Gross
margin is expected to have the larger effect because its change applies across
Ford's large revenue base.

**Partner pre-run check:** The partner confirmed the units and confirmed that
only one independent input changes per run.

## I — implementation

Run the analysis from this folder:

```bash
python3 lab11_ford_sensitivity.py
```

The program begins every case with fresh copies of the Lab 10 revenue-growth
and gross-margin paths. It changes only the selected driver, rebuilds all five
linked forecast years, applies the unchanged FCFE valuation, checks the
balance sheet and liquidity floor, and then restores and reruns the base.

## V — validation evidence

The base-before and restored-base runs match exactly:

| FY2030E output | Base before | Restored base | Result |
|---|---:|---:|---|
| Operating income | $6,252.4 | $6,252.4 | PASS |
| FCFE | $3,987.5 | $3,987.5 | PASS |
| Value per share | $10.41 | $10.41 | PASS |

Each of the six lower/base/higher runs has a maximum balance-sheet gap of
$0.000000 million and passes the $20 billion liquidity-floor check. No run was
excluded from the comparison.

### One-at-a-time results

Changes are signed differences from the unchanged Lab 10 base. Operating
income and FCFE are FY2030E amounts.

| Driver and case | Actual input path, FY2026E–FY2030E | Operating income | Change | FCFE | Change | Value/share | Change |
|---|---|---:|---:|---:|---:|---:|---:|
| Revenue growth — lower | 1.0% / 1.0% / 1.0% / 1.0% / 1.0% | $5,865.2 | $(387.2) | $3,419.4 | $(568.1) | $8.93 | $(1.48) |
| Revenue growth — base | 2.0% / 2.5% / 2.5% / 2.5% / 2.0% | $6,252.4 | $0.0 | $3,987.5 | $0.0 | $10.41 | $0.00 |
| Revenue growth — higher | 3.5% / 3.5% / 3.5% / 3.5% / 3.5% | $6,628.0 | $375.5 | $4,634.8 | $647.2 | $12.00 | $1.60 |
| Gross margin — lower | 13.5% / 13.5% / 13.5% / 13.5% / 13.5% | $4,615.9 | $(1,636.5) | $2,697.6 | $(1,289.9) | $7.00 | $(3.41) |
| Gross margin — base | 14.5% / 14.6% / 14.7% / 14.8% / 14.8% | $6,252.4 | $0.0 | $3,987.5 | $0.0 | $10.41 | $0.00 |
| Gross margin — higher | 15.5% / 15.5% / 15.5% / 15.5% / 15.5% | $7,133.7 | $881.2 | $4,682.1 | $694.6 | $12.34 | $1.93 |

### Output spans over the selected ranges

Span is the maximum valid output minus the minimum valid output across each
driver's lower, base, and higher cases.

| Driver | Operating-income span | FCFE span | Value/share span |
|---|---:|---:|---:|
| Revenue growth | $762.7 | $1,215.3 | $3.08 |
| Gross margin | $2,517.8 | $1,984.5 | $5.33 |

Gross margin produces the larger span for all three outputs **over these
ranges**. This is a range-dependent comparison, not a universal ranking of
Ford's drivers.

### Trace of the higher-margin case

Revenue remains on its base path. The margin change recalculates gross profit,
SG&A, taxes, the balance sheet, FCFE, and valuation.

| Year | Revenue | Gross profit | SG&A | Ford Credit expense | Operating income | FCFE |
|---|---:|---:|---:|---:|---:|---:|
| 2026E | $191,012.3 | $29,606.9 | $11,842.8 | $11,269.7 | $6,494.4 | $(995.5) |
| 2027E | $195,787.6 | $30,347.1 | $12,138.8 | $11,551.5 | $6,656.8 | $3,653.1 |
| 2028E | $200,682.3 | $31,105.8 | $12,442.3 | $11,840.3 | $6,823.2 | $4,066.1 |
| 2029E | $205,699.4 | $31,883.4 | $12,753.4 | $12,136.3 | $6,993.8 | $4,443.6 |
| 2030E | $209,813.4 | $32,521.1 | $13,008.4 | $12,379.0 | $7,133.7 | $4,682.1 |

For FY2030E, the higher-margin case changes gross profit by **+$1,468.7
million**, operating income by **+$881.2 million**, and FCFE by **+$694.6
million** from base. Its value per share is **$12.34**, or **+$1.93** from
base.

### Prediction reconciliation

In the higher-revenue-growth case, operating income increases 6.0%, FCFE
increases 16.2%, and value per share increases 15.4% from base. The predicted
5%–10% range therefore contains the operating-income result but understates
the FCFE and valuation effects. The prediction that gross margin would have
the larger effect is consistent with the calculated spans.

**My independent check:** Higher gross-margin operating income minus base
operating income = $7,133.7 million − $6,252.4 million = $881.3 million. This
is $0.1 million different from the Python result of $881.2 million, which is
most likely caused by rounding because the table only shows one decimal place.

My prediction was close for operating income because higher revenue directly
increased gross profit and operating income, resulting in a 6.0% increase.
However, I underestimated the effects on FCFE and value per share because
changes in revenue flow through several linked cash-flow items, and the
valuation can amplify those changes through future cash flows and terminal
value.

## E — driver conclusion and partner evidence

Gross margin was the larger driver over my tested ranges because the change in
margin was applied to Ford's entire revenue base. When margin changed, it
directly affected gross profit, which then affected operating income, taxes,
FCFE, and value per share through the linked financial statements and
valuation.

Gross margin produced a larger span than revenue growth over these selected
ranges because changing the margin had a more direct effect on the amount of
profit Ford generated from each dollar of revenue. The tested gross-margin
range also produced a larger overall change in the model than the
revenue-growth range.

This result did not change my base valuation estimate of $10.41 per share, but
it showed me that the valuation is very sensitive to the gross-margin
assumption. My next research priority would be Ford's future gross margin
because changes in pricing, production costs, and product mix could materially
change the valuation.

**Partner question received:** Why did gross margin have a bigger effect than
revenue growth?

**My response:** Because the gross-margin change applies across Ford's entire
revenue base, so it directly changes gross profit and then flows through
operating income, FCFE, and value per share.

**Check I performed on my partner's analysis:** I checked that only one
independent input changed in each sensitivity run and that the other
assumptions stayed at their base values.

**Partner's summary of my conclusion:** Gross margin was the larger driver over
the tested ranges, and Ford's valuation is especially sensitive to changes in
margin assumptions.

## Sensitivity — learn on your own

1. **What is one-at-a-time sensitivity?** One-at-a-time sensitivity means
   changing only one independent assumption while keeping all other
   independent assumptions at their base values. This helps show how much that
   specific assumption affects the model's outputs.

2. **How can the selected input ranges affect which driver appears most
   important?** The selected ranges can affect the ranking because a wider or
   more aggressive range can create a larger output span. Therefore, a driver
   with the largest span over my tested ranges is not automatically the most
   important driver under every possible range.

3. **Why does a sensitivity table not give forecast probabilities?** A
   sensitivity table shows what happens to the model when assumptions are
   changed, but it does not show how likely each scenario is to happen. The
   lower and higher cases are test cases, not probability-weighted forecasts.

## Reflection

What surprised me most was how much gross margin changed the value per share.
I knew it would have an effect, but I did not expect it to move from $10.41 to
$12.34. That showed me that Ford's valuation is more sensitive to margin
changes than I originally thought.

## AI-use disclosure

After the locked prediction and partner pre-run check, OpenAI Codex helped add
the one-at-a-time sensitivity implementation, execute the cases, and format
the calculation evidence. The student remains responsible for independently
checking a signed difference, explaining the result, completing the partner
exchange, and submitting accurate files.

## Checkout — GitHub links

- [Lab 11 report](https://github.com/abdullayevkarim2207-afk/Lab-10-/blob/main/lab11_ford.md)
- [Lab 11 sensitivity code](https://github.com/abdullayevkarim2207-afk/Lab-10-/blob/main/lab11_ford_sensitivity.py)
- [Preserved Lab 10 model](https://github.com/abdullayevkarim2207-afk/Lab-10-/blob/main/lab10_ford_proforma.py)
