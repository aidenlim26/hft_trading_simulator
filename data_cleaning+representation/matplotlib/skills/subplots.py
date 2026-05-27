import matplotlib.pyplot as plt
import numpy as np

#Figure = The entire canvas
#Ax = A single plot (subplot)

x = np.array([1,2,3,4,5])

figure, axes = plt.subplots(2,2)        #Creates 2 rows and 2 columns of graphs, now have 4 graphs, axes is techincally a numpy array

axes[0,0].scatter(x,x*2,color="red")
axes[0,0].set_title("x*2")

axes[0,1].bar(x,x**2,color="blue")
axes[0,1].set_title("x**2")

axes[1,0].scatter(x,x**3,color="violet")
axes[1,0].set_title("x**3")

axes[1,1].plot(x,x**4,color="green")
axes[1,1].set_title("x**4")

plt.tight_layout()      #make sure everything fits in the window

plt.show()