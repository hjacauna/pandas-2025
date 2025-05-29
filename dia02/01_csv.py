# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";") # read csv file with custom separator
df

# %%

df.to_csv("customers2.csv", sep=";", index=False) # save csv file with custom separator

# %%

df.to_excel("customers.xlsx", index=False) # save as excel file

# %%

df_2 = pd.read_excel("customers.xlsx") # read excel file
df_2