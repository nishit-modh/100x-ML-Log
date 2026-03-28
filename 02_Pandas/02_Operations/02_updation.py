import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev", "Priten", "Savan", "Resma", "Vishwa"],
    "Age": [20, 23, 31, 23, 34, 32, 36, 34],
    "Salary": [50000, 43000, 44000, 52000, 41000, 43000, 42000, 78000],
    "Performance Score": [70, 80, 76, 86, 75, 96, 83, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame")
print(df)

# for updating whole column at once
# lets reduce every performnace score by 20
print("Updated data - Reduced Performance Sore by 20")
df["Performance Score"] = df["Performance Score"] - 20
print(df)



# .loc[] - For updating a value of a specific row
# ================================================
# for updating value selected of selected rows
# df.loc[row_index, "col_name"] = new_value
# let's update Performance Score for Nishit and increase Salary of Dhruvil by 100000
df.loc[0, "Performance Score"] = 99
df.loc[1, "Salary"] = df.loc[1, "Salary"] + 100000
print("Updated data - Nishit Per Score & Dhruvil Salary")
print(df)