import pandas as pd

# for reading CSV files
df = pd.read_orc("sales_data_sample.csv", encoding="latin1")
print(df)
print("=================================================================================")

# for reading json
df2 = pd.read_json("sample_Data.json")
print(df2)
print("=================================================================================")

# for reading xlsx files (Excel)
df3 = pd.read_excel("SampleSuperstore.xlsx")
print(df3)