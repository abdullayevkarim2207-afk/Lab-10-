"""Lab 11 one-at-a-time sensitivity analysis for the Ford pro forma.

Each run starts with a fresh copy of the Lab 10 independent assumptions. Amounts
are USD millions except per-share data; rates are stored as decimals.
"""

from __future__ import annotations

from dataclasses import dataclass

import lab10_ford_proforma as model


YEARS = tuple(model.YEARS)
REVENUE_CASES = {
    "Lower": {year: 0.010 for year in YEARS},
    "Base": model.REVENUE_GROWTH.copy(),
    "Higher": {year: 0.035 for year in YEARS},
}
MARGIN_CASES = {
    "Lower": {year: 0.135 for year in YEARS},
    "Base": model.GROSS_MARGIN.copy(),
    "Higher": {year: 0.155 for year in YEARS},
}


@dataclass(frozen=True)
class CaseResult:
    driver: str
    case: str
    input_path: dict[int, float]
    forecasts: list[dict[str, float]]
    operating_income: float
    fcfe: float
    value_per_share: float
    max_balance_gap: float
    cash_floor_pass: bool


def calculate_value_per_share(forecasts: list[dict[str, float]]) -> float:
    """Apply the unchanged Lab 10 FCFE valuation convention without printing."""
    explicit_value = sum(
        row["fcfe"] / (1.0 + model.COST_OF_EQUITY) ** index
        for index, row in enumerate(forecasts, start=1)
        if row["fcfe"] > 0.0
    )
    terminal_value = 0.0
    if forecasts[-1]["fcfe"] > 0.0:
        terminal_value = (
            forecasts[-1]["fcfe"]
            * (1.0 + model.TERMINAL_GROWTH)
            / (model.COST_OF_EQUITY - model.TERMINAL_GROWTH)
        )
    equity_value = explicit_value + terminal_value / (
        1.0 + model.COST_OF_EQUITY
    ) ** len(forecasts)
    return equity_value / model.SHARES_OUTSTANDING


def run_case(driver: str, case: str, input_path: dict[int, float]) -> CaseResult:
    """Run one case from fresh base assumptions and retain validation evidence."""
    revenue_growth = model.REVENUE_GROWTH.copy()
    gross_margin = model.GROSS_MARGIN.copy()
    if driver == "Revenue growth":
        revenue_growth = input_path.copy()
    elif driver == "Gross margin":
        gross_margin = input_path.copy()
    else:
        raise ValueError(f"Unknown driver: {driver}")

    forecasts = model.build_projection(
        revenue_growth=revenue_growth,
        gross_margin=gross_margin,
    )
    model.assert_balanced(forecasts)
    max_gap = max(abs(row["balance_gap"]) for row in forecasts)
    floor_pass = all(
        row["cash"] + row["marketable_securities"] >= model.COMPANY_CASH_FLOOR
        for row in forecasts
    )
    final = forecasts[-1]
    return CaseResult(
        driver=driver,
        case=case,
        input_path=input_path.copy(),
        forecasts=forecasts,
        operating_income=final["operating_income"],
        fcfe=final["fcfe"],
        value_per_share=calculate_value_per_share(forecasts),
        max_balance_gap=max_gap,
        cash_floor_pass=floor_pass,
    )


def format_path(path: dict[int, float]) -> str:
    return "/".join(f"{100.0 * path[year]:.1f}%" for year in YEARS)


