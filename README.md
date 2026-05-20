# Integrity Data Foundation

Engineering-first data validation and structuring baselines for integrity and risk-based inspection decision support.

This repository focuses on the part most teams underestimate: making engineering data consistent, traceable, and defensible before adding advanced analytics or machine learning. The goal is not to produce impressive outputs, but to build a reliable foundation where assumptions are explicit and failure modes are visible.

## Integrity Code Series

Part of an ongoing series of physics-first integrity simulators by Felipe Rocha:

| # | Repo | Domain |
|---|---|---|
| Week 3 | [Integrity-code-series-3](https://github.com/felipearocha/Integrity-code-series-3) | F1 lap simulation (six coupled ODEs) |
| Week 6 | [Integrity-code-series-week6-smartphone-galvanic](https://github.com/felipearocha/Integrity-code-series-week6-smartphone-galvanic) | Smartphone galvanic corrosion (Laplace + Butler-Volmer) |
| Week 7 | [integrity_code_series_week7_h2_lferw](https://github.com/felipearocha/integrity_code_series_week7_h2_lferw) | LF-ERW H2 conversion (B31.12 + NACE TM0316) |
| Week 8 | [integrity-code-series-week8-creep-fatigue-heater](https://github.com/felipearocha/integrity-code-series-week8-creep-fatigue-heater) | Creep-fatigue 9Cr-1Mo (Norton/Omega + Coffin-Manson) |
| Week 9 | [integrity-code-series-week9-cui](https://github.com/felipearocha/integrity-code-series-week9-cui) | CUI thermohygro-electrochemical (3 PDEs, Strang) |
| Week 10 | [integrity-code-series-week-10_nnph_scc](https://github.com/felipearocha/integrity-code-series-week-10_nnph_scc) | NNpHSCC full-physics (Chen-Sutherby-Xing + BS 7910) |
| Bonus | [Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation](https://github.com/felipearocha/Vibration-Accelerated-Corrosion-Coupled-Mechano-Electrochemical-Simulation) | Vibration-accelerated corrosion (SDOF + Butler-Volmer + Archard) |
| Bonus | [synthetic-integrity-digital-twin-piml](https://github.com/felipearocha/synthetic-integrity-digital-twin-piml) | Physics-informed neural-network surrogate |
| Bonus | [integrity-data-foundation](https://github.com/felipearocha/integrity-data-foundation) | Engineering data validation baseline |

## What this is
A set of lightweight Python baselines to:
- validate and normalize integrity datasets
- enforce engineering-aware data contracts
- expose inconsistencies early (instead of hiding them)
- produce structured outputs ready for downstream decision workflows

## What this is not
This is not a production product, not a client deliverable, and not a benchmark repository. No client data is included.

## Why it matters
In integrity programs, poor data does not only reduce accuracy. It changes decisions. A clean, structured, and auditable dataset is often the largest lever for ROI because it reduces rework, shortens decision cycles, and increases trust in outputs.

## Repository principles
This repo is designed around:
- explicit assumptions
- transparent validation logic
- deterministic outputs
- security-aware handling of data artifacts

## Quickstart
Create and activate a virtual environment, install dependencies, and run the example pipeline on sample data.

Windows:
python -m venv .venv
. .venv\Scripts\activate
pip install -r requirements.txt
python -m integrity_data_foundation.pipeline --input data/sample --output out

macOS/Linux:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m integrity_data_foundation.pipeline --input data/sample --output out

## Outputs
The pipeline produces:
- normalized datasets
- validation reports (what failed, why, where)
- a structured export for downstream decision workflows

## Security note
Treat engineering data as decision-critical. This repository includes guidance to avoid leaking sensitive information and to keep data lineage and integrity checks visible.

## License
MIT