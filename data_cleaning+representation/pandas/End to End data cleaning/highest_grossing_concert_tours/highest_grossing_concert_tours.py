import pandas as pd
df = pd.read_csv("highest_grossing_concert_tours.csv")

#CLEAN HEADERS
#print(df.columns.to_list())
df = df.rename(columns={
    "Actual\xa0gross":"Actual Gross",
    "Adjusted\xa0gross (in 2022 dollars)":"Adjusted Gross (2022 dollars)"
})
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")
#print("FIX APPLIED")
#print(df.columns.to_list())


#CLEAN MONEY COLUMNS TO REMOVE INCONSISTENCIES
money_cols = ["actual_gross","adjusted_gross_(2022_dollars)","average_gross"]
for col in money_cols:
    df[col] = (df[col].astype(str).str.replace("$","",regex=False).str.replace(",","",regex=False).str.replace('"','',regex=False))
    df[col] = pd.to_numeric(df[col], errors="coerce")
#print(df[money_cols])

#CLEAN TOUR TITLE COLUMN
fix_tour_titles = {
    "The Eras Tour †":"The Eras Tour",
    "Sticky & Sweet Tour ‡[4][a]":"Sticky and Sweet Tour",
    "Summer Carnival †":"Summer Carnival",
    "The Monster Ball Tour *":"The Monster Ball Tour",
    "Living Proof: The Farewell Tour ‡[21][a]":"Living Proof The Farewell Tour"
}
df["tour_title"] = df["tour_title"].replace(fix_tour_titles).str.lower().str.replace(" ","_")
#print(df["tour_title"])


#CLEAN ARTIST NAMES
df["artist"] = df["artist"].str.strip().str.lower().str.replace(" ","_")
fix_beyonce_name = {
    "beyoncé" : "beyonce"
}
df["artist"] = df["artist"].replace(fix_beyonce_name)
#print(df["artist"])

#ORGANISE START AND END YEAR COLUMNS
df["year(s)"] = df["year(s)"].astype(str).replace("[–]","-", regex=True).str.strip()
df[["start_year","end_year"]] = df["year(s)"].str.split("-", n=1, expand=True)
df["end_year"] = df["end_year"].fillna(df["start_year"])
df = df.drop(columns="year(s)")
#print(df.columns.to_list())


#REMOVE SQUARE BRACKETS AND REPLACE WITH COMMAS
df["peak"] = df["peak"].str.replace("[",",", regex=False).str.replace("]","", regex=False)
df["all_time_peak"] = df["all_time_peak"].str.replace("[",",", regex=False).str.replace("]","", regex=False)
df["ref."] = (df["ref."].fillna("").astype(str).str.replace(r"\]\[",",", regex=True).str.replace(r"[\[\]]","", regex=True).str.strip())
print(df.to_string())

df.to_csv("highest_grossing_concert_tours.csv", index=False)


