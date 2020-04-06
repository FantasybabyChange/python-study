import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

csv = pd.read_csv("./iris_training.csv")
print(csv)
# csv.plot(kind="scatter", x="120", y="4")
# sns.set(style="white", color_codes=True)
# sns.jointplot(x="120", y="4", data=csv, size=5)
# sns.distplot(csv["120"])
sns.FacetGrid(csv, hue="virginica", size=5).map(plt.scatter, "120", "4", ).add_legend()
plt.show()
