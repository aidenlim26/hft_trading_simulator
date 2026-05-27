import matplotlib.pyplot as plt
import numpy as np

# Pie chart = Circular chart divided into slices to show percentages of the total.
# Good for visualising distribution among catagories

catagories = np.array(["Freshmen","Sophmores","Juniors","Seniors"])
values = np.array([300,250,275,225])
colours = ["red","blue","yellow","violet"]

plt.pie(values, labels=catagories,
                autopct="%1.1f%%",      # "autopct" means auto percentage, and just copy "%1.1f%%" everytime to format the percentage to 1 dp with a % at the back
                colors=colours,
                explode=[0,0,0,0.1],    # "explode" basically means how far the selected part of the pie chart moves away from the rest of the slices
                shadow=True,            # "shadow" is the dropshadow, basically gives the pie chart a shadow
                startangle=90)          # rotates the chart

plt.title("College")

plt.show()