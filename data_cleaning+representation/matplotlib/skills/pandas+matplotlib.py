import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("pokemon.csv")

type_counts = df['Type1'].value_counts(ascending=True)

plt.barh(type_counts.index,type_counts.values,color="violet",edgecolor="black")
plt.xlabel("Counts")
plt.ylabel("Pokemons")
plt.title("Type 1 Pokemons")
plt.tight_layout()      #make sure everything fits in the graph
plt.show()