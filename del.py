import pandas as pd
import csv

df = pd.read_csv("merged.csv")
print(df.shape)

del df["Brown dwarf"]

df.to_csv("final.csv")
