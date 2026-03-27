import pandas as pd

"""
Basis attributes can be used to get basic but useful info quickly!
this are attributes not methods
like - 
1. Number of columns and rows - shape
2. names of columns - columns
"""

df = pd.read_json("sample_Data.json")
print(df)

print(f"Shape of df: {df.shape}")
print(f"Columns of df: {df.columns}")