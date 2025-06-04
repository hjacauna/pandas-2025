# %%
import pandas as pd
from pathlib import Path

# prefer local sample file if the original dataset is missing
file_path = Path("../data/customers.csv")
if not file_path.exists():
    file_path = Path("customers2.csv")

df = pd.read_csv(file_path, sep=";")
df

# %%

df.to_csv("customers2.csv", sep=";", index=False) # save csv file with custom separator

# %%

df.to_excel("customers.xlsx", index=False) # save as excel file

# %%

df_2 = pd.read_excel("customers.xlsx") # read excel file
df_2