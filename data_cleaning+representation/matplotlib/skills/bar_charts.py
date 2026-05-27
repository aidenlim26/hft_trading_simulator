import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains","Fruit","Vegetables","Protein","Dairy","Sweets"])
values = np.array([4,3,2,5,3,1])

#plt.bar(categories,values, color="skyblue")     #default "plt.bar" is a vertical bar chart
plt.barh(categories,values, color="skyblue")     # "plt.barh" is a horizontal bar chart

plt.title("Daily consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()