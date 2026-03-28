import pandas as pd

data = {"time": [10, 20, 30, 40, 50, 60], "price": [500, None, None, 2000, 2500, 3000]}

df = pd.DataFrame(data)
print("Befor Interpolation")
print(df)

# interpolate() - Filles very relevent data based on selected method
# df["value"].interpolate(method="m_name", axis)

df["price"] = df["price"].interpolate(method="linear")
print("Interpolated Data: ")
print(df)