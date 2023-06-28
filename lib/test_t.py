import numpy as np
from scipy import stats
from numpy.random import seed
from numpy.random import randn
from numpy.random import normal
from scipy.stats import ttest_1samp

from process_data import raw_dataset

book_count = raw_dataset[:5].filter(['bookCount'])

print(book_count)

t_stat, p_value = ttest_1samp(book_count, popmean=50)

print("t_stat", t_stat)
print("p_value", p_value)
