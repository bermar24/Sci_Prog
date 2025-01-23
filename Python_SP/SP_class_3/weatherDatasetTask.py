import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in Seaborn "tips" dataset
tips = sns.load_dataset('tips')
print("\nHead movies:\n", tips.head())
print("\nColumns movies:\n", tips.columns)

# TODO Violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(data=tips, x='time', y='tip', palette='muted', hue='time', legend=False)
plt.title('Tip Distributions by Time of Day', fontsize=16)
plt.xlabel('Time of Day', fontsize=14)
plt.ylabel('Tip Amount', fontsize=14)
plt.show()

# Add a column for tip percentage
tips['tip_percentage'] = (tips['tip'] / tips['total_bill']) * 100

# Bar plot for average tip percentage by day
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='tip_percentage', errorbar=None, palette='coolwarm', hue='day', legend=False)
plt.title('Average Tip Percentage by Day', fontsize=16)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Tip Percentage (%)', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Scatterplot with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', palette='Set1', alpha=0.8, legend=False)
sns.regplot(data=tips, x='total_bill', y='tip', scatter=False, color='blue', line_kws={"linewidth": 2})
plt.title('Total Bill vs. Tip Amounts', fontsize=16)
plt.xlabel('Total Bill ($)', fontsize=14)
plt.ylabel('Tip Amount ($)', fontsize=14)
plt.grid(linestyle='--', alpha=0.7)
plt.show()