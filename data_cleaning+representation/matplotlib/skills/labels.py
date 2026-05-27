import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([17,23,38,5])
y3 = np.array([13,15,20,30])

plt.title("Class size", fontsize=20,
                        family="Arial",         #font type
                        fontweight="bold",
                        color="blue")

plt.xlabel("Year", fontsize=20,
                   family="Arial",
                   fontweight="bold",
                   color="violet")

plt.ylabel("Students", fontsize=20,
                       family="Arial",
                       fontweight="bold",
                       color="violet")

#plt.tick_params(axis="x")          #ticks parameters can either be "x", "y", or "both"
#plt.tick_params(axis="y")
plt.tick_params(axis="both",
                colors="grey")      #makes the ticks grey

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.xticks(x)          #Makes it so theres only ticks at each x-value (no more 0.5 increments)

plt.show()