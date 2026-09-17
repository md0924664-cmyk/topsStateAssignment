
# Topic: Simple Linear Regression
#
# Requirements:
# pip install pandas matplotlib scikit-learn


# ============================================================
# Question 1
# Given a dataset of YouTube influencers with their number of
# followers (independent variable) and average monthly brand
# deals (dependent variable), identify the dependent and
# independent variables. Explain your reasoning in 2-3 sentences.
# ============================================================

# Answer:
# Independent variable: Number of followers
# Dependent variable: Average monthly brand deals
#
# Reason:
# The number of followers is the independent variable because it
# is used to explain or predict the number of brand deals.
# Average monthly brand deals is the dependent variable because
# it may change based on the influencer's number of followers.


# ============================================================
# Question 2
# Using Excel, Google Sheets, or Python, plot a scatter plot of
# Myntra ad spend (in lakhs) vs. number of app downloads for
# 10 sample data points. Highlight the line of best fit.
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# Sample data
myntra_data = {
    "Ad_Spend_Lakhs": [5, 8, 10, 12, 15, 18, 20, 23, 25, 28],
    "App_Downloads_Thousands": [18, 27, 31, 38, 46, 53, 59, 68, 74, 82]
}

myntra_df = pd.DataFrame(myntra_data)

# Calculate line of best fit using pandas/numpy
x = myntra_df["Ad_Spend_Lakhs"]
y = myntra_df["App_Downloads_Thousands"]

slope, intercept = __import__("numpy").polyfit(x, y, 1)
best_fit = slope * x + intercept

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, label="Sample data")
plt.plot(x, best_fit, linewidth=2, label="Line of Best Fit")
plt.xlabel("Myntra Ad Spend (Lakhs)")
plt.ylabel("App Downloads (Thousands)")
plt.title("Myntra Ad Spend vs. App Downloads")
plt.legend()
plt.grid(True)
plt.show()

# Answer:
# The scatter plot shows a positive relationship: as Myntra's
# advertising spend increases, the number of app downloads also
# generally increases. The straight line represents the line of
# best fit, which summarizes this overall trend.


# ============================================================
# Question 3
# Using Python and scikit-learn, fit a simple linear regression
# model to predict average daily orders on Swiggy based on daily
# advertising spend. Print the slope and intercept and explain
# both in context.
# ============================================================

from sklearn.linear_model import LinearRegression

# Sample Swiggy data
swiggy_data = {
    "Ad_Spend_Lakhs": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    "Daily_Orders": [110, 145, 175, 210, 250, 280, 315, 350, 385, 420]
}

swiggy_df = pd.DataFrame(swiggy_data)

# Independent variable (X) and dependent variable (y)
X = swiggy_df[["Ad_Spend_Lakhs"]]
y = swiggy_df["Daily_Orders"]

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Print coefficient (slope) and intercept
slope = model.coef_[0]
intercept = model.intercept_

print("\n--- Question 3: Swiggy Linear Regression ---")
print("Slope (Coefficient):", round(slope, 2))
print("Intercept:", round(intercept, 2))

# Answer:
# Slope (coefficient):
# The slope tells us how many additional daily orders are
# predicted for every extra 1 lakh spent on advertising.
#
# Intercept:
# The intercept is the model's predicted number of daily orders
# when advertising spend is 0 lakhs.
#
# Note: The intercept is a mathematical model value and may not
# represent a realistic business situation if zero ad spend is
# outside the observed data range.


# ============================================================
# Question 4
# Calculate the R-squared value for the Swiggy regression model
# and interpret what it tells us.
# ============================================================

r_squared = model.score(X, y)

print("\n--- Question 4: R-squared ---")
print("R-squared:", round(r_squared, 4))

# Answer:
# R-squared is the proportion of variation in daily orders that
# is explained by advertising spend in this simple linear
# regression model.
#
# An R-squared value closer to 1 indicates that the model explains
# a large portion of the variation in orders. A value closer to 0
# indicates that advertising spend explains very little of the
# variation.
#
# For this sample dataset, the R-squared value is expected to be
# very close to 1, showing a strong linear relationship in the
# sample data. This does not prove that advertising alone causes
# the increase in orders; other factors may also affect orders.


# ============================================================
# End of Assignment
# ============================================================
