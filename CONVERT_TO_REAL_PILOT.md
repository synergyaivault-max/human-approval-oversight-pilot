# Convert to Real Pilot

## Purpose

This scaffold is currently simulated/demo-only. The following steps are required before any real-world pilot, findings, or claims can exist.

## Before Recruitment

- Verify all survey artifacts on mobile and desktop.
- Confirm CSV export structure matches the analysis contract.
- Re-run synthetic dry test after any modification.
- Freeze instrument wording before recruitment.
- Verify informed consent language.

## Recruitment Requirements

- Recruit a small convenience sample.
- Avoid deceptive recruitment language.
- Preserve participant anonymity.
- Keep a simple exclusion log.

## Data Handling

- Store raw CSV exports separately from cleaned data.
- Remove identifiers before analysis.
- Preserve original raw exports unchanged.

## Analysis Requirements

- Replace all synthetic CSVs with real participant data.
- Run the existing `analysis.py` pipeline without modifying scoring logic mid-run.
- Document exclusions before chart generation.
- Preserve reproducibility.

## Reporting Rules

- Clearly distinguish exploratory observations from findings.
- Include limitations prominently.
- Do not generalize beyond the task domain or sample size.
- Do not present synthetic/demo charts as real results.

## Before Public Release

- Technical review by an external reviewer.
- Final verification that no synthetic artifacts remain mislabeled.
- Confirm all public-facing language matches actual project status.

## Current Status

As of this document, the repository remains a simulated scaffold with no real participant data and no findings.
