import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev", "Priten", "Savan", "Resma", "Vishwa"],
    "Age": [20, 23, 31, 23, 34, 32, 36, 34],
    "Salary": [50000, 43000, 44000, 52000, 41000, 43000, 42000, 41000],
    "Performance Score": [70, 80, 76, 86, 70, 96, 83, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame: ")
print(df)

"""
Single sort : if age1 == age2 -> sorting will be base on id
multi sort : if age1 == age2 -> sorting based on 2nd sort condition(Salary)...
"""

# Simple sort - based on single column only
# df.sort_values( by="col_name", ascending=True/False, inplace=True)

age_sort = df.sort_values(by="Age", ascending=True)
print("Sorted by age: ")
print(age_sort)

# multi column sort - by=["col_1", "col_2"...] 
# df.sort_values( by=["col_name", "col_name2"], ascending=[True, False], inplace=True)
df.sort_values(by=["Age", "Salary", "Performance Score"], ascending=[True, False, False], inplace=True)
print("Multi Sort: Age(asc), Salary(desc), Performance Score(Desc)")
print(df) 