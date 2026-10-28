"""Gráfico de frequência: quantidade de chamados por tipo de atendimento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_frequencia.csv")
ordem = df["tipo_atendimento"].value_counts().index

fig, ax = plt.subplots(figsize=(9, 6))
sns.countplot(data=df, x="tipo_atendimento", order=ordem, hue="tipo_atendimento", palette="mako", legend=False, ax=ax)
for container in ax.containers:
    ax.bar_label(container, padding=3)
ax.set_title("Frequência de chamados por tipo de atendimento", fontsize=14, fontweight="bold")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Quantidade de chamados")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "05_frequencia.png", dpi=150)
plt.show()
