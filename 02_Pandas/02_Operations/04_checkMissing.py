import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", None, "Dev", "Priten", None, "Resma", "Vishwa"],
    "Age": [20, 23, 31, None, 34, 32, 36, None],
    "Salary": [50000, 43000, None, 52000, 41000, 43000, 42000, 78000],
    "Performance Score": [70, 80, None, 86, 75, None, None, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame")
print(df)

# isnull() - to check which values are missing
print("Is value missing?: ")
print(df.isnull())

# total values missing in each column
print("Column wise missing value count: ")
print(df.isnull().sum())