import matplotlib.pyplot as plt
import pandas as pd

# Cargar dataset (df del ítem b)
df = pd.read_csv("Cancer_Pulmon.csv")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Boxplots de variables clínicas", fontsize=16, fontweight="bold")

# Boxplot de age
axes[0].boxplot(df['age'], vert=True)
axes[0].set_title("Age")
axes[0].set_ylabel("Edad")

# Boxplot de bmi
axes[1].boxplot(df['bmi'], vert=True)
axes[1].set_title("BMI")
axes[1].set_ylabel("BMI")

# Boxplot de cholesterol_level
axes[2].boxplot(df['cholesterol_level'], vert=True)
axes[2].set_title("Cholesterol Level")
axes[2].set_ylabel("Nivel de colesterol")

plt.tight_layout()
plt.savefig("grafico_boxplot.png", dpi = 300)
plt.show()
