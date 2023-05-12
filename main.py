import pandas

dataset = pandas.read_csv("pldb.csv")

dataset = dataset.query('numberOfUsers > 0')
dataset = dataset.query('numberOfJobs > 0')
dataset = dataset.query("type == 'pl'")

dataset = dataset.filter([
    'title',
    'type',
    'languageRank',
    'numberOfUsers',
    'numberOfJobs',
    'tiobe.currentRank',
])
git
descriptive_statistics = dataset.filter(
    ['languageRank', 'numberOfUsers', 'numberOfJobs', 'tiobe.currentRank'])

print(descriptive_statistics.agg(
    ['mean', 'median', 'min', 'max', 'std', 'var']
))

# print(min_numberOfUsers)
