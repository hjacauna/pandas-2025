# %%
import pandas as pd

df = pd.read_csv("../data/transactions.csv",sep=";")    
df.head()

# %%
pontos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50]
filtro = []

for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])


resultado

# %%

teste = pd.DataFrame(
    {
        "nome": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"],
        "idade": [15, 35, 45, 29, 40],
        "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"] 

    }
)

filtro = teste["idade"] > 18

teste[filtro]

# %%

df = pd.read_csv("../data/transactions.csv",sep=";")    
df.head()

# %%

filtro = df["VlPoints"] > 50

df[filtro]

# %%

filtro = (df["VlPoints"] >= 50) & (df["VlPoints"] < 100)
filtro
df[filtro]

# %%

filtro = (df["VlPoints"] == 1) | (df["VlPoints"]== 100)
filtro
df[filtro]