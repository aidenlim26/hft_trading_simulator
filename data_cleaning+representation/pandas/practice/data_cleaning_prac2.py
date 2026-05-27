import pandas as pd

df = pd.read_csv("titanic_passengers.csv")

#QUICK INSPECTION
#Print the dataset shape, column names, and dtypes.
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#Show 8 random rows, but make it reproducible (random_state=0).
random_8 = df.sample(n=8, random_state=0)[["PassengerId","Fare","Survived"]]     #adding column names so that they only show from those columns
#print(random_8)
#List columns that contain any missing values, sorted by missing count.
missing_values = df.isna().sum().sort_values(ascending=False)
#print(missing_values)


#MISSING VALUES
#Compute the % missing in each column (rounded to 1 decimal).
missing_percentages = (df.isna().mean() * 100).round(1).sort_values(ascending=False)        #.mean() = no. of NaN / total numbers
#print(missing_percentages)
#Fill missing Cabin with "Unknown". Then show Cabin.value_counts().head(5).
df = df.fillna({"Cabin":"Unknown"})
#print(df["Cabin"].value_counts().sort_values(ascending=False))
#Fill missing Age with the median within each Pclass (group-wise imputation).
Pclass_median = df["Pclass"].median()
df = df.fillna(Pclass_median)
#print(df["Pclass"])


#FILTERING & CONDITIONS
#How many passengers are:
#under 18
under_18 = (df["Age"]<18).sum()
#print(under_18)
#18–60
age18_to_60 = ((df["Age"]>=18) & (df["Age"]<=60)).sum()
#print(age18_to_60)
#over 60
over_60 = (df["Age"]>60).sum()
#print(over_60)
#Find all rows where Fare is 0 or Fare is missing.
fare_rows = df[(df["Fare"] == 0) | (df["Fare"].isna())]
#print(fare_rows)


#SORTING & SELECTING
#Show the 10 passengers with the highest Fare (include Name, Fare, Pclass).
top_10_fares = df.sort_values(by="Fare", ascending=False).head(10)
#print(top_10_fares[["Name","Fare","Pclass"]])
#Sort by Pclass ascending, then Fare descending.
sorted_df = df.sort_values(by=["Pclass","Fare"], ascending=[True,False]).head(20)
#print(sorted_df[["Name","Fare","Pclass"]])


#GROUPBY SUMMARIES
#Survival rate by Sex (mean of Survived).
group_sex = df.groupby("Sex")
#print(group_sex["Survived"].mean())
#Survival rate by Pclass.
group_Pclass = df.groupby("Pclass")
#print((group_Pclass["Survived"].mean())*100)
#group_PClass = df.groupby("Pclass")
#print(group_PClass["Survived"].mean() * 100)
#Average Fare by Embarked and Pclass (a 2D groupby).
average_fare = df.groupby(["Embarked", "Pclass"])["Fare"].mean().round(2)
#print(average_fare)
#For each Embarked, show the median Age and count of passengers.
group_embarked = df.groupby("Embarked")
median_age = group_embarked["Age"].median()
#print(median_age)
count_passengers = group_embarked["PassengerId"].count()
#print(count_passengers)


#VALUE COUNTS & MAPPING
#Embarked proportions (value_counts(normalize=True)) after filling missing.
df = df.fillna({"Embarked":"Missing"})
embarked_proportions = df["Embarked"].value_counts(normalize=True)*100
#print(embarked_proportions)
#Map Sex to numeric (male->0, female->1) into a new column SexCode.
#SexCode = df["Sex"].replace({"male":0,"female":1})
#print(SexCode)


#STRING CLEANING
#Extract title from Name (e.g., Mr, Mrs, Miss) into a Title column.
df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.", expand=False).str.strip()
#print(df["Title"])
#Show the top 10 most common titles.
top_10_titles = (df["Title"].value_counts(normalize=True)*100)
#print(top_10_titles)

#OUTLIERS & VALIDATION
#Find rows with Age < 0, Fare < 0, or Fare > 500. How many? Show first 10.
df = df.fillna({"Age":"Missing"})
age_outliers = (df["Age"]<0).sum()
#print(age_outliers)
fare_outliers = df[((df["Fare"]<0) | (df["Fare"]>500))].head(10)
print(fare_outliers)















