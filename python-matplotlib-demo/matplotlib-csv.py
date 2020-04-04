import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
csv = pd.read_csv("./iris_training.csv")
print(csv)
csv.plot(kind="scatter", x="120", y="4")
plt.show()
