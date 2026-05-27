import pandas as pd
import numpy as np

df = pd.read_csv("dirty_cafe_sales.csv")

#CLEAN HEADERS
#print(df.columns.to_list())
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
#print("FIX APPLIED")
#print(df.columns.to_list())

#CLEAN to replace UNKNOWN & ERROR to NaN
df = df.replace(["UNKNOWN","ERROR"],np.nan,regex=True)
df = df.dropna()
#print(df)

#FIXING DTYPES
#print(df[["quantity","price_per_unit","total_spent"]])
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price_per_unit"] = pd.to_numeric(df["price_per_unit"], errors="coerce")
df["total_spent"] = pd.to_numeric(df["total_spent"], errors="coerce")
#print(df.dtypes)

#FIXING IMBALANCED TOTALS (Quantity * Price Per Unit ≠ Total Spent)
df["calculated_total"] = df["quantity"] * df["price_per_unit"]
df["imbalanced_total"] = np.where(abs(df["calculated_total"] - df["total_spent"]) > 0.01, True, False)
imbalanced_rows = df[df["imbalanced_total"] == True]
#print(imbalanced_rows.sum())

#DATA STANDARDISATION
#print(df['payment_method'].value_counts(normalize=True)*100)
df['payment_method'] = df['payment_method'].str.strip().str.lower().str.replace(" ","_")

#print(df['location'].value_counts(normalize=True))

#print(df['item'].value_counts())

#DUPLICATES & FORMAT ISSUES
#print(df['transaction_id'].duplicated().value_counts(normalize=True)*100)
#print(df['transaction_date'].to_string())
#df['transaction_date'] = pd.to_datetime(df['transaction_date'], dayfirst=True, errors="coerce")
#print(df['transaction_date'].to_string())

print(df.to_string())


