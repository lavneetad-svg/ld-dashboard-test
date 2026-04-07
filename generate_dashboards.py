import pandas as pd
import os

os.makedirs("output", exist_ok=True)

# PHASE 1
df1 = pd.read_csv("phase1_baseline.csv")

summary1 = df1.groupby("goal").agg(
    avg_self=("pre_score_self", "mean"),
    avg_manager=("pre_score_manager", "mean"),
    count=("participant_id", "count")
).reset_index()

html1 = f"""
<h1>Phase 1: Baseline</h1>
<p>Total Rows (Selections): {len(df1)}</p>
<p>Unique Participants: {df1['participant_id'].nunique()}</p>
{summary1.to_html(index=False)}
"""

with open("output/phase1.html", "w") as f:
    f.write(html1)


# PHASE 2
df2 = pd.read_csv("phase2_learning.csv")

html2 = f"""
<h1>Phase 2: Learning</h1>
<p>Completion Rate: {df2['completed'].mean():.2%}</p>
{df2.groupby('module')['score'].mean().to_frame().to_html()}
"""

with open("output/phase2.html", "w") as f:
    f.write(html2)


# PHASE 3
df3 = pd.read_csv("phase3_behaviour.csv")

theme_counts = df3["theme"].value_counts().to_frame().to_html()

html3 = f"""
<h1>Phase 3: Behaviour</h1>
<p>Participants: {df3['participant_id'].nunique()}</p>
<p>ALP Completed: {df3[df3['alp_completed']==1]['participant_id'].nunique()}</p>
{theme_counts}
"""

with open("output/phase3.html", "w") as f:
    f.write(html3)


# PHASE 4
df4 = pd.read_csv("phase4_results.csv")

html4 = f"""
<h1>Phase 4: Results</h1>
<p>Avg Project Score: {df4['project_score'].mean()}</p>
<p>Avg Impact: {df4['impact_metric'].mean()}</p>
"""

with open("output/phase4.html", "w") as f:
    f.write(html4)

print("Dashboards generated!")
