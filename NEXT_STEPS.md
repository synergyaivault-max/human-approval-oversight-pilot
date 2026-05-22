# NEXT STEPS

## Immediate

- Verify all repository files render correctly on GitHub.
- Confirm README.md formatting and links display properly.
- Replace any remaining placeholder contact fields in public artifacts.
- Review repository visibility and public-facing language one more time.

## Survey Validation

- Test all three HTML survey artifacts on:
  - mobile
  - desktop
  - multiple browsers if possible
- Verify CSV exports match the analysis contract exactly.
- Confirm no data is stored unintentionally in-browser.

## Dry Run

- Run one complete fake participant cycle through each condition.
- Export CSVs.
- Run `analysis.py`.
- Confirm charts regenerate correctly.
- Confirm exclusion logic still works.

## Recruitment Preparation

- Prepare simple participant invitation language.
- Decide whether recruitment will be:
  - personal network
  - Prolific
  - other small pilot source
- Freeze instrument wording before collecting real responses.

## Real Pilot Requirements

Before any claims:
- collect real participant data
- preserve exclusion log
- document any deviations
- separate raw vs cleaned data
- rerun analysis on real exports only

## Technical Review

Before publication:
- have one technically literate reviewer inspect:
  - README
  - scoring logic
  - analysis pipeline
  - synthetic vs real labeling
  - limitations framing

## Publication Gate

Do not:
- remove the simulated/demo label
- present charts as findings
- generalize conclusions
- claim empirical results

until:
- real participant data exists
- analysis is rerun
- review is completed

## Current State

The repository currently represents:
- a verified simulated scaffold
- a governance/workflow design artifact
- a pilot-ready structure

It does not yet represent:
- completed empirical research
- published findings
- validated conclusions
