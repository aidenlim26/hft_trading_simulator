import pandas as pd

#df = pd.read_csv("IRIS_dataset.csv")
df = pd.read_csv("IRIS_dataset.csv",index_col="species")    #index_col means u set which column u want to be the index

#SELECTION BY COLUMN
#print(df["species"].to_string())        #"to_string" function prints the entire thing
#print(df["petal_length"].to_string())
#print(df[["petal_length","species"]].to_string())

#SELECTION BY ROW
#print(df.loc[0])
#print(df.loc["Iris-virginica"])  #Shows all the data for the specific species
#print(df.loc["Iris-virginica",["sepal_length","petal_width"]])      #Shows only the 2 columns for the specific species**
#print(df.loc["Iris-setosa":"Iris-versicolor",["sepal_length","petal_width"]])       #Using slicing to get everything from setosa to versicolor
#print(df.to_string())
#print(df.iloc[0:11:2])           #Using slicing to print the first 10 rows with a step of 2
#print(df.iloc[0:11:2, 0:2])      #Same as line above but only includes first 2 columns

#practice
flower_species = input("Enter flower species: ")

try:
    print(df.loc[flower_species])
except KeyError:
    print("Not found")