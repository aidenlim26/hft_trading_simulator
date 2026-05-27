from tokenize import group

import pandas as pd
#Aggregate functions = Reduces a set of values into a single summary value
#Used to summarise and analyse data
#Often used with the groupby() function

df = pd.read_csv("IRIS_dataset.csv")

#WHOLE DATAFRAME
#print(df.mean(numeric_only=True))   #Telling pandas find the mean of any column that is numeric
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())  #Count function counts the number of non-NaN values in each column
#print(df.size())   #Counts number of rows in each column including NaN values

#SINGLE COLUMN
#print(df["petal_width"].mean())
#print(df["petal_width"].sum())
#print(df["petal_width"].min())
#print(df["petal_width"].max())
#print(df["petal_width"].count())

#GROUP
group = df.groupby("species")     #using the groupby function, you are grouping all the different
                                  #types of species into a group, so they are seperated
#print(group["sepal_width"].mean())    #This is to find the mean of sepal width for each type of species
#print(group["sepal_width"].sum())
#print(group["sepal_width"].min())
#print(group["sepal_width"].max())
#print(group["sepal_width"].count())
