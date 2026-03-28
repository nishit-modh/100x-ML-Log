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

# this are some og the Aggregate functions
avg_salary = df["Salary"].mean()
max_salary = df["Salary"].max()
min_salary = df["Salary"].min()
sum_salary = df["Salary"].sum()

print("Average salary: ", avg_salary)
print("Max salary: ", max_salary)
print("Min salary: ", min_salary)
print("Sum of all salaries: ", sum_salary)