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

# To remove data - drop() method
# df.drop(columns = ["col_name_1", "col_name_2"] , insplace=True)
# inplce=True -> Removal in orignal dataFrame
# inplce=False -> Removal of data in new copy

df.drop(columns=["Performance Score", "Age"] , inplace=True)
print("Removed Performance Score and Age")
print(df)