import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev", "Priten", "Savan", "Resma", "Vishwa"],
    "Age": [20, 23, 31, 23, 34, 32, 36, 34],
    "Salary": [20000, 23000, 34000, 32000, 21000, 43000, 32000, 78000],
    "Performance Score": [70, 80, 76, 86, 75, 96, 83, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame")
print(df)

# insertion by assingnmnet - Adds as last column
# USe when don't need the data in certain column
df["bonus"] = df["Salary"] / 2
print("Bonus added")
print(df)

# using insert() method
# inser(col_index, col_name, data)
df.insert(0, "Employee id", [11,12,13,15,16,17,None,18])# None -> Gives NaN
print("Employee id added")
print(df)