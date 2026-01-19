#WHAT IS FEATURE SELECTION?:
#Feature selection is the process of identifying and selecting the RELEVANT subset used in model construction
#Goal is to reduce overfitting, improving accuracy, and reducing training time


#FEATURE SELECTION METHODS:
#1. Filter Methods: Filter methods use statistical techniques to evaluate the relevance of features independently to the model
#                   Common techniques include: correlation coefficients, chi-square tests, and mutal information

#2. Wrapper Methods: Wrapper methods use a predictive model to evaluate feature subsets and select the best performing combination.
#                   Common techniques include: recursive feature elimination (RFE), and forward/backward feature selection

#3. Embedded Methods: Embedded methods perform feature selection during the model training process.
#                   Examples include: Lasso (L1 regularisation), and feature importance from tree-based models



#FEATURE SELECTION TECHNIQUES:
#1. Univariate Selection: Univariate selection evaluates each feature individually to determine its importance.
#                         Techniques like: SelectKBest, and SelectPercentile can be used to select the top features based on statistical tests

#2. Recursive Feature Elimination (RFE): RFE is a wrapper method that recursively removes the least important features based on the models performance
#                                        It repeatedly builds a model and eliminates its weakest features until the desired number of features is reached

#3. Feature Importance from Tree-based Models: Tree-based models like decision trees and random forests can provide feature importance scores
#                                              Indicating the importance of each feature in making predictions



#PRACTICAL IMPLEMENTATION OF FEATURE SELECTION WITH SCIKIT-LEARN

#Step 1: Data Preparation
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#Load dataset
data = load_iris()
X = pd.DataFrame(data.data,columns=data.feature_names)
y = data.target

#Splitting data into train and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)


#METHOD 1: Univariate Selection
from sklearn.feature_selection import SelectKBest, chi2

#Apply SelectKBest with chi2
select_k_best = SelectKBest(score_func=chi2, k=2)                       #k=2 means select the top 2 features according to the chi-squared test
X_train_k_best = select_k_best.fit_transform(X_train,y_train)
#print("Selected features:",X_train.columns[select_k_best.get_support()])    #"get_support()" returns a boolean mask, only returning True for selected feature names


#METHOD 2: Recursive Feature Elimination
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

#Apply RFE with LogisticRegression
logistic_regression_model = LogisticRegression()
rfe = RFE(logistic_regression_model, n_features_to_select=2)        #Select 2 features only, and stores which features are selected
X_train_rfe = rfe.fit_transform(X_train, y_train)               #just the output, doesnst store which features are selected
#print("Selected features:",X_train.columns[rfe.get_support()])     #uses the original column and using rfe, finds which features are selected


#METHOD 3: Tree-Based Feature Importance
from sklearn.ensemble import RandomForestClassifier

#Train random forest and get feature importance
random_forest_model = RandomForestClassifier()
random_forest_model.fit(X_train,y_train)
importances = random_forest_model.feature_importances_

#Display feature importances
feature_importances = pd.Series(importances, index=X_train.columns)     #index assigns the corresponding importance value to the column name
#print("Feature Importances:",feature_importances.sort_values(ascending=False))













