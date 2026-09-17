
# Topic: Online Retail Customer & Sales Analysis

# Note:
# This assignment is designed for Excel using OnlineRetail.csv.
# The formulas and steps below can be used directly in Excel.


# ============================================================
# Question 1
# Open OnlineRetail.csv in Excel and use the Filter feature to
# display only transactions made by customers from 'United Kingdom'.
# Count how many unique CustomerIDs made purchases from the UK.
# ============================================================

# Answer:
#
# Steps in Excel:
# 1. Open OnlineRetail.csv in Excel.
# 2. Select the complete data range.
# 3. Go to Data -> Filter.
# 4. In the Country column, select only "United Kingdom".
# 5. Check the CustomerID column for unique customers.
#
# Excel 365 formula for the unique UK customer count:
#
# =COUNTA(UNIQUE(FILTER(E:E,G:G="United Kingdom")))
#
# IMPORTANT:
# Replace E:E and G:G with the actual CustomerID and Country
# columns in your OnlineRetail.csv if they are in different columns.
#
# Answer format:
# Unique CustomerIDs from United Kingdom = [Enter Excel result]


# ============================================================
# Question 2
# Create a PivotTable to analyze total sales (Quantity * UnitPrice)
# by Country. Identify the top 3 countries by total sales.
# ============================================================

# Answer:
#
# First create a new column named "Sales" in the dataset.
#
# Formula:
# =Quantity*UnitPrice
#
# For example, if Quantity is column D and UnitPrice is column E:
# =D2*E2
#
# Then create a PivotTable:
# 1. Select the full dataset.
# 2. Insert -> PivotTable.
# 3. Put Country in Rows.
# 4. Put Sales in Values and choose Sum.
# 5. Sort Sum of Sales from Largest to Smallest.
# 6. The first three countries are the top 3 countries by sales.
#
# Answer:
# Top 3 countries by total sales:
# 1. [Country 1]
# 2. [Country 2]
# 3. [Country 3]
#
# Note:
# The exact countries depend on the OnlineRetail.csv dataset.


# ============================================================
# Question 3
# Calculate the average order value (total sales per InvoiceNo)
# for all customers. Highlight any InvoiceNo where the order value
# is above Rs. 10,000.
# ============================================================

# Answer:
#
# Step 1: Create a Sales column:
# =Quantity*UnitPrice
#
# Step 2: Calculate total order value for each InvoiceNo.
# One Excel 365 approach is:
#
# =SUMIF($A:$A,A2,$F:$F)
#
# Replace:
# A:A = InvoiceNo column
# F:F = Sales column
#
# Step 3: Calculate the average order value:
#
# =AVERAGE(G:G)
#
# Replace G:G with your Order Value column.
#
# Step 4: Highlight orders above Rs. 10,000:
# 1. Select the Order Value column.
# 2. Home -> Conditional Formatting.
# 3. Highlight Cells Rules -> Greater Than.
# 4. Enter 10000.
# 5. Choose a highlight format and click OK.
#
# Answer:
# Average Order Value = [Enter Excel result]
# InvoiceNos above Rs. 10,000 = [Enter highlighted InvoiceNos]


# ============================================================
# Question 4
# Perform a t-test in Excel to compare the average order value
# between customers from France and Germany. State whether the
# difference is statistically significant at the 0.05 level.
# ============================================================

# Answer:
#
# Step 1:
# Filter or separate the Order Value data for:
# - Country = France
# - Country = Germany
#
# Step 2:
# Go to:
# Data -> Data Analysis -> t-Test: Two-Sample Assuming Unequal Variances
#
# Step 3:
# Select the France order-value range as Variable 1 Range.
# Select the Germany order-value range as Variable 2 Range.
#
# Step 4:
# Set Hypothesized Mean Difference = 0.
# Set Alpha = 0.05.
#
# Step 5:
# Check the P(T<=t) two-tail value.
#
# Interpretation:
# If the two-tailed p-value < 0.05:
#   The difference is statistically significant.
#
# If the two-tailed p-value >= 0.05:
#   The difference is not statistically significant.
#
# Answer format:
# France average order value = [Enter result]
# Germany average order value = [Enter result]
# Two-tailed p-value = [Enter result]
# Conclusion = [Significant / Not Significant at 0.05]


# ============================================================
# Question 5
# Use ChatGPT or Copilot to generate a summary of key customer
# purchasing patterns observed from the analysis and copy it into
# a new Excel sheet named "Insights".
# ============================================================

# Answer:
#
# Sample Insights Summary:
#
# "The analysis of the Online Retail dataset shows differences in
# purchasing activity across countries. Some countries contribute
# a larger share of total sales, indicating stronger customer
# purchasing activity in those markets. The average order value
# helps identify the typical spending level per invoice, while
# invoices above Rs. 10,000 represent relatively high-value orders.
# Comparing France and Germany using a two-sample t-test helps
# determine whether their average order values differ
# statistically. Sales may also vary across months, so examining
# invoice dates can help identify seasonal purchasing patterns.
# These observations should be interpreted together with factors
# such as customer count, order frequency, product mix, and
# transaction volume."
#
# Excel task:
# 1. Create a new worksheet.
# 2. Rename it to "Insights".
# 3. Copy and paste the summary above into the sheet.
# 4. Add your actual results from Questions 1-4 for a
#    dataset-specific summary.


# ============================================================
# FINAL SUBMISSION CHECKLIST
# ============================================================
#
# [ ] OnlineRetail.csv opened in Excel
# [ ] UK transactions filtered
# [ ] Unique UK CustomerIDs counted
# [ ] Sales = Quantity * UnitPrice calculated
# [ ] Country PivotTable created
# [ ] Top 3 countries identified
# [ ] Order Value calculated per InvoiceNo
# [ ] Orders above Rs. 10,000 highlighted
# [ ] France vs Germany unequal-variance t-test completed
# [ ] p-value compared with 0.05
# [ ] Insights worksheet created
#
# END OF ASSIGNMENT
