# Bioregions 2023

185 discrete bioregions delineating Earth's terrestrial surface by ecological character, developed by One Earth. A nature-based alternative to political geography for conservation planning.

## Background

The Bioregions 2023 framework was developed by One Earth, building upon the RESOLVE Ecoregions 2017 dataset (Dinerstein et al., 2017 — 844 ecoregions). Bioregions aggregate ecologically similar ecoregions into coherent biogeographic units at a scale relevant to conservation policy and science communication.

The framework organises the world's land surface into a four-level hierarchy:

| Level | Count | Example |
|-------|-------|---------|
| Biogeographic realms | 8 | Nearctic, Palearctic, Afrotropical … |
| One Earth realms | 14 | Northern America, Western Eurasia … |
| Subrealms | 52 | Mediterranean, Amazonia, Canadian Boreal Forests … |
| Bioregions | 185 | PA18 Aegean Sea & East Mediterranean Mixed Forests |

The average bioregion covers approximately 715,000 km². Each bioregion is anchored in shared ecological and evolutionary history, reflecting natural boundaries such as mountain ranges, river basins, and climate zones.

## Data

### `data/bioregions.csv`

One row per bioregion (185 total). Columns:

| Column | Description |
|--------|-------------|
| `code` | Bioregion identifier (e.g. NA1, AT12, PA53). Two-letter realm prefix + number. |
| `name` | Full bioregion name |
| `biogeographic_realm` | One of eight traditional biogeographic realms |
| `realm` | One Earth realm (14 total) |
| `subrealm` | One Earth subrealm grouping (52 total) |

**Realm code prefixes:**

| Prefix | Biogeographic Realm | One Earth Realms |
|--------|---------------------|------------------|
| NA | Nearctic | Subarctic America, Northern America |
| NT | Neotropical | Central America, Southern America |
| PA | Palearctic | Subarctic Eurasia, Western Eurasia, Central Eurasia, Eastern Eurasia, Southern Eurasia |
| AT | Afrotropical | Afrotropics |
| IM | Indomalayan | Indomalaya |
| AU | Australasian | Australasia |
| OC | Oceanian | Oceania |
| AN | Antarctic | Antarctica |

**Bioregion counts by biogeographic realm:**

| Realm | Count |
|-------|-------|
| Palearctic | 53 |
| Nearctic | 31 |
| Neotropical | 29 |
| Afrotropical | 24 |
| Indomalayan | 18 |
| Australasian | 16 |
| Oceanian | 11 |
| Antarctic | 3 |
| **Total** | **185** |

## Source & License

Data compiled from the One Earth Bioregions 2023 framework:
- Interactive Navigator: https://www.oneearth.org/navigator/?view=bioregions
- Bioregion list: https://www.oneearth.org/bioregion-list/
- Realm pages: https://www.oneearth.org/bioregions/

Underlying ecoregion framework: Dinerstein, E. et al. (2017). An Ecoregion-Based Approach to Protecting Half the Terrestrial Realm. *BioScience*, 67(6), 534–545. https://doi.org/10.1093/biosci/bix014

**License:** CC BY-NC 4.0 — non-commercial use with attribution to One Earth.
