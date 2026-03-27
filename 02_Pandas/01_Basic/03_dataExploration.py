import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# =======================================================================
# head and tail used to select top / bottom n rows from data

# head(n)
# to get top n rows - by default top 5
print("Top 3 Entries")
print(df.head(3))

# tail(n)
# to get bottom n rows - by default top 5
print("Bottom 3 Entries")
print(df.tail(3))


print("======================")
# =======================================================================
# info() - summary of data
# 1 - number of rows and columns
# 2 - column names
# 3 - datatypes of all the data
# 4 - null counts
# 5 - memory usage of dataframe

print("Info about dataset")
print(df.info())


print("======================")
# =======================================================================
