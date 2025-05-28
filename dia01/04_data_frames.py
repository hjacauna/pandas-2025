# %%

import pandas as pd

idades = [18, 20, 22, 19, 21, 23, 25, 24, 22, 20]

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

series_idades = pd.Series(idades)
series_letras = pd.Series(letras)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["letras"] = series_letras
df 

# %%

df["letras"]

# %%

df.iloc[0]  # primeira linha

# %%

df.iloc[0]["letras"]  # primeira linha, coluna letras
