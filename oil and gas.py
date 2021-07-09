import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("oil and gas.csv")

df = df.filter(["cty_name", "year", "oil_price_nom", "gas_price_nom"])
df = df.rename(columns={"cty_name": "Country", "oil_price_nom": "Oil Prices", "gas_price_nom": 'Gas Prices'})
df1 = df.groupby("year")[["Oil Prices", "Gas Prices"]].mean().reset_index()


sns.set_theme()
sns.set_context("talk")
ax = df1.plot(x="year", y=["Oil Prices", "Gas Prices"], color=["orange", "blue"])
ax.set(xlabel="Year")
plt.title("Oil and Gas prices from 1937 to 2020")

plt.show()


