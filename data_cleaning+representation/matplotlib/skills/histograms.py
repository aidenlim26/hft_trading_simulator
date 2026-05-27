import matplotlib.pyplot as plt
import numpy as np

# Histograms is a visual representation of quantitative data
# They group values into bins(intervals) and count how many fall into range

scores = np.random.normal(loc=80,       #loc=80 means most freq score is 80
                          scale=10,     #scale is the deviation of numbers
                          size=100)     #how many values

scores = np.clip(scores,0,100)      #minimum is 0, max is 100 for scores

plt.hist(scores, bins=10,       #10 intervals
                 color="lightgreen",
                 edgecolor="black")

plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("Number of students")

plt.show()

