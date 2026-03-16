# Carbon Pricing & Emissions Trading Schemes

Global carbon pricing initiatives — carbon taxes and emissions trading schemes (ETS) — with annual price data from 1990 to 2024, plus a New Zealand ETS monthly price series from 2010 to present.

## Data

### `carbon-pricing-initiatives.csv`
Overview of all 128 compliance carbon pricing instruments tracked by the World Bank: name, type (carbon tax or ETS), jurisdiction, share of emissions covered, and current price label.

### `carbon-prices.csv`
Annual carbon prices in **USD per tonne CO₂-equivalent** for each initiative, 1990–2024, in long format. Only years with a reported price are included (1,248 observations).

| Field | Description |
|---|---|
| `initiative` | Instrument name |
| `type` | Carbon tax or ETS |
| `jurisdiction` | Country or region |
| `region` | World Bank regional grouping |
| `income_group` | World Bank income classification |
| `start_year` | Year implemented |
| `year` | Observation year |
| `price_usd_per_tco2e` | Carbon price (USD/tCO₂e) |

### `nz-ets-monthly-prices.csv`
Monthly mean spot price of New Zealand Emission Units (NZUs) in NZD per tonne CO₂e, from May 2010 to present (~190 monthly observations). The NZ ETS launched in 2008; liquid secondary market pricing began around 2010.

## Sources

- **World Bank Carbon Pricing Dashboard** — [carbonpricingdashboard.worldbank.org](https://carbonpricingdashboard.worldbank.org/) — CC-BY 4.0. Data as of April 1, 2024.
- **theecanmole/nzu** — [github.com/theecanmole/nzu](https://github.com/theecanmole/nzu) — ODC Public Domain Dedication and License (PDDL). NZ ETS market data scraped from official NZ Ministry for the Environment sources.

## Processing

Run `python3 process.py` to regenerate all CSVs by downloading the latest data from the World Bank and GitHub.
