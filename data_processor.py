import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combining dataframes
df = pd.concat([df1, df2, df3], ignore_index=True)

#Filtering for pink morsel
df = df[df["product"].str.lower().fillna("") == "pink morsel"]

#Removing dollar sign from price to allow calculation
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)

#Creating new sales column
df["sales"] = df["quantity"] * df["price"]

# Keeping required columns
df_clean = df[["sales", "date", "region"]]

# Renaming columns
df_clean.columns = ["Sales", "Date", "Region"]

#saving the file
df_clean.to_csv("data/clean_data.csv", index=False)

print(df_clean.head())