# Does the Placement of a Human Approval Step Change Oversight Quality?

### A Small Between-Subjects Pilot Study

**Author:** [[FILL: name]]
**Date:** [[FILL: month year]]
**Type:** Independent pilot study / method demonstration
**Repository:** [[FILL: link to repo or notebook]]

> NOTE — fill-in conventions used in this template:
> `[[FILL: ...]]` = insert a value or short text. `> NOTE:` blocks are guidance for you
> and should be **deleted before publishing**. Condition labels appear two ways: the
> human-readable names **Before / After / None**, and the export/analysis labels
> **`before` / `after` / `none`** (as used in `data.csv` and `analysis.py`). Keep both
> consistent with the files.

-----

## Abstract

> NOTE: Write last, ~150–250 words. Cover, in plain order: the question, the design in one
> line, what you measured, the headline numbers, and one sentence of honest caveat. Do not
> overstate; this is a pilot.

[[FILL: abstract — ~150–250 words]]

-----

## 1. Introduction

Human-in-the-loop review is widely treated as a safeguard when AI systems perform
consequential actions. Less examined is whether the *placement* of that review — before
an action takes effect, after it, or only as passive end-of-task monitoring — changes how
reliably people catch errors, and whether attention to the review step decays over time.

This pilot is a small, deliberately scoped study of that question. It is intended as a
method demonstration rather than a source of general findings: the sample is small, the
task is artificial, and the error rate is elevated for measurability. Its value is in
testing whether the effect is measurable with this instrument and in surfacing the design
issues a larger study would need to address.

> NOTE: Keep this honest and short (this length is fine). Do not inflate into broad claims
> about oversight or alignment.

-----

## 2. Research question and hypotheses

**Research question.** When a person supervises an AI assistant that occasionally makes
errors, does the placement of the human approval step change how many errors they catch?

**Primary hypothesis (directional).** Error-catch rate is highest in the **Before**
(pre-approval) condition, lower in **After** (post-review), and lowest in **None**
(passive monitoring): `before ≥ after ≥ none`.

**Secondary hypothesis (exploratory).** Catch rate declines from the first half to the
second half of the task, with a larger decline in the **After** and **None** conditions
than in **Before** (an attention-decay / rubber-stamping signal).

> NOTE: Frame the secondary hypothesis as exploratory. The pilot is underpowered to test
> it confirmatorily.

-----

## 3. Methods

### 3.1 Participants

Target sample: approximately **25 participants per condition** (~75 total).
Actual recruited: [[FILL: total recruited]].
Analyzed after exclusions: [[FILL: total analyzed]] ( `before` = [[FILL: n]],
`after` = [[FILL: n]], `none` = [[FILL: n]] ).

> NOTE: Insert final per-condition counts from the `n` column of the summary printed by
> `analysis.py`. If you used the free network-recruited fallback (~8/condition), say so
> here and note the study is underpowered accordingly.

### 3.2 Recruitment source

Participants were recruited via [[FILL: Prolific / personal network / other]].
[[FILL: compensation, if any]]. The task took approximately five minutes.

### 3.3 Design

Between-subjects: each participant completed one condition only. Assignment to condition
was [[FILL: randomized via Prolific group distribution / split by list]].

> NOTE: Between-subjects is deliberate — once a participant learns that errors exist,
> vigilance carries over and would contaminate a within-subjects comparison.

### 3.4 Conditions

All three conditions used the identical 20-item task and policy; only the timing and
framing of the review step differed.

|Label   |Name                      |Review timing                        |Participant response                 |
|--------|--------------------------|-------------------------------------|-------------------------------------|
|`before`|Before (pre-approval gate)|Before the action takes effect       |Approve / Reject, per item           |
|`after` |After (post-review)       |After the action is shown as recorded|Looks right / Flag as error, per item|
|`none`  |None (passive monitoring) |Only at the end                      |List the item numbers believed wrong |

### 3.5 Task

Participants reviewed an AI assistant processing small expense/reimbursement entries
against a fixed six-rule policy (Appendix A). The task contained **20 items in fixed
order**: **12 correct** and **8 containing a seeded error**. AI outputs were pre-written
(no live model was used), so each item’s correct/error status is fixed and scoring is
objective. Three correct items were designed to be plausibly suspect, to detect
over-flagging.

> NOTE: State the elevated error rate plainly: 8/20 = 40%, chosen so catch rate is
> measurable, not to reflect real systems. This belongs here and in Limitations.

### 3.6 Scoring definitions

For each participant-item:

- **caught** = the participant flagged an item that was an error (higher is better).
- **false_alarm** = the participant flagged an item that was actually correct (lower is better).

Per participant: catch rate = caught / 8; false-alarm rate = false_alarms / 12. Both are
reported because catch rate alone can be inflated by flagging everything; the false-alarm
rate distinguishes genuine discrimination from blanket suspicion.

### 3.7 Exclusion criteria

Participants were excluded if they (a) did not consent, (b) reported not being a fluent
English reader, or (c) failed the single attention-check item. Exclusions: [[FILL: count]]
(no consent = [[FILL]], failed attention check = [[FILL]], other = [[FILL]]).

-----

## 4. Materials and procedure

Participants saw a consent and screening section, then the policy, then condition-specific
instructions, then the 20 items, then one attention check, then a debrief. The instrument
was delivered as three Google Forms (one per condition), identical except for the review
framing and response options. Responses were exported to CSV, columns renamed to the
analysis format (`Q1`–`Q20` for the Before/After forms; `flagged_items` for the None form),
and processed with `analysis.py`.

Materials (verbatim policy text and item examples) are in Appendix A and the project
repository.

> NOTE: Do not rewrite the instrument here — reference it. The canonical wording lives in
> the Forms text and project files.

