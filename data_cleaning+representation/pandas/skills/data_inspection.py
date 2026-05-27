import pandas as pd

df = pd.read_csv("titanic_passengers.csv")

#print(df.head()) #shows first 5 rows
#print(df.tail()) #shows last 5 rows
#print(df.sample(n=5, random_state=0)) #shows random 5 rows, random_state=0 means its the same random rows everytime u run it
#print(df.info)
print(df.describe())