# Lazard Levelized Cost of Energy (LCOE)

Annual benchmark of the unsubsidized levelized cost of energy (\$/MWh) for utility-scale generation technologies. Published by Lazard since 2008.

## Data

`data/lcoe.csv` — LCOE low/high ranges per technology per year, from Lazard LCOE v1.0 (2008) through v17.0 (2023).

**Technologies covered:**

| ID | Name | First reported |
|----|------|---------------|
| `solar-pv-utility` | Utility-Scale Solar PV | 2008 |
| `wind-onshore` | Onshore Wind | 2008 |
| `wind-offshore` | Offshore Wind | 2015 |
| `gas-ccgt` | Gas Combined Cycle | 2008 |
| `gas-peaker` | Gas Peaker | 2015 |
| `coal` | Coal | 2008 |
| `nuclear` | Nuclear | 2008 |

**Units:** Nominal USD per MWh (unsubsidized, i.e. pre-subsidy)

## Key Finding

Solar PV costs fell ~93% from 2008 to 2023 (midpoint: ~\$398/MWh → ~\$60/MWh). Onshore wind fell ~60% over the same period. By 2020, both were cheaper than new-build coal or nuclear across nearly all scenarios.

Notable exception: the 2022 report (v16.0) showed solar costs widening to \$24–\$96/MWh due to supply chain inflation after a decade of steady decline.

## Source

Lazard's Levelized Cost of Energy Analysis, Versions 1.0–17.0 (2008–2023):
https://www.lazard.com/research-insights/lazards-levelized-cost-of-energyplus/

Data extracted from the annual PDF reports. Values represent the headline unsubsidized LCOE ranges for new-build projects in the US, reflecting typical financing, capacity factors, and fuel costs at time of publication.

Note: Lazard also publishes a separate Levelized Cost of Storage (LCOS) analysis for battery storage — not included here.

## License

Data extracted from publicly available Lazard PDF reports. Released as public domain (ODC-PDDL).
