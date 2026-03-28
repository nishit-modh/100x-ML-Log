import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev", "Priten", "Diya", "Resma", "Vishwa"],
    "Age": [20, 23, 21, 23, 34, 32, 23, 34],
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

print("Sample Dataframe")
print(df)

print("Descriptive Statastics")
print(df.describe())
