import pandas as pd
import numpy as np

df = pd.read_csv("marketing_campaign.csv")

#CLEAN HEADERS
#print(df.columns.to_list())
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
#print("FIX APPLIED")
#print(df.columns.to_list)


#TYPE CONVERSION & CURRENCY CLEANING
dirty_spend_mask = df["spend"].astype(str).str.contains(r'\$')
#print((df.loc[dirty_spend_mask,["campaign_id","spend"]]).head(3))
#REMOVING THE "$" SO THAT IT'S EASIER TO AGGREGATE NUMBERS
df["spend"] = df["spend"].astype(str).str.replace(r'[^\d.-]',"", regex=True)       #replace anything that isnt a digit, decimal, or minus with nothing
                                                                                   #"^" means anything not in this list ...
                                                                                   #"\d" means any digit, "." any dot, "-"any minus sign replace with ""
df["spend"] = pd.to_numeric(df["spend"], errors="coerce")
#print("FIX APPLIED")
#print((df.loc[dirty_spend_mask,["campaign_id","spend"]]).head(3))


#CATAGORICAL TYPOS
#print(df["channel"].unique())
fix_channel_titles = {
    "TikTok":"Tiktok",
    "E-mail":"Email",
    "Gogle":"Google",
    "Tik_Tok":"Tiktok",
    "Insta_gram":"Instagram",
    "Facebok":"Facebook"
}
df["channel"] = df["channel"].replace(fix_channel_titles)
#print("FIX APPLIED")
#print(df["channel"].unique())


#HANDLING MIXED BOOLEANS
#print(df["active"].unique())
fix_active_booleans = {
    "Y":"True",
    "0":"False",
    "No":"False",
    "Yes":"True",
    "1":"True",
}
df["active"] = df["active"].map(fix_active_booleans).fillna(False).astype(bool)
#print("FIX APPLIED")
#print(df["active"].unique())
#print(df["active"])


#DATA PARSING
#print(df["start_date"].dtypes)
#df["start_date"] = pd.to_datetime(df["start_date"], dayfirst=True, errors="coerce")
#df["end_date"] = pd.to_datetime(df["end_date"], dayfirst=True, errors="coerce")
#print("FIX APPLIED")
#print(df["start_date"].dtypes)


#LOGICAL INTEGRITY (CLICKS VS IMPRESSIONS)
#print(df.columns.to_list())
df = df.loc[:, ~df.columns.duplicated()]
impossible_mask = df["clicks"] > df["impressions"]
#print(df.loc[impossible_mask, ["campaign_id","clicks","impressions"]].head(3))


#HANDLING OUTLIERS (WINSORIZING)
Q1 = df["spend"].quantile(0.25)
Q3 = df["spend"].quantile(0.75)
interquantile_range = Q3-Q1
upper_limit = Q3 + (interquantile_range * 3)     #upper limit is 3x the average range of variation
#print(upper_limit)
outlier_mask = df["spend"] > upper_limit
#print(df.loc[outlier_mask,["campaign_id","spend"]].head(3))
#print("FIX APPLIED")
df.loc[outlier_mask,"spend"] = upper_limit
#print(df.loc[outlier_mask,["campaign_id","spend"]].head(3))


#STRING PARSING (FEATURE EXTRACTION)
print(df["campaign_name"].head(3))
df["season"] = df["campaign_name"].str.extract(r"Q\d_([^_]+)_")
print("FIX APPLIED")
print(df[["campaign_name","season"]].head(3))




