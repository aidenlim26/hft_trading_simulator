#METHOD 1: Feature Importances from Tree-Based Models

#Tree-based models like RandomForestClassifier and GradientBoostingClassifier provide built-in feature importance scores
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

#Load dataset
data = load_iris()
X = data.data
y = data.target
feature_names = data.feature_names

#Train a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X,y)

#Get feature importances
importances = clf.feature_importances_

#Create a Dataframe for better visualisation
importance_df = pd.DataFrame({
    'Feature':feature_names,
    'Importance':importances
}).sort_values(by='Importance',ascending=False)
#print(importance_df)

#Plot feature importances
plt.figure(figsize=(10,6))
plt.barh(importance_df['Feature'],importance_df['Importance'])
plt.xlabel('Importance',size=20)
plt.ylabel('Feature Importances',size=20)
plt.tight_layout()
#plt.show()




#METHOD 2: Using SelectFromModel
#SelectFromModel selects features based on their importance based on their importance scores from their fitted model
#Can be applied to various classifiers and regressions

from sklearn.feature_selection import SelectFromModel

#Create a selector with the trained model
clf = RandomForestClassifier(n_estimators=100)
selector = SelectFromModel(clf, threshold='mean')       #threshold='mean' = features with importance above the mean is selected
selector.fit(X,y)

#Get selected features indices
selected_features = selector.get_support(indices=True)  #returns the indices of the SELECTED features

#Print selected feature names
selected_feature_names = [feature_names[count] for count in selected_features]
#print("Selected Features:",selected_feature_names)




#METHOD 3: Using Recursive Feature Elimination (RFE)
#Recursively removes features and selects features based on model performance

from sklearn.feature_selection import RFE

#Create RFE selector with a classifier
rfe = RFE(clf,n_features_to_select=2)
rfe.fit(X,y)                                #Fits the features based on model

#Get the selected feature indices
rfe_selected_features = rfe.support_        #Boolean mask True=Selected, does this to select the selected features

#Print selected feature names
rfe_selected_feature_names = [feature_names[count] for count in range(len(feature_names)) if rfe_selected_features[count]]
#Feature names found using a list comprehension
#print("Selected Feature Names:",rfe_selected_feature_names)




#MODEL 4: Using L1 Regularisation with Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel

#Train a logistic regression model with L1 penalty
logreg = LogisticRegression(penalty='l1',solver='saga')
logreg.fit(X,y)

#Get feature importances (coefficients)
logreg_importances = abs(logreg.coef_[0])

#Create a Dataframe for better visualisation
logreg_importances_df = pd.DataFrame({
    'Feature':feature_names,
    'Coefficient':logreg_importances
}).sort_values(by='Coefficient',ascending=False)

#print(logreg_importances_df)









