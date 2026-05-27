import pandas as pd
# Series = A Panda's 1D labeled array that can hold any data type.
# Basically like a column in excel

#data = [100,102,104,200,202]

#series = pd.Series(data)
#series = pd.Series(data,index=["a","b","c","d","e"]) #Index is for you to customise the index
#print(series1)
#print(series.loc["b"])  #loc means location by label, used to find the data corresponding to the index
#series.loc["c"] = 200
#print(series)
#print(series.iloc[1]) #iloc means integer location by label, basically same as accessing an array
#print(series[series >= 200])  #filtering

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}  #Adding a dictionary

series = pd.Series(calories)
#print(series.loc["Day 2"])
#series.loc["Day 3"] += 500  # "+=" is to add on the value on top of the existing value
print(series[series > 2000])