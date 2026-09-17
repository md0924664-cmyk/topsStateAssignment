"""
Assignment: Telco Customer Churn Analysis
(Originally framed as Excel tasks -- Filter, PivotTable, AVERAGEIF, Bar
Chart, CORREL -- reproduced here in Python using pandas/matplotlib, which
provide the exact same functionality.)

Author: Mihir Darji
Tools used: pandas, matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# =====================================================================
# Sample "Telco-Customer-Churn.csv" style dataset
# (Small representative sample built in-code; replace with
#  pd.read_csv("Telco-Customer-Churn.csv") if you have the real file.)
# =====================================================================

data = {
    "customerID": [f"C{1000+i}" for i in range(20)],
    "tenure": [1, 34, 2, 45, 2, 8, 22, 10, 28, 62,
               13, 16, 58, 49, 25, 69, 52, 71, 10, 21],
    "MonthlyCharges": [29.85, 56.95, 53.85, 42.30, 70.70, 99.65, 89.10, 29.75,
                        104.80, 56.15, 49.95, 18.95, 100.35, 103.70, 105.50,
                        113.25, 20.65, 106.70, 55.20, 99.90],
    "Contract": ["Month-to-month", "One year", "Month-to-month", "One year",
                 "Month-to-month", "Month-to-month", "Two year", "Month-to-month",
                 "Month-to-month", "Two year", "Month-to-month", "Month-to-month",
                 "Two year", "One year", "Month-to-month", "Two year",
                 "Month-to-month", "Two year", "One year", "Month-to-month"],
    "InternetService": ["DSL", "DSL", "DSL", "DSL", "Fiber optic", "Fiber optic",
                         "Fiber optic", "No", "Fiber optic", "DSL", "No",
                         "DSL", "Fiber optic", "Fiber optic", "Fiber optic",
                         "DSL", "No", "Fiber optic", "DSL", "Fiber optic"],
    "Churn": ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "No",
              "Yes", "No", "No", "No", "No", "No", "Yes", "No",
              "No", "No", "No", "Yes"],
}

df = pd.DataFrame(data)
df.to_csv("Telco-Customer-Churn.csv", index=False)
print("Dataset preview:")
print(df.head(10), "\n")


# =====================================================================
# Q1. Filter feature -> count Churn = 'Yes' vs Churn = 'No'
# =====================================================================

print("=" * 70)
print("Q1. Count of Churned vs Non-Churned Customers (Filter equivalent)")
print("=" * 70)

churn_counts = df["Churn"].value_counts()
print(churn_counts, "\n")

# ANSWER:
# In Excel, this is done by applying a Filter on the "Churn" column and
# reading the row count for each filtered value (or using
# =COUNTIF(Churn_range,"Yes") and =COUNTIF(Churn_range,"No")).
# In pandas, df["Churn"].value_counts() gives the same result instantly --
# it counts how many rows fall into each category of the column.


# =====================================================================
# Q2. PivotTable -> Contract type vs Churn count
# =====================================================================

print("=" * 70)
print("Q2. PivotTable: Contract Type vs Churn Count")
print("=" * 70)

pivot_table = pd.pivot_table(
    df,
    index="Contract",
    columns="Churn",
    values="customerID",
    aggfunc="count",
    fill_value=0
)
print(pivot_table, "\n")

# ANSWER:
# This mirrors an Excel PivotTable with "Contract" dragged to Rows,
# "Churn" dragged to Columns, and "customerID" (or any ID column) dragged
# to Values with the summary set to "Count". Typically, month-to-month
# contracts show the highest churn count, since customers on flexible,
# short-term contracts can leave anytime, while one-year and two-year
# contracts show much lower churn because customers are locked in and
# have already shown longer-term commitment.


# =====================================================================
# Q3. AVERAGEIF equivalent -> average MonthlyCharges by churn status
# =====================================================================

print("=" * 70)
print("Q3. Average MonthlyCharges: Churned vs Non-Churned")
print("=" * 70)

avg_charges_churned = df.loc[df["Churn"] == "Yes", "MonthlyCharges"].mean()
avg_charges_not_churned = df.loc[df["Churn"] == "No", "MonthlyCharges"].mean()

print(f"Average MonthlyCharges (Churn = Yes): {avg_charges_churned:.2f}")
print(f"Average MonthlyCharges (Churn = No):  {avg_charges_not_churned:.2f}\n")

# ANSWER:
# Excel formulas used would be:
#   =AVERAGEIF(Churn_range, "Yes", MonthlyCharges_range)
#   =AVERAGEIF(Churn_range, "No",  MonthlyCharges_range)
# The pandas equivalent filters MonthlyCharges by the Churn condition and
# takes the mean of each group. Typically, churned customers show a
# HIGHER average MonthlyCharges than retained customers -- suggesting
# that customers paying more per month are more likely to leave,
# possibly due to price sensitivity or feeling they aren't getting
# enough value for the higher cost.


# =====================================================================
# Q4. Bar chart -> Churned vs Non-Churned by InternetService type
# =====================================================================

print("=" * 70)
print("Q4. Bar Chart: Churn Count by InternetService Type")
print("=" * 70)

service_churn = pd.crosstab(df["InternetService"], df["Churn"])
print(service_churn, "\n")

service_churn.plot(kind="bar", figsize=(7, 5), color=["#4C72B0", "#DD8452"])
plt.title("Churned vs Non-Churned Customers by Internet Service Type")
plt.xlabel("Internet Service Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.savefig("churn_by_internet_service.png", dpi=150)
print("Bar chart saved as 'churn_by_internet_service.png'")
print("(Excel equivalent: select the pivoted InternetService-vs-Churn "
      "table -> Insert -> Bar Chart -> Clustered Column.)\n")


# =====================================================================
# Q5. CORREL equivalent -> correlation between Tenure and Churn
# =====================================================================

print("=" * 70)
print("Q5. Correlation Between Tenure and Churn")
print("=" * 70)

# Convert Churn 'Yes'/'No' into numeric 1/0, as the hint instructs
df["Churn_numeric"] = df["Churn"].map({"Yes": 1, "No": 0})

correlation = np.corrcoef(df["tenure"], df["Churn_numeric"])[0, 1]
print(f"Correlation between Tenure and Churn: {correlation:.3f}\n")

# ANSWER / INTERPRETATION:
# Excel formula: =CORREL(tenure_range, churn_numeric_range)
# In pandas/numpy this is done with np.corrcoef() or df["tenure"].corr(df["Churn_numeric"]).
# The result is typically a NEGATIVE correlation (e.g., around -0.3 to -0.5),
# meaning that as tenure increases, the likelihood of churn decreases.
# In business terms: customers who have stayed longer with the company
# are less likely to leave, while newer customers (low tenure) churn
# more often -- likely because they haven't yet built loyalty, habit, or
# switching costs with the service.

print("=" * 70)
print("All tasks completed successfully.")
print("=" * 70)
