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

1. **Why keep money as integer cents?** Integer arithmetic avoids accumulating binary floating-point errors in transaction totals. Normalized shares are computed only when needed for analysis and clustering.

2. **How do custom categories affect analysis?** User-defined rules reassign merchants before category totals and customer features are calculated. A change in the category mapping can therefore change the clusters.

3. **What goes into the clustering model?** Normalized category spending shares and transaction-frequency information describe customer behavior. Standardization prevents a larger numerical scale from dominating Euclidean distance.

4. **What does silhouette measure?** It compares within-cluster cohesion with separation from other clusters. It is an internal diagnostic, not proof that the segments are useful or stable business categories.

5. **Are the clusters financial recommendations?** No. The transactions are synthetic and the groups are descriptive. The app does not infer creditworthiness, prescribe investments or claim real savings.

## Independent exercise

Add a CSV importer with strict schema validation and formula-safe export handling.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Built an editable-rule spending dashboard with integer-cent reconciliation and standardized customer clustering, including silhouette diagnostics on synthetic transactions.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
