import numpy as np
import pandas as pd

#Data normalisation is used to prevent datasets with a large range from dominating the data. Transforms features to a common scale

#Scikit-learn normalisation transformers:
#1. MinMaxScaler (Feature scaling) - Widely used technique that rescales features to a common range, (0-1). Useful when range of features vary significantly
#2. Z-score normalisation (Standardisation) - Transforms features to follow a standard normal distribution of a mean of 1, and standard deviation of 1
#                                             This technique is useful when the distribution of features is not uniform
#3. Robust scaling - Uses the median and interquartile range to scale features, making it look robust to outliers

#When to normalise data?:
#On ML algos that rely on distance calculations. E.g. KNN or SVM, or when the data has different units and scales
#Normalisation also benefitial for algos using gradient descent optimisation

#HOW TO CHOOSE THE RIGHT SCALER?
#Min-Max Scaling good for PRESERVING SPECIFIC RANGES
#Standard Scaler good for PRESERVING MEAN AND STANDARD DEVIATION




#IMPLEMENTING DATA NORMALISATION WITH SCIKIT-LEARN

#1. MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])   #sample data
minmaxscaler = MinMaxScaler()                             #initialise the scaler

#Fit and transform the data
normalised_data = minmaxscaler.fit_transform(data)        #Max value = 1, Min value = 0, and the rest are proportionately given a value
#print(normalised_data)


#2. Standardisation (Z-score Nomination)
from sklearn.preprocessing import StandardScaler
standardscaler = StandardScaler()

#Fit and transform the data
standardised_data = standardscaler.fit_transform(data)      #Mean = 0, Standard Deviation = 1, means that all the + and - values the average = 1.
#print(standardised_data)


#3. Robust Scaling
from sklearn.preprocessing import RobustScaler
robustscaler = RobustScaler()

#Fit and transform the data
robust_scaled_data = robustscaler.fit_transform(data)       #Maps the data between -1 and 1, using the interquartile range
#print(robust_scaled_data)




#PRACTICAL EXAMPLE
from sklearn.datasets import fetch_california_housing

#Step 1: Load the dataset
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MedHouseVal'] = housing.target
#print(housing)

#Step 2: Performing the techniques

#1. Min-Max-Scaling
from sklearn.preprocessing import MinMaxScaler

#Initialise the scaler
min_max_scaler = MinMaxScaler()     #can be the other transformers as well

#Fit and transform the data
df_min_max_scaled = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns)

#Display first few rows of scaled dataset
#print(df_min_max_scaled.head())


#COMBINING DIFFERENT SCALERS (OPTIONAL)
# Initialize scalers
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

# Apply Min-Max Scaling to selected columns
columns_min_max = ['CRIM', 'ZN', 'INDUS']
df_min_max = pd.DataFrame(min_max_scaler.fit_transform(df[columns_min_max]), columns=columns_min_max)

# Apply Standardization to other columns
columns_standard = ['NOX', 'RM', 'AGE']
df_standard = pd.DataFrame(standard_scaler.fit_transform(df[columns_standard]), columns=columns_standard)

# Combine the scaled data
df_combined = pd.concat([df_min_max, df_standard, df.drop(columns=columns_min_max + columns_standard)], axis=1)

# Display the first few rows of the combined dataset
#print(df_combined.head())