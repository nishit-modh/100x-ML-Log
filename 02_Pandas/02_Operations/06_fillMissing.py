import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", None, "Dev", "Priten", None, "Resma", "Vishwa"],
    "Age": [20, 23, 31, 24, 34, 32, 36, 28],
    "Salary": [50000, 43000, None, 52000, 41000, 43000, 42000, 78000],
    "Performance Score": [None, 80, None, 86, 75, None, None, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame")
print(df)

# fillna(value, inplace=True)
print("Filled in Performance Score & salary: ")
df["Salary"] = df["Salary"].fillna(0)
df["Performance Score"] = df["Performance Score"].fillna(df["Performance Score"].mean())
print(df)