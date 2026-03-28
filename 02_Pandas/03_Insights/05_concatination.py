import pandas as pd

df_region1 = pd.DataFrame({
    "coustomer_id" : [1,2,3],
    "Names": ["Dev", "Joe", "Carl"]
})

df_region_2 = pd.DataFrame({
    "coustomer_id" : [4,5],
    "Names": ["Dona", "Bella"]
})

# verticle concat
df_concat_verticle = pd.concat([df_region1, df_region_2], ignore_index=True)
print(df_concat_verticle)
print("===========================")

# horizontal concat
df_concat_horizontal = pd.concat([df_region1, df_region_2],ignore_index=True, axis=1)
print(df_concat_horizontal)