def print_results(results: list[CaseResult], base: CaseResult) -> None:
    print("\nSENSITIVITY RESULTS — FINAL YEAR FY2030E")
    print("Amounts are USD millions except value per share.")
    header = (
        f"{'Driver / case':<29}{'Input path 2026-2030':<32}"
        f"{'Operating income':>18}{'Change':>13}{'FCFE':>13}"
        f"{'Change':>13}{'Value/share':>14}{'Change':>11}"
    )
    print(header)
    print("-" * len(header))
    for result in results:
        print(
            f"{result.driver + ' — ' + result.case:<29}"
            f"{format_path(result.input_path):<32}"
            f"{result.operating_income:18,.1f}"
            f"{result.operating_income - base.operating_income:13,.1f}"
            f"{result.fcfe:13,.1f}"
            f"{result.fcfe - base.fcfe:13,.1f}"
            f"{result.value_per_share:14.2f}"
            f"{result.value_per_share - base.value_per_share:11.2f}"
        )

    print("\nOUTPUT SPANS (maximum minus minimum across lower/base/higher)")
    print(
        f"{'Driver':<20}{'Operating income':>20}{'FCFE':>15}"
        f"{'Value/share':>16}"
    )
    for driver in ("Revenue growth", "Gross margin"):
        group = [result for result in results if result.driver == driver]
        print(
            f"{driver:<20}"
            f"{max(x.operating_income for x in group) - min(x.operating_income for x in group):20,.1f}"
            f"{max(x.fcfe for x in group) - min(x.fcfe for x in group):15,.1f}"
            f"{max(x.value_per_share for x in group) - min(x.value_per_share for x in group):16.2f}"
        )

    print("\nACCOUNTING AND LIQUIDITY CHECKS")
    print(f"{'Driver / case':<29}{'Maximum balance gap':>23}{'Cash floor':>15}")
    for result in results:
        print(
            f"{result.driver + ' — ' + result.case:<29}"
            f"{result.max_balance_gap:23.6f}"
            f"{('PASS' if result.cash_floor_pass else 'FAIL'):>15}"
        )


def print_trace(base: CaseResult, selected: CaseResult) -> None:
    print("\nTRACE — HIGHER GROSS MARGIN VERSUS BASE")
    print(
        f"{'Year':<8}{'Revenue':>14}{'Gross profit':>16}{'SG&A':>14}"
        f"{'Credit expense':>17}{'Operating income':>19}{'FCFE':>14}"
    )
    for base_row, changed_row in zip(base.forecasts, selected.forecasts):
        print(
            f"{int(changed_row['year']):<8}"
            f"{changed_row['revenue']:14,.1f}"
            f"{changed_row['gross_profit']:16,.1f}"
            f"{changed_row['sga']:14,.1f}"
            f"{changed_row['ford_credit_expense']:17,.1f}"
            f"{changed_row['operating_income']:19,.1f}"
            f"{changed_row['fcfe']:14,.1f}"
        )
        if changed_row["year"] == 2030.0:
            print(
                "FY2030E signed differences from base: "
                f"gross profit {changed_row['gross_profit'] - base_row['gross_profit']:+,.1f}; "
                f"operating income {changed_row['operating_income'] - base_row['operating_income']:+,.1f}; "
                f"FCFE {changed_row['fcfe'] - base_row['fcfe']:+,.1f}."
            )


def main() -> None:
    base_before = run_case("Revenue growth", "Base", REVENUE_CASES["Base"])
    results = [
        run_case("Revenue growth", case, path)
        for case, path in REVENUE_CASES.items()
    ] + [
        run_case("Gross margin", case, path)
        for case, path in MARGIN_CASES.items()
    ]
    base_after = run_case("Revenue growth", "Base", REVENUE_CASES["Base"])

    print("LAB 11 — FORD ONE-AT-A-TIME SENSITIVITY")
    print(
        "Base-before/base-after check: "
        f"operating income {base_before.operating_income:,.1f} / "
        f"{base_after.operating_income:,.1f}; "
        f"FCFE {base_before.fcfe:,.1f} / {base_after.fcfe:,.1f}; "
        f"value/share ${base_before.value_per_share:.2f} / "
        f"${base_after.value_per_share:.2f} — "
        f"{'PASS' if base_before == base_after else 'FAIL'}"
    )
    print_results(results, base_before)
    higher_margin = next(
        result
        for result in results
        if result.driver == "Gross margin" and result.case == "Higher"
    )
    print_trace(base_before, higher_margin)


if __name__ == "__main__":
    main()
