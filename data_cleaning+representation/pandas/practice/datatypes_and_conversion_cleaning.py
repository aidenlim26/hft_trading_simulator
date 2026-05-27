import pandas as pd
import numpy as np
from unicodedata import category

df = pd.read_csv("Building_Permits.csv",low_memory=False)
#Objective: Get familiar with dtype conversions and their effects.
#Print all column dtypes.
print("Before transformation:",df.dtypes)
#Convert numeric columns stored as objects (e.g., "Volume", "Price") using pd.to_numeric(errors="coerce").
df["Permit Number"] = pd.to_numeric(df["Permit Number"],errors="coerce").astype(float)
df["Block"] = pd.to_numeric(df["Block"],errors="coerce").astype(float)
#print(df.dtypes)
#Convert date columns to datetime.
df["Permit Creation Date"] = pd.to_datetime(df["Permit Creation Date"],errors="coerce") #from object to a date e.g. (2016-05-27)
#print(df["Permit Creation Date"])
#Ensure categorical columns (e.g., “Sector”, “Exchange”) are set to category.
df["Street Suffix"] = df["Street Suffix"].astype("category")       #dtype "category" is used when there's limited number of unique e.g. blood type
#print(df["Street Suffix"])
#Print dtypes before and after transformation.
print("After transformation: ",df.dtypes)