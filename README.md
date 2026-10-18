# SpendMap

Understand spending with editable categories for **budget analysts**.

Original topic: **Personal Finance Spending Clusters** from [the source post](https://www.instagram.com/p/DdyMaogE4ud/).

> Local portfolio implementation developed with Codex assistance. Measured results and limitations are documented; no production adoption, revenue or hiring outcome is claimed.

![Application screenshot](reports/screenshots/app.png)

## What works

- Rule categories
- merchant overrides
- monthly trends
- standardized clustering

[Example output](reports/example-output.json) · [Recorded checks](reports/test-results.txt) · [Learning and interview guide](LEARNING_GUIDE.md)

## Start

Python 3.12 is the validated Python runtime. Run commands from this repository directory. Windows users activate `.venv\Scripts\activate` instead of `source`.

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python generate.py
python app.py
```

Open **http://127.0.0.1:8080**. Keep the process running. Set `PORT` to use another port. The Python development servers are intended for local demonstrations.

## Demonstration

Change Market to Food in the category rules, rerun, and confirm category totals still sum to the original cents total. Compare two and four clusters and inspect segment sizes.

## Architecture and decisions

Browser controls → validated Flask API → project analysis/workflow → results and export.

Stack: pandas · scikit-learn · Flask.

1. Use integer cents for ingestion and reconciliation before displaying currency.
2. Map merchant names to user-defined categories and retain unmatched transactions as Uncategorized.
3. Cluster standardized category shares and transaction frequency so total spending does not dominate segments.

## Verification

```sh
python -m pytest -q
```

See [VERIFICATION.md](VERIFICATION.md) for actual executed checks, setup verification, model/data results and any outstanding environment limitations. The [recorded CI runs](reports/ci-verification.json) passed for the linked source revision.

## Data and attribution

Synthetic transactions. See [DATA_AND_SOURCES.md](DATA_AND_SOURCES.md) for provenance and usage notes. Original project code is MIT unless a preserved source file or dependency states otherwise. Model and third-party data licenses remain separate.

## Limitations and next improvement

Synthetic transactions; no bank connection, persistence of category preferences or financial advice. KMeans clusters are descriptive and depend on category definitions, scaling and k. Silhouette is an internal separation diagnostic, not business validation.

Suggested extension: Add a CSV importer with strict schema validation and formula-safe export handling.

## Honest portfolio use

This implementation and documentation were developed with substantial Codex assistance. Before presenting it, run the demonstration, explain the design choices, and complete the suggested independent modification. Do not describe generated code as work experience, an accepted upstream contribution, or a deployed production service.

## Connect

[LinkedIn — Abhijith Viswanathan](https://www.linkedin.com/in/abhijith-viswanathan-0a7216436/)
