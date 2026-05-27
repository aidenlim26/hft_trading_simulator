import pandas as pd
from pandas import Int64Dtype
from unicodedata import category

df = pd.read_csv("titanic_passengers.csv")

#Missing values check
#Which 3 columns have the most missing values?
#Show the missing count for every column.
#missing = df.isna().sum().sort_values(ascending=False)      #sorts from largest to smallest
#print(missing.head(3))      #shows the top 3 columns with most missing values

#Fix dtypes
#Convert Survived and Pclass to integers, Fare to float, and Sex + Embarked to category/object.
#Print df.dtypes before and after.
#print(df.dtypes)
df["Survived"] = pd.to_numeric(df["Survived"], errors="coerce").astype(int)
df["Pclass"] = pd.to_numeric(df["Pclass"], errors="coerce").astype(int)
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce").astype(int)

df["Sex"] = df["Sex"].astype("category")
df["Embarked"] = df["Embarked"].astype("category")
#print(df.dtypes)

#Clean Embarked
#How many missing Embarked values are there?
#Fill missing Embarked with the most common port (mode).
#Show Embarked.value_counts(normalize=True) after cleaning.
missing_embarked = df["Embarked"].isna().sum()
#print(missing_embarked)
#print(df.to_string())
#print(df["Embarked"].value_counts())
mode = df["Embarked"].mode(dropna=True)[0]
#print(mode)
df["Embarked"] = df["Embarked"].fillna(mode)
#print(df["Embarked"].value_counts(normalize=True))

#Clean Age
#How many missing Age values are there?
#Fill missing Age with the median age.
#Print the new min/max age and confirm no missing Age.
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
missing_age = df["Age"].isna().sum()
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
new_missing_age = df["Age"].isna().sum()
#rint(f"Old missing ages: {missing_age}")
#print(f"New missing ages: {new_missing_age}")
max_age = df["Age"].max()
min_age = df["Age"].min()
#print(f"Max age: {max_age}")
#print(f"Min age: {min_age}")

#Duplicates + basic validation
#Are there any duplicate PassengerId values? If yes, remove duplicates (keep first).
duplicated_age = df["Age"].duplicated().sum()
#print(f"Duplicated ages = {duplicated_age}")
df = df.drop_duplicates(subset=["Age"],keep="first")
#print(df)
#print("New duplicated ages:", df["Age"].duplicated().sum())
#Check for any impossible values: Age < 0 or Fare < 0. How many rows are invalid?
# make sure they're numeric (safe if already done)
df["Age"]  = pd.to_numeric(df["Age"], errors="coerce")
df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
invalid_mask = (df["Age"] < 0) | (df["Fare"] < 0)
invalid_rows = df[invalid_mask]
print("Invalid rows (Age < 0 or Fare < 0):", invalid_rows.shape[0])




