"""
Process planetary_boundaries_data.xlsx into clean CSV files.
Source: BastienGauthier/planetary-flag (https://github.com/BastienGauthier/planetary-flag)
Paper: Steffen et al. 2015, Science - Planetary Boundaries
"""
import pandas as pd
import numpy as np

EXCEL_FILE = "planetary_boundaries_data.xlsx"

data_all = pd.read_excel(EXCEL_FILE, sheet_name=None)

# ── 1. Boundaries definition CSV ─────────────────────────────────────────────

df_synth = pd.read_excel(EXCEL_FILE, sheet_name="synthese", index_col=0)

# Map descriptive status info from Steffen 2015 (zones exceeded as of paper date)
# 4 boundaries exceeded: climate change, biosphere integrity (genetic), land use,
# biogeochemical flows (P & N)
STEFFEN_STATUS = {
    "1.0": "exceeded",    # Climate change - CO2 > 350 ppm
    "2.0": "within",      # Ocean acidification
    "3.0": "within",      # Ozone depletion (recovering)
    "4.0": "within",      # Atmospheric aerosols (uncertain)
    "5.1": "exceeded",    # Phosphorus cycle
    "5.2": "exceeded",    # Nitrogen cycle
    "6.1": "within",      # Blue water
    "6.2": "exceeded",    # Green water (transgressed per 2023 paper)
    "7.0": "exceeded",    # Land-system change
    "8.1": "exceeded",    # Genetic diversity
    "8.2": "within",      # Functional diversity (uncertain)
    "9.0": "exceeded",    # Novel entities (per 2022 paper)
}

def get_latest(sheet_name, value_col, year_col="year"):
    df = data_all[sheet_name]
    # Get numeric values only
    df = df[[year_col, value_col]].copy()
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
    df = df.dropna(subset=[value_col])
    if df.empty:
        return None, None
    # Prefer most recent year with numeric value
    row = df.sort_values(year_col).iloc[-1]
    return float(row[value_col]), row[year_col]

# Map to get latest values
LATEST_MAP = {
    "1.0_climate_change":       ("deseasonalized", "decimal_date"),
    "2.0_acidification":        ("value", "year"),
    "3.0_ozone":                ("value", "year"),
    "4.0_aerosol":              ("value", "year"),
    "5.1_P_cycle":              ("value", "year"),
    "5.2_N_cycle":              ("value", "year"),
    "6.1_blue_water":           ("value", "year"),
    "6.2_green_water":          ("value", "year"),
    "7.0_land_use":             ("value", "year"),
    "8.1_genetic_diversity":    ("value", "year"),
    "8.2_functional_diversity": ("value", "year"),
    "9.0_novel_entities":       ("value", "year"),
}

rows = []
for idx, row in df_synth.iterrows():
    idx_str = str(idx)
    sheet = row["sheetname"]
    value_col, date_col = LATEST_MAP[sheet]
    current_val, current_year = get_latest(sheet, value_col, date_col)

    # Round year for decimal dates
    if current_year is not None and isinstance(current_year, float):
        current_year = int(current_year)

    # Compute whether current value exceeds boundary
    if current_val is not None:
        if row["sign"] == "positive":
            exceeded = current_val > row["limit"]
        else:
            exceeded = current_val < row["limit"]
    else:
        exceeded = None

    rows.append({
        "id": idx_str,
        "name": row["name_en"],
        "unit": row["unit"],
        "boundary_value": row["limit"],
        "boundary_zone_lower": row["color_limit_min"],
        "boundary_zone_upper": row["color_limit_max"],
        "boundary_direction": row["sign"],
        "current_value": round(current_val, 4) if current_val is not None else None,
        "current_year": current_year,
        "boundary_exceeded": exceeded,
    })

df_boundaries = pd.DataFrame(rows)
df_boundaries.to_csv("boundaries.csv", index=False)
print("Written: boundaries.csv")
print(df_boundaries[["id", "name", "current_value", "current_year", "boundary_exceeded"]].to_string())

# ── 2. Temporal evolution CSV ──────────────────────────────────────────────────

# For each boundary, extract year + value series in long format.
# Use raw (non-interpolated) data points only.

TEMPORAL_SHEETS = [
    # (sheet_name, year_col, value_col, boundary_id, boundary_name, unit)
    ("1.0_climate_change",       "decimal_date", "deseasonalized", "1.0", "Climate change (CO2)", "ppm"),
    ("2.0_acidification",        "year",         "value",          "2.0", "Ocean acidification (Aragonite saturation)", "Omega"),
    ("3.0_ozone",                "year",         "value",          "3.0", "Ozone depletion (Dobson units)", "DU"),
    ("4.0_aerosol",              "year",         "value",          "4.0", "Atmospheric aerosols (AOD)", "-"),
    ("5.1_P_cycle",              "year",         "value",          "5.1", "Phosphorus cycle", "Tg/year"),
    ("5.2_N_cycle",              "year",         "value",          "5.2", "Nitrogen cycle", "Tg/year"),
    ("6.1_blue_water",           "year",         "value",          "6.1", "Freshwater change - blue water", "%"),
    ("6.2_green_water",          "year",         "value",          "6.2", "Freshwater change - green water", "%"),
    ("7.0_land_use",             "year",         "value",          "7.0", "Land-system change (forest cover)", "%"),
    ("8.1_genetic_diversity",    "year",         "value",          "8.1", "Biosphere integrity - genetic diversity (E/MSY)", "E/MSY"),
    ("8.2_functional_diversity", "year",         "value",          "8.2", "Biosphere integrity - functional diversity (%HANPP)", "%HANPP"),
    ("9.0_novel_entities",       "year",         "value",          "9.0", "Novel entities (relative to pre-industrial)", "%"),
]

temporal_rows = []
for sheet, year_col, val_col, bid, bname, unit in TEMPORAL_SHEETS:
    df = data_all[sheet][[year_col, val_col]].copy()
    df.columns = ["year", "value"]
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["value"])
    df["year"] = pd.to_numeric(df["year"], errors="coerce").round(4)
    df["boundary_id"] = bid
    df["boundary_name"] = bname
    df["unit"] = unit
    temporal_rows.append(df)

df_temporal = pd.concat(temporal_rows, ignore_index=True)
df_temporal = df_temporal[["year", "boundary_id", "boundary_name", "value", "unit"]]
df_temporal = df_temporal.sort_values(["boundary_id", "year"])
df_temporal.to_csv("boundary-evolution.csv", index=False)
print(f"\nWritten: boundary-evolution.csv ({len(df_temporal)} rows)")
print(df_temporal.groupby("boundary_id").size().rename("rows"))
