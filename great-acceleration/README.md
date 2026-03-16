# The Great Acceleration: Trajectory of the Anthropocene

24 indicators of the Great Acceleration — the dramatic, post-1950 surge in human activity and its simultaneous impact on Earth's systems. Data compiled by the International Geosphere-Biosphere Programme (IGBP) and Stockholm Resilience Centre.

## Paper

Steffen, W., Broadgate, W., Deutsch, L., Gaffney, O., & Ludwig, C. (2015). **The trajectory of the Anthropocene: the Great Acceleration.** *The Anthropocene Review*, 2(1), 81–98. DOI: [10.1177/2053019614564785](https://journals.sagepub.com/doi/full/10.1177/2053019614564785)

## Data

| File | Description | Rows |
|------|-------------|------|
| `data/socioeconomic.csv` | 12 socioeconomic indicators | ~1,141 |
| `data/earth-system.csv` | 12 Earth system indicators | ~1,834 |

### Socioeconomic Indicators

| ID | Indicator | Unit |
|----|-----------|------|
| `population` | Population | billion |
| `real-gdp` | Real GDP | trillion USD (2005) |
| `fdi` | Foreign Direct Investment | trillion USD (current) |
| `urban-population` | Urban Population | billion |
| `primary-energy` | Primary Energy Use | exajoule (EJ) |
| `fertilizer` | Fertilizer Consumption | million tonnes |
| `large-dams` | Large Dams | thousand dams (cumulative) |
| `water-use` | Water Use | thousand km³ |
| `paper-production` | Paper Production | million tonnes |
| `transportation` | Transportation (Motor Vehicles) | million vehicles |
| `telecommunications` | Telecommunications | billion subscriptions |
| `international-tourism` | International Tourism | million arrivals |

Most socioeconomic indicators include regional breakdowns: **OECD**, **BRICS** (Brazil, Russia, India, China, South Africa), and **Rest of World**.

### Earth System Indicators

| ID | Indicator | Unit |
|----|-----------|------|
| `co2` | Carbon Dioxide | ppm |
| `n2o` | Nitrous Oxide | ppb |
| `ch4` | Methane | ppb |
| `ozone` | Stratospheric Ozone | % loss |
| `temperature` | Surface Temperature Anomaly | °C (vs. 1961–1990) |
| `ocean-acidification` | Ocean Acidification | nmol/kg (H⁺) |
| `marine-fish` | Marine Fish Capture | million tonnes |
| `shrimp-aquaculture` | Shrimp Aquaculture | million tonnes |
| `nitrogen` | Nitrogen to Coastal Zone | million tonnes/year |
| `tropical-forest` | Tropical Forest Loss | % |
| `domesticated-land` | Domesticated Land | % of total land area |
| `terrestrial-biosphere` | Terrestrial Biosphere Degradation | % decrease in mean species abundance |

## Source Data

Raw Excel file from IGBP: `great-acceleration-data.xlsx`
Run `python3 process.py` to regenerate CSVs from the Excel source.

## License

Data published under CC BY 4.0. Cite the original paper when using this dataset.
