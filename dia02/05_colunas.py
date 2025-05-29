# %%
import pandas as pd

df = pd.read_csv('../data/transactions.csv',sep=';')
df

# %%

df.shape

# %%

df.info(memory_usage='deep')

# %%

df.dtypes

# %%

df.rename(columns={'VlPoints': 'ValorPontos',
                   'DescSysOrigin': 'SistemaOrigem'},inplace=True)

# %%
colunas = ["IdCustomer", "ValorPontos"]
df[colunas]

# %%
# select * from df

df

# %%

# select IdCustomer, ValorPontos from df
df[['IdCustomer', 'ValorPontos']]

# %%

# select idcustomer, valorpontos from df limit 5    
df[['IdCustomer', 'ValorPontos']].head(5)

