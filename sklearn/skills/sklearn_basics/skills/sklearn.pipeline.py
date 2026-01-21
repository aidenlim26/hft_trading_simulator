#The pipeline class in sklearn allows you to chain together multiple steps such as data transformations and model training into one process

#Components of a pipeline:
#A pipeline contains a sequence of steps, where each step is a TUPLE containing a name and a transformer or estimator object
#The final step of the pipeline must be an estimator (e.g. classifier or regressor), while the preceding steps must be transformers (e.g. scalers, encoders)

#Step 1: Import Libraries and Load Data
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
data = load_iris()
X = data.data
y = data.target

#Step 2: Split the data into training and testing sets
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Step 3: Define the pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler',StandardScaler()),                        #each step is a TUPLE
    ('pca',PCA(n_components=2)),
    ('classifier',LogisticRegression())
])

#Step 4: Train the pipeline
pipeline.fit(X_train,y_train)

#Step 5: Make predictions
y_prediction = pipeline.predict(X_test)

#Step 6: Evaluate the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_prediction)
#print(f"Accuracy:,{accuracy:.2f}")                      #print accuracy to 2dp

























