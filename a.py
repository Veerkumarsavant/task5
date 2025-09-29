import pandas as pd

file_url =r"C:\Users\sushm\Downloads\result_rforest.csv"
try:
    df = pd.read_csv(file_url)
    print("Data Info (df.info())")
    df.info()

    print("\n" + "=" * 50 + "\n")
    print("Descriptive Statistics (df.describe(include='all'))")
    description = df.describe(include="all")
    print(description)

    print("\n" + "=" * 50 + "\n")
    print("Value Counts (Categorical/Low-Cardinality)")
    value_counts = {}
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].nunique() < 20:
            value_counts[col] = df[col].value_counts().head(10)

    for col, counts in value_counts.items():
        print(f"\nValue Counts for Column: **{col}**")
        print(counts)

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure or replace the URL with a valid file path.")