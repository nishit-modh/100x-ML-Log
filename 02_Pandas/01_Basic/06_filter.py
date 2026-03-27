import pandas as pd

"""
To filter 
- select specific columns
- filter rows
- combine multiple conditions
"""

data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev", "Priten", "Diya", "Resma", "Vishwa"],
    "Age": [20, 23, 31, 23, 34, 32, 36, 34],
    "city": [
        "Ahmedabad",
        "Modasa",
        "Ahmedabad",
        "Mahesana",
        "Viramgam",
        "Ahmedabad",
        "Modasa",
        "Modasa",
    ],
    "Salary": [20000, 23000, 34000, 32000, 21000, 43000, 32000, 78000],
    "Performance Score": [70, 80, 76, 86, 75, 96, 83, 75],
}
df = pd.DataFrame(data)

print("Sample Dataframe: ")
print(df)
print("========================")

# ==============================================================
# data frame - 2d // series - 1d
# Selecting columns - will return series not a data frame due to data of single column only
name = df["Name"]
print("Names(Single column series)")
print(name)
print("========================")


# selecting multi column
subset = df[["Name", "Salary"]]
print("Names & Salary(Dataframe with 2 columns)")
print(subset)
print("========================")


# ==============================================================
# Filtering rows - single conditions
young_blood = df[df["Age"] < 30]
print("Young peopel (younger than 30)")
print(young_blood)
print("========================")

# ==============================================================
# multiple conditions
print("========================")
broke_adults = df[(df["Age"] > 30) & (df["Salary"] < 40000)]
print("Broke adult people (Age > 30 + salary < 40K)")
print(broke_adults)
