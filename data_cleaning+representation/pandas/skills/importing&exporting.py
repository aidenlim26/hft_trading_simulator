import pandas as pd

#Importing a CSV file into a dataframe
df = pd.read_csv("IRIS_dataset.csv")
#Exporting changes to the csv
df.to_csv("highest_grossing_concert_tours.csv", index=False)

#print(df)   #Only print the first 5 and last 5 rows

#print(df.to_string())         #This prints ALL the rows



#Importing a JSON file
df1 = pd.read_json("iris.json")

#print(df1.to_string())