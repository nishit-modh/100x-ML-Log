import pandas as pd

df_customers = pd.DataFrame({
    "customer_id" : [1,2,3,4,5],
    "Name" : ["Henry", "Carl", "Mark", "Joe", "Bella"]
})

df_orders = pd.DataFrame({
    "customer_id" : [1,6,3,7,5],
    "order" : [200,400,600,100,900]
})

# general syntax
# df_merged = pd.merge(df_1, df_2, on="common_Col_name", how="join_type")

# 1. Inner join -> data with coomon col id
df_inner = pd.merge(df_customers, df_orders, on="customer_id", how="inner")
print("Inner join: ")
print(df_inner)

# 2. outer join -> complete merge (Not matching values - NaN)
df_outer = pd.merge(df_customers, df_orders, on="customer_id", how="outer")
print("Outer join: ")
print(df_outer)

# 3. left join -> Keeps all values in left (Non mathing values filled with NaN)
df_left = pd.merge(df_customers, df_orders, on="customer_id", how="left")
print("Left join: ")
print(df_left)

# 4. right join -> Keeps all values in left (Non mathing values filled with NaN)
df_right = pd.merge(df_customers, df_orders, on="customer_id", how="right")
print("Right join: ")
print(df_right)

# cross Join : df_1 m rows | df_2 n rows -> GIVES m*n rows
df_cross = pd.merge(df_customers, df_orders, how="cross")
print("Cross join: ")
print(df_cross)