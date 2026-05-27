import pandas as pd
#Data cleaning = the process of fixing/removing:
#                               1. incomplete, incorrect, or irrelevant data
#                               2. ~75% of work done w/ pandas is data cleaning

df = pd.read_csv("IRIS_dataset.csv")

# 1. Drop irrelevant columns
#df = df.drop(columns=["petal_length","petal_width"])    #make it df = ... to reassign it and make sure changes are saved

# 2. Handle missing data
#df = df.dropna(subset=["Type2"])   #dropna is "drop not available"
                                    #inside subset[], u add the name of the column that has missing data
                                    #if theres missing data, the entire row would be deleted
#df = df.fillna({"Type2":"None"})   #fillna is "fill not available"
                                    #inside the function u add a dictionary
                                    #inside the dictionary the key is the column name
                                    #and the value is the string u replace the missing data with

# 3. Fix inconsistent values
df["species"] = df["species"].replace({"Iris-setosa":"SETOSA"})         #df[], select column name inside brackets
                                                                        #replace function
                                                                        #inside function add a dictionary
                                                                        #dictionary, key=current name
                                                                        #value=what u want to replace it with
                                                                        #you can add multiple things to change in the dictionary

df = df.rename(columns={                                                #Use .rename() to rename column headers
    "Actual\xa0gross": "Actual Gross",
    "Adjusted\xa0gross (in 2022 dollars)": "Adjusted Gross (2022 dollars)"
})

df["active"] = df["active"].map(fix_active_booleans).fillna(False).astype(bool)  #Map function is different as it returns NaN for values not found in the dictionary
                                                                                 #Good for booleans

# 4. Standardise text
df["species"] = df["species"].str.strip()        #Removes all spaces before the words
df["species"] = df["species"].str.lower()        #Make all values in the column lower case
df["species"] = df["species"].str.title()        #Make only the first value capital, everything else lower
dirty_spend_mask = df["spend"].astype(str).str.contains(r'\$') #If the string contains "$"

# 5. Fix data types
#df["Legendary"] = df["Legendary"].astype(bool)  #astype function changes the datatype

# 6. Duplicate values
#ONE COLUMN
duplicated_values = df["species"].duplicated(keep="first")  #keep="first" marks everything as false apart from duplicated values, but the first original value is false
#MULTIPLE COLUMNS
duplicated_values1 = df.duplicated(subset=["species","petal_width","petal_length"], keep="first")     #subset = used to select multiple columns
df = df.drop_duplicates()           #Deletes all duplicate rows

# 7. Sorting values from largest to smallest
s = pd.Series([10,2,7], index=["A","B","C"])
sortedvalues = s.sort_values(ascending=False)       #".sort_values(ascending=False)" sorts from largest to smallest
#print(sortedvalues)

# 8. Converting values to int/float
df1 = pd.read_csv("titanic_passengers.csv")
#print(df1.dtypes)
df1["Cabin"] = pd.to_numeric(df1["Cabin"],errors="coerce")  #errors="coerce" means if there's any errors would just show as "NaN"
#print(df1.to_string())
#print(df1.dtypes)

# 9. Finding the most frequent value = .mode()
mode = df1["Embarked"].mode()[0]      #The [0] is just to get rid of the index
print(mode)
#print(df.to_string())

# 10. Coverting values to a date (datetime)
df["Permit Creation Date"] = pd.to_datetime(df["Permit Creation Date"], dayfirst=True, errors="coerce") #from object to a date e.g. (2016-05-27)
                                                                        #dayfirst=True means its in DD/MM/YYYY instead of the default MM/DD/YYYY
# 11. Finding unique values
unique_values = df["Description"].unique()  #shows all the unique values
unique_values_count = df["Description"].nunique(dropna=True)        #Counts number of unique values sort of like .sum()

# 12. Extracting text from a string in a column
df["Name"].str.extract(r",^\s*([A-Za-z]+)\.", expand=False)         #"," = where does the extraction begin from? extraction starts after the comma
                                                                    #"^" = start of the string
                                                                    #"\s*" = optional spaces at the beginning
                                                                    #"([A-Za-z]+)" = capture one or more letters (this is what you want)
                                                                    #"\." = a literal dot . (dot is special in regex, so we escape it)
# 13. Splitting a string
df[["start_year", "end_year"]] = df["Year(s)"].str.split("-", n=1, expand=True)     #split df["year(s) into df["start_year"] and df["end_year"]
                                                                                    #seperates at "-" and only splits once (n=1)