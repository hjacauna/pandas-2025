# %%
import pandas as pd

df = pd.read_csv("../data/transaction_product.csv",sep=";")    
df

# %%

filtro = (df["CodProduct"] == 5) | (df["CodProduct"] == 11)
df[filtro]

# %%
filtro = df["CodProduct"].isin([5, 11])
df[filtro]

# %%

clientes = pd.read_csv("../data/customers.csv",sep=";")
clientes.head()

# %%

~clientes["CreatedAt"].isna()
clientes["CreatedAt"].notna()