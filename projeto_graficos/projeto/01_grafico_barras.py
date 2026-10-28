"""Gráfico de barras agrupadas: vendas médias por categoria e região."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_barras.csv")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao", palette="viridis", ax=ax)
ax.set_title("Vendas médias por categoria e região", fontsize=14, fontweight="bold")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.legend(title="Região")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "01_barras.png", dpi=150)
plt.show()
