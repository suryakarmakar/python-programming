import pandas as pd

# Sample data
data1 = {"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]}
data2 = {"ID": [2, 3, 4], "Age": [25, 30, 22]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge data based on the 'ID' column
merged_data = pd.merge(df1, df2, on="ID", how="inner")
print(merged_data)
