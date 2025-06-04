# %%

import pandas as pd


series_idades = pd.Series(
    [18, 20, 22, 19, 21, 23, 25, 24, 22, 20],)
series_idades

# %%


media_idades = series_idades.mean()
print(f"A média das idades é: {media_idades:.2f} anos")
summary = series_idades.describe()
print("Resumo estatístico das idades:")
print(summary)