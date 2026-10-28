"""Gráfico de dispersão: altura x peso, colorido por sexo."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(9, 6))
sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo", style="sexo", s=70, alpha=0.8, ax=ax)
ax.set_title("Relação entre altura e peso", fontsize=14, fontweight="bold")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "03_dispersao.png", dpi=150)
plt.show()
