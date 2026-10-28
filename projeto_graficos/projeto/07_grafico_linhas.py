"""Gráfico de linhas: evolução diária das vendas (jan-mar/2026), com marcadores por loja."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

import matplotlib.dates as mdates

df = pd.read_csv(BASE / "dados_linhas.csv", parse_dates=["data"]).sort_values("data")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df["data"], df["vendas"], color="gray", alpha=0.6, linewidth=1.5, label="Vendas diárias")
sns.scatterplot(data=df, x="data", y="vendas", hue="loja", s=45, zorder=3, ax=ax)
ax.set_title("Evolução diária das vendas", fontsize=14, fontweight="bold")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
ax.legend(title="Loja")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "07_linhas.png", dpi=150)
plt.show()
