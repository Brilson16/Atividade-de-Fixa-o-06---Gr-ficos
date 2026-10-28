"""Boxplot: distribuição salarial por departamento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_boxplot.csv")

fig, ax = plt.subplots(figsize=(9, 6))
sns.boxplot(data=df, x="departamento", y="salario", hue="departamento", palette="Set2", legend=False, ax=ax)
ax.set_title("Distribuição salarial por departamento", fontsize=14, fontweight="bold")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "02_boxplot.png", dpi=150)
plt.show()
