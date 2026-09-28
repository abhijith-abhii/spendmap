# SpendMap — learning guide

## What it does

Understand spending with editable categories. The intended user is budget analysts. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Change Market to Food in the category rules, rerun, and confirm category totals still sum to the original cents total. Compare two and four clusters and inspect segment sizes.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Use integer cents for ingestion and reconciliation before displaying currency.
2. Map merchant names to user-defined categories and retain unmatched transactions as Uncategorized.
3. Cluster standardized category shares and transaction frequency so total spending does not dominate segments.

## Five interview questions

1. **What problem does this project solve, and what is its unit of work?** Explain understand spending with editable categories, identify budget analysts as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Use integer cents for ingestion and reconciliation before displaying currency. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Map merchant names to user-defined categories and retain unmatched transactions as Uncategorized. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Cluster standardized category shares and transaction frequency so total spending does not dominate segments. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** Synthetic transactions; no bank connection, persistence of category preferences or financial advice. KMeans clusters are descriptive and depend on category definitions, scaling and k. Silhouette is an internal separation diagnostic, not business validation. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a CSV importer with strict schema validation and formula-safe export handling.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated understand spending with editable categories using pandas · scikit-learn · Flask, with rule categories and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
