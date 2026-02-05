# integrity-data-foundation
Data validation and structuring baselines for integrity and RBI decision support.

## integrity-data-foundation

Data validation and structuring baselines for integrity and RBI decision support.

This repository focuses on the work that determines whether integrity analytics and ML can be trusted: data structure, validation, traceability, and failure visibility. It is not a production system and it does not include any client data.

### What this is
A small Python package that:
- Normalizes common integrity fields into consistent formats
- Validates required columns, units, ranges, and allowed values
- Produces a clean dataset plus a validation report that makes issues explicit

### What this is not
This repository does not:
- Replace engineering judgment
- Provide RBI calculations or inspection plans
- Claim model accuracy or production readiness

### Why it matters
In integrity programs, poor data quality does not only reduce accuracy, it distorts decisions. The fastest way to lose trust in automation is to hide uncertainty. This project is designed to surface it.

### Design principle
Make assumptions explicit and make failure modes visible.

### Quickstart

1) Create a virtual environment and install:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -e .
