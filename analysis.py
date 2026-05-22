# =====================================================================

# RQ1 — “Does the placement of a human approval step change oversight quality?”

# Beginner-friendly analysis pipeline.

# 

# What this script does, start to finish:

# 1. Loads the answer key + the three raw survey exports

# 2. Gives every participant an anonymous ID

# 3. Reshapes Conditions A & B from “wide” (1 row/person) to

# “long” (1 row/person/item)

# 4. Turns Condition C’s checkbox list into the same long format

# 5. Joins the answer key so each row knows if the item was an error

# 6. Derives `caught` and `false_alarm`

# 7. Saves the cleaned data.csv

# 8. Computes catch-rate and false-alarm-rate per condition

# 9. Makes the three charts

# 

# Runs in Google Colab or any local Python with pandas + matplotlib.

# In Colab: upload the 4 CSVs first (folder icon on the left), then run.

# =====================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ———————————————————————

# STEP 1 — Load the answer key and the three raw exports

# ———————————————————————

# The answer key tells us, for each item, whether it was an “error” or

# “correct”, and its position (1-20) in the fixed item order.

key = pd.read_csv(“answer_key.csv”)

raw_a = pd.read_csv(“raw_condition_A.csv”)  # Before  (Approve / Reject)
raw_b = pd.read_csv(“raw_condition_B.csv”)  # After   (Looks right / Flag as error)
raw_c = pd.read_csv(“raw_condition_C.csv”)  # None    (one list of flagged numbers)

# How many errors / correct items there are (denominators for our rates).

# These come straight from the answer key, so they stay correct even if

# you change the items later.

N_ERRORS  = int((key.item_type == “error”).sum())    # expected: 8
N_CORRECT = int((key.item_type == “correct”).sum())  # expected: 12

# ———————————————————————

# STEP 2 + 3 — Reshape the “choice” conditions (A and B) wide -> long

# ———————————————————————

# A and B both have 20 columns (Q1..Q20), one per item. We want one row

# per person PER item instead. `melt` does exactly that.

def reshape_choice(raw, condition, flag_value):
df = raw.copy()

```
# Drop the Google Forms timestamp if present (we don't need it).
df = df.drop(columns=[c for c in ["Timestamp"] if c in df.columns])

# STEP 2: assign anonymous IDs based on row order, e.g. B01, B02...
# (We use the first letter of the condition as a prefix.)
prefix = condition[0].upper()
df["participant_id"] = [f"{prefix}{i + 1:02d}" for i in range(len(df))]

# STEP 3: wide -> long. value_vars are the 20 question columns.
q_cols = [f"Q{i}" for i in range(1, 21)]
long = df.melt(
    id_vars="participant_id",
    value_vars=q_cols,
    var_name="item_id",
    value_name="response",
)

# Turn "Q7" into the integer 7 so we can join on the answer key.
long["item_id"] = long["item_id"].str.replace("Q", "", regex=False).astype(int)

long["condition"] = condition

# `flagged` = 1 if the participant marked this item as a problem.
# We lower-case and strip to be forgiving about spacing/capitalisation.
long["flagged"] = (
    long["response"].astype(str).str.strip().str.lower() == flag_value.lower()
).astype(int)

return long[["participant_id", "condition", "item_id", "flagged"]]
```

long_a = reshape_choice(raw_a, “before”, “Reject”)
long_b = reshape_choice(raw_b, “after”, “Flag as error”)

# ———————————————————————

# STEP 4 — Convert Condition C’s checklist into the same long format

# ———————————————————————

# In C, each person gives ONE cell like “3, 8, 12, 16” = the items they

# flagged. We expand that into 20 rows per person (flagged = 1 if listed).

def reshape_checklist(raw, condition):
df = raw.copy()
df = df.drop(columns=[c for c in [“Timestamp”] if c in df.columns])
df[“participant_id”] = [f”C{i + 1:02d}” for i in range(len(df))]

```
rows = []
for _, r in df.iterrows():
    cell = "" if pd.isna(r["flagged_items"]) else str(r["flagged_items"])
    # Accept commas or semicolons as separators; keep only digits.
    selected = set()
    for token in cell.replace(";", ",").split(","):
        token = token.strip()
        if token.isdigit():
            selected.add(int(token))
    # One row per item 1..20.
    for item in range(1, 21):
        rows.append({
            "participant_id": r["participant_id"],
            "condition": condition,
            "item_id": item,
            "flagged": 1 if item in selected else 0,
        })
return pd.DataFrame(rows)
```

long_c = reshape_checklist(raw_c, “none”)

