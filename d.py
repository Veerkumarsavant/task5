import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\sushm\Downloads\result_rforest.csv")
passenger_id = df['PassengerId']
survived = df['Survived']

plt.figure(figsize=(7, 2))
sns.histplot(passenger_id, kde=True, bins=30, color='darkgreen')
plt.title('Histogram of PassengerId')
plt.xlabel('Passenger ID')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 3))
sns.boxplot(x=passenger_id, color='salmon')
plt.title('Boxplot of PassengerId')
plt.xlabel('Passenger ID')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 3))
sns.scatterplot(
    x=passenger_id,
    y=survived,
    hue=survived,
    palette=['lightcoral', 'skyblue'],
    legend=False
)
plt.yticks([0, 1], ['Died (0)', 'Survived (1)'])
plt.title('Scatterplot of Predicted Survival vs. PassengerId')
plt.xlabel('Passenger ID')
plt.ylabel('Predicted Survival Status')
plt.tight_layout()
plt.show()