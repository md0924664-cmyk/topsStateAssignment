
# Questions + Answers

# Requirements:
# pip install pandas scipy seaborn matplotlib


# ============================================================
# Question 1
# Download/create a small dataset of 10-15 songs with features
# like danceability, energy, and popularity, then calculate the
# Pearson correlation coefficient between danceability and
# popularity using pandas.
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr

# Answer:
# A small sample dataset is created manually below.
songs_data = {
    "Song": [
        "Song A", "Song B", "Song C", "Song D", "Song E",
        "Song F", "Song G", "Song H", "Song I", "Song J",
        "Song K", "Song L"
    ],
    "Danceability": [0.82, 0.65, 0.91, 0.54, 0.76, 0.88,
                     0.60, 0.72, 0.95, 0.48, 0.80, 0.69],
    "Energy": [0.78, 0.61, 0.89, 0.45, 0.72, 0.91,
               0.55, 0.68, 0.94, 0.40, 0.83, 0.64],
    "Popularity": [85, 64, 92, 48, 76, 88,
                   55, 70, 96, 42, 81, 67]
}

songs_df = pd.DataFrame(songs_data)

# Pearson correlation using pandas corr()
pearson_correlation = songs_df["Danceability"].corr(
    songs_df["Popularity"], method="pearson"
)

print("\n--- Question 1: Pearson Correlation ---")
print(songs_df)
print("Pearson correlation (Danceability vs Popularity):",
      round(pearson_correlation, 4))

# Interpretation:
# The Pearson correlation is positive and close to 1 for this
# sample dataset. This means that songs with higher danceability
# generally tend to have higher popularity in this sample.
# Correlation shows an association, not proof that danceability
# causes popularity.


# ============================================================
# Question 2
# Given IPL players with total runs and Instagram followers,
# use scipy.stats.spearmanr to calculate Spearman correlation
# and interpret whether higher runs generally mean more followers.
# ============================================================

ipl_data = {
    "Player": [
        "Player A", "Player B", "Player C", "Player D", "Player E",
        "Player F", "Player G", "Player H", "Player I", "Player J"
    ],
    "Total_Runs": [5200, 4300, 6100, 3500, 4700, 2900, 5500, 3900, 3200, 6800],
    "Instagram_Followers_Millions": [
        18.5, 12.2, 25.0, 8.4, 15.6,
        5.8, 20.1, 10.5, 7.2, 29.0
    ]
}

ipl_df = pd.DataFrame(ipl_data)

spearman_correlation, p_value = spearmanr(
    ipl_df["Total_Runs"],
    ipl_df["Instagram_Followers_Millions"]
)

print("\n--- Question 2: Spearman Correlation ---")
print(ipl_df)
print("Spearman correlation:", round(spearman_correlation, 4))
print("P-value:", round(p_value, 6))

# Interpretation:
# A positive Spearman correlation means that players with higher
# total runs generally tend to have more Instagram followers in
# this sample.
# However, followers can also depend on factors such as fame,
# team, country, endorsements, and social-media activity.
# Therefore, runs alone do not necessarily cause more followers.


# ============================================================
# Question 3
# Create a correlation matrix for three Flipkart product features:
# price, user rating, and number of reviews using pandas corr().
# ============================================================

flipkart_data = {
    "Price": [499, 799, 999, 1299, 1599, 1999, 2499, 2999, 3499, 3999],
    "User_Rating": [3.8, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.2, 4.6, 4.7],
    "Number_of_Reviews": [120, 210, 350, 420, 650, 800, 1050, 920, 1350, 1600]
}

flipkart_df = pd.DataFrame(flipkart_data)

corr_matrix = flipkart_df[[
    "Price", "User_Rating", "Number_of_Reviews"
]].corr()

print("\n--- Question 3: Flipkart Correlation Matrix ---")
print(corr_matrix)

# Answer:
# The correlation matrix shows the pairwise relationship between
# price, user rating, and number of reviews.
# Values close to +1 indicate a strong positive relationship,
# values close to -1 indicate a strong negative relationship,
# and values close to 0 indicate little linear relationship.


# ============================================================
# Question 4
# Visualize the Flipkart correlation matrix as a heatmap using
# seaborn's heatmap(), with annotations and a color bar.
# ============================================================

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    cbar=True,
    fmt=".2f",
    linewidths=0.5
)

plt.title("Flipkart Product Features Correlation Heatmap")
plt.tight_layout()
plt.show()

# Answer:
# The heatmap provides a visual representation of the correlation
# matrix. The annotations display the exact correlation values,
# while the color bar helps identify the strength and direction
# of the relationships.


# ============================================================
# Question 5
# List two potential pitfalls when interpreting correlation
# coefficients in data from real apps like Zomato or YouTube.
# Give a short example for each.
# ============================================================

# Answer:
#
# Pitfall 1: Correlation does not mean causation.
# Example:
# On YouTube, video length and total views might be positively
# correlated. This does not mean that making every video longer
# will automatically increase views. Popular creators may make
# both longer videos and receive more views because of their
# existing audience.
#
# Pitfall 2: Confounding variables can create a misleading
# correlation.
# Example:
# On Zomato, restaurant ratings and the number of orders may be
# positively correlated. However, location, restaurant popularity,
# discounts, cuisine type, and delivery availability could affect
# both ratings and orders. Therefore, the correlation between
# ratings and orders does not necessarily mean ratings alone
# caused the higher number of orders.


# ============================================================
# END OF ASSIGNMENT
# ============================================================