# ———————————————————————

# STEP 5 — Stack all three, then join the answer key

# ———————————————————————

long_all = pd.concat([long_a, long_b, long_c], ignore_index=True)

data = long_all.merge(
key[[“item_id”, “item_type”, “item_position”]],
on=“item_id”,
how=“left”,
)

# ———————————————————————

# STEP 6 — Derive the two outcomes we care about

# ———————————————————————

# caught       = correctly flagged an item that WAS an error

# false_alarm  = flagged an item that was actually CORRECT

data[“caught”] = ((data.item_type == “error”) & (data.flagged == 1)).astype(int)
data[“false_alarm”] = ((data.item_type == “correct”) & (data.flagged == 1)).astype(int)

# ———————————————————————

# STEP 7 — Save the cleaned long-format dataset

# ———————————————————————

data.to_csv(“data.csv”, index=False)
print(f”Saved data.csv  ({len(data)} rows = “
f”{data.participant_id.nunique()} participants x 20 items)\n”)

# ———————————————————————

# STEP 8 — Rates per participant, then averaged per condition

# ———————————————————————

per_p = (
data.groupby([“participant_id”, “condition”])
.agg(caught=(“caught”, “sum”), false_alarm=(“false_alarm”, “sum”))
.reset_index()
)
per_p[“catch_rate”] = per_p[“caught”] / N_ERRORS
per_p[“false_alarm_rate”] = per_p[“false_alarm”] / N_CORRECT

ORDER = [“before”, “after”, “none”]  # fixed display order for all charts

# Standard error = std / sqrt(n). With only 1 person in a group it is NaN;

# that’s fine for a pilot — it just means “not enough data to show a bar’s error”.

def se(x):
return x.std(ddof=1) / (len(x) ** 0.5) if len(x) > 1 else 0.0

summary = (
per_p.groupby(“condition”)
.agg(
n=(“participant_id”, “count”),
catch_mean=(“catch_rate”, “mean”),
catch_se=(“catch_rate”, se),
fa_mean=(“false_alarm_rate”, “mean”),
fa_se=(“false_alarm_rate”, se),
)
.reindex(ORDER)
)
print(“Summary by condition:”)
print(summary.round(3), “\n”)

# ———————————————————————

# STEP 9a — Chart: error-catch rate by condition

# ———————————————————————

plt.figure(figsize=(6, 4))
plt.bar(summary.index, summary.catch_mean, yerr=summary.catch_se, capsize=5)
plt.ylim(0, 1)
plt.ylabel(“Mean error-catch rate”)
plt.title(“Error-catch rate by approval-step placement”)
plt.savefig(“chart_a_catch_rate.png”, dpi=150, bbox_inches=“tight”)
plt.close()

# ———————————————————————

# STEP 9b — Chart: false-alarm rate by condition

# ———————————————————————

plt.figure(figsize=(6, 4))
plt.bar(summary.index, summary.fa_mean, yerr=summary.fa_se, capsize=5, color=”#c0623f”)
plt.ylim(0, 1)
plt.ylabel(“Mean false-alarm rate”)
plt.title(“False-alarm rate by approval-step placement”)
plt.savefig(“chart_b_false_alarm.png”, dpi=150, bbox_inches=“tight”)
plt.close()

# ———————————————————————

# STEP 9c — Chart: first-half vs second-half catch rate (attention decay)

# ———————————————————————

errors = data[data.item_type == “error”].copy()
errors[“half”] = np.where(errors.item_position <= 10, “first10”, “last10”)

half = (
errors.groupby([“participant_id”, “condition”, “half”]).caught.mean().reset_index()
)
half_summary = (
half.groupby([“condition”, “half”]).caught.mean().unstack().reindex(ORDER)
)
print(“First-half vs second-half catch rate:”)
print(half_summary.round(3), “\n”)

x = np.arange(len(ORDER))
w = 0.35
plt.figure(figsize=(6, 4))
plt.bar(x - w / 2, half_summary[“first10”], w, label=“Items 1-10”)
plt.bar(x + w / 2, half_summary[“last10”], w, label=“Items 11-20”)
plt.xticks(x, ORDER)
plt.ylim(0, 1)
plt.ylabel(“Mean error-catch rate”)
plt.title(“Catch rate: first half vs second half”)
plt.legend()
plt.savefig(“chart_c_decay.png”, dpi=150, bbox_inches=“tight”)
plt.close()

print(“Done. Wrote: data.csv, chart_a_catch_rate.png, “
“chart_b_false_alarm.png, chart_c_decay.png”)
