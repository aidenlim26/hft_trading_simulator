from sklearn.datasets import load_iris
import numpy as np

#STEP 1: IMPORTING DATA
iris = load_iris()

X = iris.data           #input data
y = iris.target         #outputs, what we are trying to predict

feature_names = iris.feature_names
target_names = iris.target_names

#print(feature_names)
#print(target_names)


#STEP 2: SPLITTING DATASETS
from sklearn.model_selection import train_test_split

#Need to split into training and testing datasets
#Training set = used to train the model
#Testing set = evaluate how accurate the model is

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,random_state=1)       #testsize = 0.4 means 40% testing data, 60% training data, random_state=1 is used for reproducibility

#Check the shape to make sure all datasets have the correct proportions of data
#print("X_train Shape:",  X_train.shape)
#print("X_test Shape:", X_test.shape)
#print("Y_train Shape:", y_train.shape)
#print("Y_test Shape:", y_test.shape)


#STEP 3: HANDLING CATEGORICAL DATA

#LABEL ENCODING
#Need to change text data into numerical data (e.g. cat,dogs,mouse -> 0,1,2)

from sklearn.preprocessing import LabelEncoder

#LabelEncoder(): It is initialized to create an encoder object that will convert categorical values into numerical labels.
#fit_transform(): This method first fits the encoder to the categorical data and then transforms the categories into corresponding numeric labels.

categorical_feature = ['cat','dog','dog','cat','bird']
encoder = LabelEncoder()
encoded_feature = encoder.fit_transform(categorical_feature)
#print(encoded_feature)

#ONE-HOT-ENCODING
from sklearn.preprocessing import OneHotEncoder
#Creates separate binary columns for each category
#Reshaped to a 2D array
#E.g. cat,dog,mouse -> [[1,0,0]  Cat
#                       [0,1,0]  Dog
#                       [0,0,1]] Mouse

categorical_feature = np.array(categorical_feature).reshape(-1,1)
encoder1 = OneHotEncoder(sparse_output=False)       #(sparse_output=False) generates binary columns
encoded_feature1 = encoder1.fit_transform(categorical_feature)
#print(encoded_feature1)


#STEP 4: TRAINING THE MODEL
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(max_iter=200)      #creating a logistic regression classifier object
log_reg.fit(X_train,y_train)                    #using this, the regression model adjusts the model's parameters to best fit the data


#STEP 5: MAKE PREDICTIONS
y_pred = log_reg.predict(X_test)        #log_reg.predict uses trained regression model to predict labels for test data X

#STEP 6: EVALUATING MODEL ACCURACY
#Done by comparing y_test and y_pred
from sklearn import metrics

print("Logistic Regression Accuracy:", metrics.accuracy_score(y_test,y_pred))


#STEP 6: MAKE PREDICTIONS ON NEW DATA
sample = [[3,5,4,2],[2,3,5,4]]
preds = log_reg.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:",pred_species)
