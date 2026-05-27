import pandas as pd
import numpy as np
df = pd.read_csv("Building_Permits.csv",low_memory=False)
#Objective: Work with factor-like columns.
#Show all unique values in a column like “Description”.
unique_values = df["Description"].nunique(dropna=True)
#print(unique_values)
#Count frequency of each category with value_counts(normalize=True).
frequency = df["Description"].value_counts(normalize=True)*100
#print(frequency)
#Identify which columns have only one unique value (and drop them).
one_unique_columns = df.columns[df.nunique(dropna=True)==1].tolist()
df = df.drop(columns=one_unique_columns)
#Standardize inconsistent text labels (e.g., replace “Tech”, “Technology”, “tech” → “Technology”).
standardise_labels = df["Existing Use"].str.strip().str.lower().str.title()
#print(standardise_labels)