-----

## 5. Analysis plan

Analysis is descriptive and pre-specified. `analysis.py` reshapes the three exports into a
long-format dataset (`data.csv`, one row per participant-item), derives `caught` and
`false_alarm`, computes per-participant rates, and averages them by condition. Primary
output: mean catch rate by condition with standard errors. Secondary outputs: mean
false-alarm rate by condition, and first-half vs second-half catch rate by condition.

An optional exploratory Kruskal–Wallis test across conditions may be reported, **clearly
labeled as exploratory and underpowered**; descriptive means are the basis for any
statement, not the test.

> NOTE: With pilot-size samples, lead with the descriptive estimates and report any test
> cautiously.

-----

## 6. Results

> NOTE: All numbers below come from the console output and figures produced by
> `analysis.py`. Insert the three PNGs at the marked points. Do not write interpretation
> beyond what the numbers support.

### 6.1 Sample and exclusions

[[FILL: total recruited]] participants completed the task; [[FILL: excluded]] were excluded
([[FILL: brief reason breakdown]]), leaving [[FILL: total analyzed]] for analysis.

### 6.2 Error-catch rate by condition

[[INSERT FIGURE: chart_a_catch_rate.png]]
*Figure 1. Mean error-catch rate by condition (error bars = standard error).*

|Condition (`label`)|n       |Mean catch rate|SE      |
|-------------------|--------|---------------|--------|
|Before (`before`)  |[[FILL]]|[[FILL]]       |[[FILL]]|
|After (`after`)    |[[FILL]]|[[FILL]]       |[[FILL]]|
|None (`none`)      |[[FILL]]|[[FILL]]       |[[FILL]]|

[[FILL: one or two plain sentences stating the observed ordering and the size of the gaps.
Example format only, replace with real values: “Catch rate was highest in the Before
condition (M = __, SE = __) and lowest in None (M = __, SE = __).” — hypothetical until
filled.]]

### 6.3 False-alarm rate by condition

[[INSERT FIGURE: chart_b_false_alarm.png]]
*Figure 2. Mean false-alarm rate by condition (error bars = standard error).*

|Condition (`label`)|n       |Mean false-alarm rate|SE      |
|-------------------|--------|---------------------|--------|
|Before (`before`)  |[[FILL]]|[[FILL]]             |[[FILL]]|
|After (`after`)    |[[FILL]]|[[FILL]]             |[[FILL]]|
|None (`none`)      |[[FILL]]|[[FILL]]             |[[FILL]]|

[[FILL: state whether false-alarm rates were low and comparable across conditions, or
whether any condition showed elevated over-flagging.]]

### 6.4 First-half vs second-half catch rate

[[INSERT FIGURE: chart_c_decay.png]]
*Figure 3. Mean error-catch rate, first 10 items vs last 10 items, by condition.*

|Condition (`label`)|First half|Second half|
|-------------------|----------|-----------|
|Before (`before`)  |[[FILL]]  |[[FILL]]   |
|After (`after`)    |[[FILL]]  |[[FILL]]   |
|None (`none`)      |[[FILL]]  |[[FILL]]   |

[[FILL: state the observed direction of change per condition; note this is exploratory.]]

### 6.5 Optional exploratory test

[[FILL: if reported — test name, statistic, p-value, and an explicit note that it is
exploratory and underpowered. Otherwise delete this subsection.]]

-----

## 7. Discussion

> NOTE: 1–2 short paragraphs. Say what the estimates *suggest*, tied to the hypotheses, and
> what they cannot establish at this scale. Avoid causal or general claims.

[[FILL: what the pattern suggests about review placement and oversight quality, stated as
preliminary.]]

[[FILL: what the first-half/second-half pattern hints about attention decay, if anything,
stated as exploratory.]]

-----

## 8. Limitations

This is a pilot and its results are preliminary effect estimates, not general findings.
Specific limitations:

- **Small sample.** Per-condition n is small; estimates are imprecise and the study is
  underpowered for formal hypothesis testing.
- **Artificial task.** A single expense-review domain with short, stylized entries; results
  may not transfer to other tasks or to real workplace conditions.
- **Elevated error rate.** 40% of items contained errors, chosen for measurability, far
  above realistic systems; this likely raises baseline vigilance.
- **No live model.** AI outputs were pre-written rather than generated by a model, which
  removes natural variation in error type and phrasing.
- **Non-expert reviewers.** Crowd or convenience participants, not domain experts or the
  intended operators of such a system.
- **Manipulation via framing.** Conditions differ in instruction and timing framing rather
  than in a fully realistic system interface.
- **Single exposure.** Each participant saw one condition once; no learning or fatigue
  across sessions is captured.

-----

## 9. Conclusion

[[FILL: 2–4 sentences. Restate the question, the preliminary pattern, and the most useful
next step (e.g., larger sample, lower error rate, live model, expert participants). End
without overclaiming.]]

-----

## Appendix A — Expense policy (verbatim)

> NOTE: Paste the exact six-rule policy text shown to participants. Do not paraphrase.

- Claim period: March 1–31, 2026.
- A receipt is required for any expense over $25.
- Meals: maximum $30 per person.
- Reimbursable categories: Travel, Meals, Office Supplies, Software.
- Not reimbursable: alcohol, personal items, gifts.
- No duplicate claims. The recorded amount and category must match the receipt, and any
  arithmetic must be correct.

## Appendix B — Item examples (optional)

> NOTE: Optionally include 2–3 representative items (one correct, one error, one
> correct-but-tempting) copied verbatim from the instrument, with their correct/error
> status and error type. The full 20-item bank and answer key are in the repository
> (`answer_key.csv`). Do not alter wording.

[[FILL: 2–3 verbatim item examples, or delete this appendix and point to the repo.]]
