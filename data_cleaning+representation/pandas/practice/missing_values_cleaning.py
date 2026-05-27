import pandas as pd
df = pd.read_csv("Building_Permits.csv",low_memory=False)
#Missing Values
#Objective: Practice identifying and summarizing missing data patterns.
#Which 3 columns have the most missing values?
missing_values = df.isna().sum()
top3_missing_values = (df.isna().sum().sort_values(ascending=False)).head(3)
#print(top3_missing_values)
#Show a full summary of missing counts and percentages (sorted).
missing_percent = df.isna().mean()*100
missing_summary = (pd.DataFrame({"Missing count": missing_values, "Missing percentage" : missing_percent}).sort_values("Missing percentage",ascending=False))
#print(missing_summary.head(10))
#Display rows where any column is missing.
row_of_missing_column = df[df.isna().any(axis=1)]       #axis=1 means row-wise = True if any cell in the row is missing
#print(row_of_missing_column)
#(Bonus) Drop rows missing more than 50% of their columns.
new_df = df.dropna(thresh=len(df.columns) * 0.5)    #dropna by default removes rows that have ANY missing values
                                                    #thresh means "keep rows that have at least this many non-NaN values"
                                                    #thresh = half of the length of the columns
#print(new_df)
