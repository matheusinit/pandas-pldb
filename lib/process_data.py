import pandas

raw_dataset = pandas.read_csv(
    "~/Development/pandas-pldb/pldb.csv", low_memory=False)

raw_dataset = raw_dataset.query('numberOfUsers > 0')
raw_dataset = raw_dataset.query('numberOfJobs > 0')

# Make categorical the column


def makeNonNumericalColCategorical(dataset, column):
    col = dataset[column].values.tolist()
    categoricalCol = pandas.factorize(col)[0]

    return categoricalCol


raw_dataset = raw_dataset.filter([
    'title',
    'originCommunity',
    'bookCount',
    'githubLanguage.repos',
    'type'
]).dropna()

dataset = raw_dataset.copy(deep=True)
# dataset = dataset.query("type == 'pl'")

dataset['title'] = makeNonNumericalColCategorical(dataset, "title")

dataset['originCommunity'] = makeNonNumericalColCategorical(
    dataset, "originCommunity")
