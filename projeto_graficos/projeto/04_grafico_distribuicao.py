"""Histograma com curva de densidade: distribuição da idade dos clientes."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(9, 6))
sns.histplot(df["idade"], bins=15, kde=True, color="steelblue", ax=ax)
ax.axvline(df["idade"].mean(), color="red", linestyle="--", label=f"Média: {df['idade'].mean():.1f}")
ax.axvline(df["idade"].median(), color="green", linestyle="--", label=f"Mediana: {df['idade'].median():.1f}")
ax.set_title("Distribuição da idade dos clientes", fontsize=14, fontweight="bold")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Frequência")
ax.legend()
plt.tight_layout()
fig.savefig(BASE / "graficos" / "04_distribuicao.png", dpi=150)
plt.show()
