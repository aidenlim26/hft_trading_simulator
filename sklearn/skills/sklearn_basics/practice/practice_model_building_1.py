import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#Load the dataset
data = load_diabetes()

#Seperate data and target
X = data.data
y = data.target

#Split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Choose a model
model = LinearRegression()

#Train and fit the model
model.fit(X_train,y_train)


#Predict on test data
y_pred = model.predict(X_test)

#Evaluate model performance
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("Intercept:",model.intercept_)
print("Coefficients:",model.coef_)
print("Mean Squared Error:",mse)
print("R^2 score:",r2)
print("y_prediction",y_pred)


#Matplotlib comparison
import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()