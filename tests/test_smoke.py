import json
from pathlib import Path

import pandas as pd

from integrity_data_foundation.pipeline import run
from integrity_data_foundation.validators import normalize_dataframe, validate_dataframe

SAMPLE = Path(__file__).resolve().parents[1] / "data" / "sample"
CLEAN = {
    "Unit ID": "984",
    "Circuit /Equipment Tag": "SPL-13",
    "Equipment ID (Asset ID)": "984C-6003",
    "Damage Mechanism as per Corrosion Study": "Thinning",
}


def issues_of(**cells):
    _, issues = validate_dataframe(pd.DataFrame([{**CLEAN, **cells}]))
    return [(i.field, i.severity) for i in issues]


def test_sample_fails_with_the_seeded_errors(tmp_path):
    assert run(SAMPLE, tmp_path) == 1
    issues = json.loads((tmp_path / "validation_issues.json").read_text(encoding="utf-8"))
    errors = {(i["row_index"], i["field"]) for i in issues if i["severity"] == "error"}
    assert errors == {
        (1, "Damage Mechanism as per Corrosion Study"),
        (1, "Design Pressure (KPag)"),
        (2, "Unit ID"),
    }
    assert (tmp_path / "normalized_integrity_data.csv").exists()


def test_missing_input_returns_2(tmp_path):
    assert run(tmp_path, tmp_path / "out") == 2


def test_clean_row_has_no_issues():
    assert issues_of() == []


def test_blank_required_cell_is_an_error():
    assert issues_of(**{"Unit ID": float("nan")}) == [("Unit ID", "error")]


def test_blank_optional_cells_raise_nothing():
    assert issues_of(**{"Last Inspection Date": float("nan"), "Risk Rank": float("nan")}) == []


def test_blank_stays_blank_after_normalize():
    out = normalize_dataframe(pd.DataFrame({"Risk Rank": [" Low ", float("nan")]}))
    assert out["risk_rank"][0] == "Low"
    assert pd.isna(out["risk_rank"][1])
