import matplotlib.pyplot as plt
import numpy as np

# Scatter graphs = Shows relationship between two variables, helps to identify correlation (+,-, None)

x1 = np.array([0,1,1,2,3,4,5,6,7,7,8])               #hours studied
y1 = np.array([55,60,65,62,68,70,75,78,82,85,87])    #grades

x2 = np.array([0,1,2,2,3,4,5,6,7,8,8])               #hours studied
y2 = np.array([50,58,65,70,72,78,83,88,92,95,97])

plt.scatter(x1,y1,color="blue",
                  alpha=0.5,      #alpha = transparency of dots
                  s=25,           #s = size
                  label="Class A")

plt.scatter(x2,y2,color="red",
                  alpha=0.5,      #alpha = transparency of dots
                  s=25,           #s = size
                  label="Class B")

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")

plt.legend()        #Used after "label="" " is used in the plt.scatter
plt.show()