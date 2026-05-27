import matplotlib.pyplot as plt
import numpy as np

x = np.array([50,100,150,200,250])
y1 = np.array([1,2,3,4,5])
y2 = np.array([12,13,15,19,22])
y3 = np.array([23,24,27,20,30])

line_styles = dict(marker=".",
                    markersize=12,
                    markerfacecolor="red",
                    markeredgecolor="black",
                    linestyle="dashdot",
                    linewidth=3,
                    color="violet")         #color = line colour

plt.plot(x,y1, **line_styles)               #use "**" to unpack a dictionary
plt.plot(x,y2)
plt.plot(x,y3, **line_styles)

plt.show()