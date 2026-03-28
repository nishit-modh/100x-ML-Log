import pandas as pd

data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev", "Priten", "Savan", "Resma", "Vishwa"],
    "Age": [20, 24, 26, 20, 24, 30, 30, 24],
    "Salary": [50000, 30000, 30000, 50000, 40000, 50000, 40000, 40000],
    "Performance Score": [70, 70, 75, 85, 70, 95, 80, 75],
}

df = pd.DataFrame(data)

print("Orignal DataFrame: ")
print(df)
print("============================")

# groupby - single group
sal_age = df.groupby(["Age"])["Salary"].mean()
print("Mean salary as per age: ")
print(sal_age)

max_sal_age = df.groupby(["Age"])["Salary"].max()
print("Max salary in each age: ")
print(max_sal_age)

# groupby - multi grouping
group_age_name = df.groupby(["Age","Performance Score","Name"])["Salary"].max()
print(group_age_name)

group_salary_age = df.groupby(["Salary", "Age"])["Performance Score"].mean()
print(group_salary_age)