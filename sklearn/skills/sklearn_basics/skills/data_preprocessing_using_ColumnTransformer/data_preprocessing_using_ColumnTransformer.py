#Data preprocessing:
#Involves cleaning and transforming raw data into a format suitable for modeling.

#What is ColumnTransformer?:
#Scikit-learn ML library that allows you to selectively apply data preparation transforms to different columns in your dataset
#Useful when you have a mix of categorical and numerical data that require different preprocessing steps

#ColumnTransformer Advantages:
#1. Selective transformation: Apply specific transformations to subsets of columns
#2. Pipeline integration: Easily integrate with sklearn's pipeline for streamlined workflows
#3. Code organisation: Encapsulate preprocessing logic in a single, maintainable object

#SKLEARN TRANSFORMERS:
#1. SimpleImputer = Used to fill in missing data in a dataset with a specified strategy, such as mean, median, or mode.
#2. OneHotEncoder = Converts categorical features into a format that can be provided into ML algos by creating binary columns for each category
#                   NO correlation between categories
#3. OrdinalEncoder = Transforms categorical features into integer values that represent the ordinal relationship between categories. (e.g. low speed = 0, high speed =1)
#                   HAS correlation between categories



#IMPLEMENTING TRANSFORMERS IN SKLEARN

#Step 1: Importing Necessary Libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("CAR_SPEED_DATA.csv")

#Step 2: Splitting dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(df.drop(columns=['has_driving_license']),df['has_driving_license'],test_size=0.2)

#print(X_train)

#Step 3: Use sklearn's SimpleImputer to fill null with mean of each feature
#print(df.isnull().sum())
#Use SimpleImputer for speed column
si = SimpleImputer()
X_train_Speed = si.fit_transform(X_train[['Speed']])
X_test_Speed = si.fit_transform(X_test[['Speed']])
#print(X_train_Speed)

#Step 4: OrdinalEncoder for Average_speed feature
oe = OrdinalEncoder(categories=[['low','high']])
X_train_Average_speed = oe.fit_transform(X_train[['Average_speed']])
X_test_Average_speed = oe.fit_transform(X_test[['Average_speed']])
#print(X_train_Average_speed)

#Step 5: One Hot Encoding for Gender and City
ohe = OneHotEncoder(drop='first', sparse_output=False)      #drops first category of each feature
#                                                            OneHotEncoder by default returns a matrix, 'sparse_output=False' makes it return as a numpy array
X_train_Gender_City = ohe.fit_transform(X_train[['Gender','City']])
X_test_Gender_City = ohe.fit_transform(X_test[['Gender','City']])
#print(X_train_Gender_City)

#Step 6: Extracting 'Age'
X_train_Age = X_train.drop(columns=['Gender','Speed','Average_speed','City']).values
X_test_Age = X_test.drop(columns=['Gender','Speed','Average_speed','City']).values
#print(X_train_Age)

#Step 7: Concatenation into a single transformer
X_train_transformed = np.concatenate((X_train_Average_speed,X_train_Gender_City,X_train_Speed,X_train_Age),axis=1)
X_test_transformed = np.concatenate((X_test_Average_speed,X_test_Gender_City,X_test_Speed,X_test_Age),axis=1)
#print(X_test_transformed)






#USING ColumnTransformer (shortcut)

#ColumnTransformer:
#Powerful tool for applying different preprocessing transformations to specific columns within a dataset
#This allows processing based on the nature of each feature.

#ColumnTransformer SYNTAX:
#transformer = ColumnTransformer(transformers=[('imputer', SimpleImputer(), ['NumericalColumn1', 'NumericalColumn2']),('ordinal', OrdinalEncoder(), ['OrdinalColumn']),('onehot', OneHotEncoder(), ['CategoricalColumn1', 'CategoricalColumn2'])],remainder='passthrough')

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

transformer = ColumnTransformer(transformers=[
    ('t1',SimpleImputer(),['Speed']),                                               #t1,2,3 are just labels
    ('t2',OrdinalEncoder(categories=[['low','high']]),['Average_speed']),
    ('t3',OneHotEncoder(sparse_output=False,drop='first'),['Gender','City'])
],remainder='passthrough')                                                          #remainder ='passthrough' = any value unchanged by transformer is copied to output

#Fitting model with transformed data
print(transformer.fit_transform(X_train))
transformer.fit_transform(X_test)
print(transformer.transform(X_test))










