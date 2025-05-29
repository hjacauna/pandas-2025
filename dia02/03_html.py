# %%

import pandas as pd

dfs = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")
dfs
# Display the first table

# %%

df_uf = dfs[1]
df_uf.to_csv("unidades_federativas.csv", sep=";", index=False)
# Display the first few rows of the DataFrame