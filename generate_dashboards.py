import pandas as pd
import matplotlib.pyplot as plt

# ---------- PHASE 1 ----------
df1 = pd.read_csv("phase1_baseline.csv")

summary1 = df1.groupby("goal")["pre_score_self"].mean()

plt.figure()
summary1.plot(kind="bar")
plt.title("Phase 1: Avg Self Score by Goal")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("phase1_chart.png")
plt.close()

html1 = f"""
<h1 style="color:#2E86C1;">Phase 1: Baseline</h1>
<p><b>Total Selections:</b> {len(df1)}</p>
<p><b>Unique Participants:</b> {df1['participant_id'].nunique()}</p>
<img src="phase1_chart.png" width="500">
"""

with open("phase1.html", "w") as f:
    f.write(html1)


# ---------- PHASE 2 ----------
df2 = pd.read_csv("phase2_learning.csv")

summary2 = df2.groupby("module")["score"].mean()

plt.figure()
summary2.plot(kind="bar")
plt.title("Phase 2: Avg Score by Module")
plt.tight_layout()
plt.savefig("phase2_chart.png")
plt.close()

html2 = f"""
<h1 style="color:#28B463;">Phase 2: Learning</h1>
<p><b>Completion Rate:</b> {df2['completed'].mean():.2%}</p>
<img src="phase2_chart.png" width="500">
"""

with open("phase2.html", "w") as f:
    f.write(html2)


# ---------- PHASE 3 ----------
df3 = pd.read_csv("phase3_behaviour.csv")

theme_counts = df3["theme"].value_counts()

plt.figure()
theme_counts.plot(kind="bar")
plt.title("Phase 3: Behaviour Themes")
plt.tight_layout()
plt.savefig("phase3_chart.png")
plt.close()

html3 = f"""
<h1 style="color:#AF7AC5;">Phase 3: Behaviour</h1>
<p><b>Participants:</b> {df3['participant_id'].nunique()}</p>
<img src="phase3_chart.png" width="500">
"""

with open("phase3.html", "w") as f:
    f.write(html3)


# ---------- PHASE 4 ----------
df4 = pd.read_csv("phase4_results.csv")

html4 = f"""
<h1 style="color:#E67E22;">Phase 4: Results</h1>
<p><b>Avg Project Score:</b> {df4['project_score'].mean()}</p>
<p><b>Avg Impact:</b> {df4['impact_metric'].mean()}</p>
"""

with open("phase4.html", "w") as f:
    f.write(html4)

print("Visual dashboards generated!")
