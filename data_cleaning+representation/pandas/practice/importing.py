import pandas as pd
#Read the CSV into df and make sure missing values (blank fields like Cabin) become NaN. Print df.shape, df.head(), and df.isna().sum().
#Import the same CSV but parse PassengerId as an integer index (set it as index while reading or right after). Verify it’s unique.
#Read the CSV and enforce dtypes: Survived and Pclass as integers, Sex and Embarked as category/object, Fare as float. Show df.dtypes and fix any mismatches.
df = pd.read_csv("../titanic_passengers.csv", index_col="PassengerId")

#print(df.shape)
#print(df.head())
#print(df.isna().sum())      #Shows number of missing values
print(df.dtypes)

df["Survived"] = df["Survived"].astype(int)
df["Pclass"] = df["Pclass"].astype((int))
df["Sex"] = df["Sex"].astype(object)
df["Embarked"] = df["Embarked"].astype(object)
df["Fare"] = df["Fare"].astype(float)
#print(df.to_string())