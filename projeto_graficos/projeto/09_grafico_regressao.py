"""Regressão linear: renda mensal x gasto mensal."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
sns.set_theme(style="whitegrid")

from scipy import stats

df = pd.read_csv(BASE / "dados_regressao.csv")
res = stats.linregress(df["renda_mensal"], df["gasto_mensal"])

fig, ax = plt.subplots(figsize=(9, 6))
sns.regplot(
    data=df, x="renda_mensal", y="gasto_mensal",
    scatter_kws={"alpha": 0.6}, line_kws={"color": "red"}, ax=ax,
)
ax.set_title("Regressão linear: renda x gasto mensal", fontsize=14, fontweight="bold")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
ax.text(
    0.05, 0.92,
    f"y = {res.slope:.3f}x + {res.intercept:.1f}\nR² = {res.rvalue**2:.3f}",
    transform=ax.transAxes, fontsize=11,
    bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
)
plt.tight_layout()
fig.savefig(BASE / "graficos" / "09_regressao.png", dpi=150)
plt.show()
