import pandas as pd
#Filtering = keeping the rows that match a condition

df = pd.read_csv("IRIS_dataset.csv")

#wide_petal = df[df["petal_width"] >= 2.3]
long_sepal = df[df["sepal_length"] >= 7.3]
petalsepal5 = df[(df["petal_length"] == 5.0) |                     #"|" means or in C++
            (df["sepal_length"] == 5.0)]
#print(wide_petal)
#print(long_sepal)
print(petalsepal5)