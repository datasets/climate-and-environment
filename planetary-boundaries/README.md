# Planetary Boundaries

Data on the nine planetary boundaries framework — the environmental limits within which humanity can safely operate. As of 2023, nine out of twelve tracked indicators have exceeded their boundary values.

## Background

The planetary boundary (PB) concept was introduced in 2009 by Rockström et al. and updated in 2015 by Steffen et al. in *Science*. The framework defines nine Earth-system processes that together regulate the stability and resilience of the Holocene state in which human civilisation developed. Each boundary has a quantitative threshold; crossing it risks pushing the Earth system toward a new, potentially irreversible state.

The nine boundaries are:
1. **Climate change** — atmospheric CO₂ concentration (boundary: 350 ppm; current: ~428 ppm — **exceeded**)
2. **Ocean acidification** — aragonite saturation state Ωa (boundary: 2.75; current: ~2.84 — within)
3. **Ozone depletion** — stratospheric ozone in Dobson units (boundary: 276 DU; current: ~286 DU — within, recovering)
4. **Atmospheric aerosol loading** — aerosol optical depth (boundary: 0.1; current: ~0.063 — within)
5. **Biogeochemical flows** — phosphorus (boundary: 6.2 Tg/yr; current: ~18 Tg/yr — **exceeded**) and nitrogen (boundary: 62 Tg/yr; current: ~165 Tg/yr — **exceeded**)
6. **Freshwater change** — blue water (boundary: 12.9%; current: ~22.6% — **exceeded**) and green water (boundary: 12.4%; current: ~22% — **exceeded**)
7. **Land-system change** — forest cover as % of original (boundary: 75%; current: ~59% — **exceeded**)
8. **Biosphere integrity** — genetic diversity in E/MSY (boundary: 10; current: ~150 — **exceeded**) and functional diversity in %HANPP (boundary: 10%; current: ~30% — **exceeded**)
9. **Novel entities** — synthetic chemicals, plastics, nuclear materials (boundary: 0% relative to pre-industrial; current: ~50% — **exceeded**)

## Data

### `data/boundaries.csv`

One row per planetary boundary indicator (12 sub-indicators total). Columns:

| Column | Description |
|--------|-------------|
| `id` | Indicator ID (1.0 = climate change, 5.1 = phosphorus, etc.) |
| `name` | Short English name |
| `unit` | Measurement unit |
| `boundary_value` | Safe operating space threshold (Steffen et al. 2015) |
| `boundary_zone_lower` | Lower bound of uncertainty zone |
| `boundary_zone_upper` | Upper bound of uncertainty zone (above = high risk) |
| `boundary_direction` | `positive` = higher is worse; `negative` = lower is worse |
| `current_value` | Most recent observed value (~2025) |
| `current_year` | Year of most recent observation |
| `boundary_exceeded` | Whether the current value has crossed the threshold |

### `data/boundary-evolution.csv`

Temporal evolution of each indicator from pre-industrial times to ~2025. Long format (year, boundary_id, boundary_name, value, unit).

Data density varies: the climate change indicator uses monthly Mauna Loa CO₂ data from 1958 onward (815 data points), while other indicators have sparse historical anchor points from key papers and databases.

## Sources

- **Steffen et al. 2015** — "Planetary Boundaries: Guiding human development on a changing planet", *Science* 347(6223). [DOI: 10.1126/science.1259855](https://www.science.org/doi/10.1126/science.1259855)
- **Richardson et al. 2023** — "Earth beyond six of nine planetary boundaries", *Science Advances* 9(37). [DOI: 10.1126/sciadv.adh2458](https://www.science.org/doi/10.1126/sciadv.adh2458)
- **Rockström et al. 2009** — "Planetary Boundaries: Exploring the Safe Operating Space for Humanity", *Ecology and Society*. [Link](http://www.ecologyandsociety.org/vol14/iss2/art32/)
- **NOAA Mauna Loa CO₂** — Monthly atmospheric CO₂ measurements. [Link](https://gml.noaa.gov/ccgg/trends/)
- **BastienGauthier/planetary-flag** — Temporal evolution data compiled by Bastien Gauthier. [GitHub](https://github.com/BastienGauthier/planetary-flag)

## License

Data is made available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please cite the original papers when using this data.
