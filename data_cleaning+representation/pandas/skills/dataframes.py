import pandas as pd

#Dataframe = A tabular data structure with rows and columns (2D structure)
#Similar to excel spreadsheets

data = {                                            #Creating a dictionary
    "Name": ["Spongebob","Patrick", "Squidward"],
    "Age": [30,35,50]
}

df = pd.DataFrame(data, index=["Employee 1","Employee 2", "Employee 3"])   #"df" means dataframe
#print(df)
#print(df.loc["Employee 3"])
#print(df.iloc[2])

#Add a new column
df["Job"] = ["Cook","N/A","Cashier"]
#print(df)

#Add a new rows
new_rows = pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"},
                         {"Name":"Eugene","Age": 60,"Job":"Manager"}],
                        index = ["Employee 4","Employee 5"])

#print(new_rows)
df = pd.concat([df,new_rows])            #concat = concatenation, basically combining, you add all the dataframes you want to combine inside the square brackets
print(df)
