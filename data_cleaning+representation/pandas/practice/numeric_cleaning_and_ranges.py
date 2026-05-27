import pandas as pd
import numpy as np
df = pd.read_csv("Building_Permits.csv",low_memory=False)
#Objective: Detect and correct bad numeric values.
#Check for negative or zero values in “Price” or “Volume”.
location = pd.to_numeric(df["Location"],errors="coerce")
#print(location.shape)
negative_or_zero = df[location<=0]
#print(negative_or_zero)
#Replace invalid values (e.g., negative prices) with np.nan.
#Detect anomalies using simple rules (e.g., prices > 10× median price).
anomalies = df
#Clip extreme values using clip(lower, upper).