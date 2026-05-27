import matplotlib.pyplot as plt
import numpy as np

# "grid()" helps make plots easier to read by adding reference lines

x = [1,2,3,4,5]
y = [5,10,15,20,25]

plt.grid(linewidth=1, color="lightgray", linestyle="dashdot")

plt.plot(x,y)
plt.show()