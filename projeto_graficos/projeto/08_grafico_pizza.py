"""Gráfico de pizza: participação de cada canal no faturamento."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

df = pd.read_csv(BASE / "dados_pizza.csv")

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    df["faturamento"],
    labels=df["canal_venda"],
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("pastel"),
    wedgeprops={"edgecolor": "white"},
)
ax.set_title("Faturamento por canal de venda", fontsize=14, fontweight="bold")
plt.tight_layout()
fig.savefig(BASE / "graficos" / "08_pizza.png", dpi=150)
plt.show()
