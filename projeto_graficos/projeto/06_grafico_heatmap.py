"""Heatmap: movimento de clientes por dia da semana e horário."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_heatmap.csv")

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
matriz = df.pivot(index="dia_semana", columns="horario", values="movimento_clientes").reindex(dias)

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(matriz, annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5, cbar_kws={"label": "Clientes"}, ax=ax)
ax.set_title("Movimento de clientes por dia e horário", fontsize=14, fontweight="bold")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da semana")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "06_heatmap.png", dpi=150)
plt.show()
