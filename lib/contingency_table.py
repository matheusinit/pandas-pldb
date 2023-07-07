import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv("loan_status.csv")

print(data.head(10))

data.describe()

# tabela de contigência entre notas e status de emprestimo
data_crosstab = pd.crosstab(data['grade'], data['loan_status'], margins = False)



