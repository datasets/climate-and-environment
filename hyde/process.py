"""
Process HYDE 3.3 (History Database of the Global Environment) source data
into clean long-format CSVs.

Source data: Netherlands PBL / Utrecht University
  - popc_r.txt: Regional population counts (persons)
  - cropland_r.txt: Regional cropland area (km²)
  - pasture_r.txt: Regional pasture/grazing area (km²)

Outputs:
  data/population.csv   — global population by year
  data/land-use.csv     — global cropland and pasture by year
"""

import csv
import os

SOURCE_BASE = os.path.dirname(__file__)
OUT_DIR = os.path.join(SOURCE_BASE, "data")
os.makedirs(OUT_DIR, exist_ok=True)


def parse_regional_file(path):
    """Parse a HYDE regional .txt file (space-separated, wide format).

    Returns a dict: { label -> { year -> value } }
    where label is 'Total' or an integer region code.
    """
    rows = {}
    years = None
    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            label = parts[0]
            if label == "region":
                years = [int(y) for y in parts[1:]]
            else:
                values = [float(v) for v in parts[1:]]
                rows[label] = dict(zip(years, values))
    return rows, years


def write_population_csv(pop_rows, years, out_path):
    """Write global population time series to CSV.

    Population in persons (raw HYDE values).
    """
    total = pop_rows["Total"]
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["year", "population"])
        for year in years:
            val = total.get(year)
            if val is not None:
                writer.writerow([year, round(val)])
    print(f"Written: {out_path} ({len(years)} rows)")


def write_land_use_csv(crop_rows, past_rows, years, out_path):
    """Write global cropland and pasture time series to long-format CSV.

    Areas in km².
    """
    crop_total = crop_rows["Total"]
    past_total = past_rows["Total"]
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["year", "indicator", "area_km2"])
        for year in years:
            crop_val = crop_total.get(year)
            past_val = past_total.get(year)
            if crop_val is not None:
                writer.writerow([year, "cropland", round(crop_val, 2)])
            if past_val is not None:
                writer.writerow([year, "pasture", round(past_val, 2)])
    print(f"Written: {out_path} ({len(years) * 2} rows)")


if __name__ == "__main__":
    pop_rows, years = parse_regional_file(os.path.join(SOURCE_BASE, "popc_r.txt"))
    crop_rows, _ = parse_regional_file(os.path.join(SOURCE_BASE, "cropland_r.txt"))
    past_rows, _ = parse_regional_file(os.path.join(SOURCE_BASE, "pasture_r.txt"))

    write_population_csv(pop_rows, years, os.path.join(OUT_DIR, "population.csv"))
    write_land_use_csv(
        crop_rows, past_rows, years, os.path.join(OUT_DIR, "land-use.csv")
    )

    print("Done.")
