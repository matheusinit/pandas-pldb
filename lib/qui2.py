from scipy.stats import chi2_contingency
from process_data import dataset
import pandas as pd

print(dataset)

# H0 = Não há correlação entre o número de livros e o tipo de linguagem de programação
# H1 = Há correlação entre o número de livros e o tipo de linguagem de programação

bookCountCol = dataset.loc[:, "bookCount"]
typeCol = dataset.loc[:, "type"]

table = pd.crosstab(bookCountCol, typeCol)

stat, p, dof, expected = chi2_contingency(table)

alpha = 0.05


print("p value is ", str(p))

if p <= alpha:
    print("Dependent (reject H0)")
else:
    print("Indenpendent (H0 holds true)")
