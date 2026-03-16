# HYDE: History Database of the Global Environment

12,000 years of global population and agricultural land use. Developed by the Netherlands Environmental Assessment Agency (PBL) and Utrecht University.

## Overview

HYDE 3.3 provides estimates of world population and land use from **10,000 BCE to 2023 CE** — the entire span of human civilization. The database is built from archaeological, historical, and census sources and is widely used in climate modelling, sustainability research, and global change studies.

## Data

| File | Description | Rows |
|------|-------------|------|
| `data/population.csv` | Global population by year | 126 |
| `data/land-use.csv` | Cropland and pasture by year | 252 |

### Population

Global total world population in persons. Highlights:

| Year | Population |
|------|------------|
| 10,000 BCE | ~4.5 million |
| Year 0 (1 CE) | ~232 million |
| 1750 | ~753 million |
| 1950 | ~2.5 billion |
| 2023 | ~7.9 billion |

### Land Use

Global agricultural area in km², covering two categories:

- **Cropland** — all cultivated land (arable + permanent crops)
- **Pasture** — managed grazing land (excludes natural rangeland)

| Year | Cropland (km²) | Pasture (km²) |
|------|---------------|---------------|
| 10,000 BCE | 0 | 0 |
| Year 0 | ~1,496,000 | ~170,000 |
| 1750 | ~4,640,000 | ~3,200,000 |
| 2023 | ~16,267,000 | ~7,434,000 |

## Source Data

Raw source files (space-separated regional tables from HYDE 3.3 baseline scenario):

| File | Description |
|------|-------------|
| `popc_r.txt` | Regional population counts (persons) |
| `cropland_r.txt` | Regional cropland area (km²) |
| `pasture_r.txt` | Regional pasture area (km²) |

Run `python3 process.py` to regenerate the CSVs from these source files.

## Source

Klein Goldewijk, K., Beusen, A., Doelman, J. & Stehfest, E. (2017, updated 2024). **Anthropogenic land use estimates for the Holocene — HYDE 3.3.** Netherlands Environmental Assessment Agency (PBL) / Utrecht University. DOI: [10.24416/UU01-94FNH0](https://doi.org/10.24416/UU01-94FNH0)

HYDE project page: https://www.pbl.nl/en/hyde-history-database-of-the-global-environment

## License

CC BY 4.0. Cite the original HYDE 3.3 publication when using this dataset.
