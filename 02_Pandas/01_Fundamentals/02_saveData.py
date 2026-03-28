import pandas as pd

# we will save this data in different formats
data = {
    "Name": ["Nishit", "Dhruvil", "Dinal", "Dev"],
    "Age": [20, 23, 21, 23],
    "city": ["Ahmedabad", "Modasa", "Ahmedabad", "Mahesana"],
}

# we need to conver this to DataFrame
df = pd.DataFrame(data)
print(df)

# converting data to csv - index false to remove default index
df.to_csv("output.csv", index=False)

# converting data to excel
df.to_excel("output.xlsx")

# converting data to json
df.to_json("output.json", index=False)
