from pathlib import Path
from integrity_data_foundation.pipeline import run

def test_pipeline_runs(tmp_path):
    input_dir = Path(__file__).resolve().parents[1] / "data" / "sample"
    out_dir = tmp_path / "out"
    code = run(input_dir, out_dir)
    assert (out_dir / "validation_issues.json").exists()
    assert (out_dir / "normalized_integrity_data.csv").exists()
    assert code in (0, 1, 2)
