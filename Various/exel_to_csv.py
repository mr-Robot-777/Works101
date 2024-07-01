import pandas as pd

read_file = pd.read_excel("Test.xlsx")
read_file.to_csv("Test.csv", index=None, header=True)

df = pd.DataFrame(pd.read_csv("Test.csv"))



# Из csv в exel

import pandas as pd
import numpy as np


df_new = pd.read_csv("Names.csv")
myfile = pd.ExcelWriter('Names.xlsx')
df_new.to_excel(myfile, index=False)

myfile.save()
