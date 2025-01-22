import matplotlib.pyplot as plt
import seaborn as sns


# TODO Matplotlib
#  provides low-level control for creating basic visualizations.

# Basic Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label='Linear Growth')
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# TODO Seaborn
#  simplifies statistical visualization and aesthetics.
# Sample Data
tips = sns.load_dataset('tips')

# Distribution Plot
sns.histplot(tips['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

# Box Plot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title("Boxplot of Total Bill by Day")
plt.show()

# Customizing and Styling Plots
sns.set_theme(style="whitegrid")
sns.barplot(x='day', y='total_bill', data=tips, hue='day', palette="muted", legend=False)
plt.title("Bar Plot with Custom Styling")
plt.show()

# TODO Subplots and Multi-Panel Figures
fig, ax = plt.subplots(2, 1, figsize=(8, 6))
# Line Plot
ax[0].plot(x, y, label='Linear')
ax[0].set_title('Subplot 1: Line Plot')
# Bar Plot
ax[1].bar(x, y, color='orange')
ax[1].set_title('Subplot 2: Bar Plot')
plt.tight_layout()
plt.show()