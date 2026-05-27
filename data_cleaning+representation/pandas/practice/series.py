import pandas as pd
#Create a Series survival_rate_by_pclass showing survival rate for each Pclass (a single Series, index = class).
df = pd.read_csv("../titanic_passengers.csv")
group = df.groupby("Pclass")
survival_rate_by_pclass = group["Survived"].mean()
#print(survival_rate_by_pclass)

#Make a Series of Age, then produce:
#count of missing ages
#min/max age
#the 10 youngest passengers (values + their PassengerId)
age = df["Age"]
missing_ages = age.isna().sum()
#print(missing_ages)

min_age = age.min()
#print(min_age)
max_age = age.max()
#print(max_age)

youngest_10 = age.nsmallest(10)         #nsmallest function finds the smallest () numbers
#print(youngest_10)

youngest_10_passenger_id = df.loc[youngest_10.index,"PassengerId"]  #".index" means: “go back to the original df and pick the PassengerId values from those same rows”.
#print(youngest_10_passenger_id)

results = pd.DataFrame({
    "PassengerId":youngest_10_passenger_id,
    "Age":youngest_10
})

#print(results.to_string(index=False))

#Create a Series from Embarked and compute the proportion of each embarkation port (normalized value counts). Which is most common?
embarked = df["Embarked"]
count = embarked.value_counts(normalize=True)*100  #".value_counts", counts how often each value appears
                                                   #"normalize=True", is proportions, the total sum = 1
                                                   #"(normalize=True)*100" is the percentage
print(count)

#print(df.to_string())