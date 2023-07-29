import numpy as np
import scipy.stats
import matplotlib.pyplot as plot

from process_data import dataset

bookCountCol = dataset.loc[:, "bookCount"]
reposCol = dataset.loc[:, "githubLanguage.repos"]

print(bookCountCol)
print(reposCol)

r, p = scipy.stats.pearsonr(bookCountCol, reposCol)

print("p", p)
print("r", r)

plot.scatter(bookCountCol, reposCol, alpha=0.5)

plot.title(
    "Correlação linear entre número de livros e número de repositório no Github")

plot.xlabel("Número de livros")
plot.ylabel("Número de repositório no Github")

plot.show()
