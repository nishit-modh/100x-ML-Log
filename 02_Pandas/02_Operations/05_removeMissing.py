import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", None, "Dev", "Priten", None, "Resma", "Vishwa"],
    "Age": [20, 23, 31, 24, 34, 32, 36, 28],
    "Salary": [50000, 43000, None, 52000, 41000, 43000, 42000, 78000],
    "Performance Score": [70, 80, None, 86, 75, None, None, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame")
print(df)


"""
to remove reows/columns with null values
df.dropna(axis=0, inplace=True)
"""

# remove rows with null values
# df.dropna() or df.dropna(axis=0) - Drop rows with ANY missing values

print("Remover rows with missing value: ")
rows_removed = df.dropna()
print(rows_removed)

# remove columns with null values
# df.dropna(axis=1) - Drop columns with ANY missing values
print("Remover columns with missing value: ")
df.dropna(axis=1, inplace=True)
print(df)