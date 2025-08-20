# Manufacturing Performance Analysis — 2024

**Contact / verification email:** 23f3000916@ds.study.iitm.ac.in

## Executive Summary
The company's average **equipment efficiency rate in 2024 is 75.03**, materially below the **industry benchmark target of 90**. Despite an encouraging improvement from **Q1 (71.48)** to **Q4 (81.77)**, the current level remains **14.97 points** short of the benchmark, contributing to increased downtime and maintenance costs. To close this gap, we recommend implementing a **predictive maintenance program** that reduces unplanned downtime and optimizes maintenance schedules.

## Key Findings
- **Trend:** Quarterly efficiency increased from **71.48 → 71.33 → 75.53 → 81.77**, indicating progress but not at the slope required to hit 90 within the next period under status quo.
- **Average 2024:** **75.03** (computed from the four quarters), **below target by 14.97**.
- **Risk:** The gap drives higher scrap/rework risk and idle capacity. Unplanned failures are likely the dominant driver of variability in Q1–Q3.

## Business Implications
- **Cost of downtime:** Lower efficiency correlates with production loss and expedited shipping or overtime costs to meet demand.
- **Asset life & spares:** Reactive maintenance increases parts wear and inventory carrying costs.
- **Capacity planning:** The current trend constrains throughput; without intervention, demand spikes may require outsourcing at higher marginal cost.

## Recommendation — Implement a Predictive Maintenance Program
**Objective:** Raise efficiency from **75.03** toward **90** by proactively detecting failure signals and scheduling maintenance during low-demand windows.

**Core components:**
1. **Data foundation:** Consolidate CMMS work orders, sensor/PLC data (vibration, temperature, current), and operator logs.
2. **Modeling:** Use anomaly detection and remaining useful life (RUL) models on key subsystems (bearings, motors, pumps).
3. **Prioritization:** Start with the top 20% assets causing 80% downtime (Pareto) and expand in waves.
4. **Process changes:** Standardize condition-based work orders and kitting of spares; integrate with production planning for planned stops.
5. **Governance:** Define KPIs—MTBF, MTTR, planned vs unplanned % maintenance, and efficiency rate (OEE component).

**Expected impact (illustrative):**
- **5–8 point** efficiency lift in 2–3 quarters by reducing unplanned downtime 25–35% and cutting changeover/repair variance.
- Additional **2–3 points** by optimizing preventive intervals and eliminating redundant PM tasks.

## Visualizations
- `trend_vs_target.png` — Quarterly trend with the industry benchmark line.
- `quarterly_bars_vs_target.png` — Quarter-by-quarter comparison against the benchmark.

## Reproduce the Analysis
1. Install Python 3.10+ and matplotlib, pandas.
2. Run:
   ```bash
   python analysis.py
   ```
   This prints the average and saves the charts in the repo root.

## Data
`equipment_efficiency_2024.csv`
```
quarter,efficiency_rate
Q1-2024,71.48
Q2-2024,71.33
Q3-2024,75.53
Q4-2024,81.77
```
**Average:** 75.03

## Pull Request Checklist
- [x] Include **analysis code**
- [x] Include **visualizations** comparing to target (90)
- [x] Include **data story** with findings, implications, and the **predictive maintenance program** solution
- [x] Include email: **23f3000916@ds.study.iitm.ac.in**