import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\sushm\Downloads\result_rforest.csv")

numeric_cols = ['PassengerId', 'Survived']

sns.pairplot(df[numeric_cols])
plt.suptitle('Pairplot of PassengerId and Predicted Survival', y=1.02)
plt.show()

correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(5, 4))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    fmt=".3f",
    linewidths=0.5,
    linecolor='black',
    cbar_kws={'label': 'Correlation Coefficient'}
)
plt.title('Correlation Heatmap: PassengerId vs. Survived')
plt.tight_layout()
plt.show()