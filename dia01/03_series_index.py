# %%
import pandas as pd

idades = [18, 20, 22, 19, 21, 23, 25, 24, 22, 20]


series_idades = pd.Series(idades)
print("Série de idades:")
series_idades

# %%

idades[-1]

# %%

series_idades

# %%

series_idades = series_idades.sort_values()
series_idades

# %%

series_idades.iloc[0]  # Acessa o primeiro elemento da série

# %%
series_idades.iloc[-1]  # Acessa o último elemento da série

# %%

series_idades.iloc[0:3]  # Acessa os três primeiros elementos da série

# %%

series_idades.iloc[::-1]  # Acessa a série em ordem inversa

# %%

idades = [18, 20, 22, 19, 21, 23, 25, 24, 22, 20]

indexs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
series_idades = pd.Series(idades, index=indexs)
series_idades
# %%    
series_idades["b"]  # Acessa o elemento com o índice 'b'