from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Any, Tuple

import pandas as pd

UNIT_RE = re.compile(r"^[0-9]{3}$")
EQUIP_RE = re.compile(r"^[0-9]{3}[A-Z]-[0-9]{4}$")  # example: 100A-0001
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")

ALLOWED_RISK = {"Low", "Medium", "High"}
NUMERIC_FIELDS = [
    "Design Pressure (KPag)",
    "Design Temperature (deg. C)",
    "Max STCR (MPY)",
    "Max LTCR (MPY)",
]

def _text(value: Any) -> str:
    """Cell as stripped text; blank cells are "", not "nan"."""
    return "" if pd.isna(value) else str(value).strip()

@dataclass
class ValidationIssue:
    row_index: int
    field: str
    severity: str  # error | warn
    message: str
    value: Any

def validate_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[ValidationIssue]]:
    issues: List[ValidationIssue] = []

    required = [
        "Unit ID",
        "Circuit /Equipment Tag",
        "Equipment ID (Asset ID)",
        "Damage Mechanism as per Corrosion Study",
    ]
    for col in required:
        if col not in df.columns:
            issues.append(ValidationIssue(-1, col, "error", "Missing required column", None))

    if any(i.severity == "error" and i.row_index == -1 for i in issues):
        return df, issues

    for idx, row in df.iterrows():
        for col in required:
            if not _text(row.get(col)):
                issues.append(ValidationIssue(idx, col, "error", f"{col} is required", None))

        unit = _text(row.get("Unit ID"))
        if unit and not UNIT_RE.match(unit):
            issues.append(ValidationIssue(idx, "Unit ID", "error", "Expected 3-digit unit id", unit))

        equip = _text(row.get("Equipment ID (Asset ID)"))
        if equip and not EQUIP_RE.match(equip):
            issues.append(ValidationIssue(idx, "Equipment ID (Asset ID)", "warn",
                                          "Equipment id format differs from example ###X-####", equip))

        for col in NUMERIC_FIELDS:
            v = row.get(col)
            if pd.notna(v) and pd.isna(pd.to_numeric(v, errors="coerce")):
                issues.append(ValidationIssue(idx, col, "warn",
                                              "Not numeric, blank in normalized output", v))

        dp = row.get("Design Pressure (KPag)")
        if pd.notna(pd.to_numeric(dp, errors="coerce")) and float(dp) < 0:
            issues.append(ValidationIssue(idx, "Design Pressure (KPag)", "error",
                                          "Design pressure must be >= 0", dp))

        d = _text(row.get("Last Inspection Date"))
        if d and not DATE_RE.match(d):
            issues.append(ValidationIssue(idx, "Last Inspection Date", "warn",
                                          "Expected date format YYYY-MM-DD", d))

        rr = _text(row.get("Risk Rank"))
        if rr and rr not in ALLOWED_RISK:
            issues.append(ValidationIssue(idx, "Risk Rank", "warn",
                                          "Risk rank not in {Low, Medium, High}", rr))

    return df, issues

def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    rename_map = {
        "Circuit /Equipment Tag": "circuit_tag",
        "Equipment ID (Asset ID)": "equipment_id",
        "Damage Mechanism as per Corrosion Study": "damage_mechanism",
        "Design Pressure (KPag)": "design_pressure_kpag",
        "Design Temperature (deg. C)": "design_temperature_c",
        "Last Inspection Date": "last_inspection_date",
        "Max STCR (MPY)": "max_stcr_mpy",
        "Max LTCR (MPY)": "max_ltcr_mpy",
        "Unit ID": "unit_id",
        "Risk Rank": "risk_rank",
    }
    out = out.rename(columns={k: v for k, v in rename_map.items() if k in out.columns})

    for c in ["unit_id", "circuit_tag", "equipment_id", "damage_mechanism", "last_inspection_date", "risk_rank"]:
        if c in out.columns:
            out[c] = out[c].astype("string").str.strip()

    for c in ["design_pressure_kpag", "design_temperature_c", "max_stcr_mpy", "max_ltcr_mpy"]:
        if c in out.columns:
            out[c] = pd.to_numeric(out[c], errors="coerce")

    return out
