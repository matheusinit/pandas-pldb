import numpy as np
from scipy import stats
from numpy.random import seed
from numpy.random import randn
from numpy.random import normal
from scipy.stats import ttest_1samp

from process_data import raw_dataset, dataset

dataset_with_repos_more_than_fifty_thousand = raw_dataset.query(
    "`githubLanguage.repos` > 30000")

book_count = dataset_with_repos_more_than_fifty_thousand.filter(
    ['bookCount'])[:30]

mean = raw_dataset.filter(['bookCount']).mean()

t_stat, p_value = ttest_1samp(book_count, popmean=mean)

print("t_stat", t_stat)
print("p_value", p_value)

# h0 = Linguagens de programação com mais de 30.000 repositórios no Github não tem contagem de livros acima da média
# h1 = Linguagens de programação com mais de 30.000 repositórios no Github tem contagem de livros acima da média
