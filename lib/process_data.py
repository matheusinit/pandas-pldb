import pandas

dataset = pandas.read_csv("~/Projects/data-science/pldb.csv", low_memory=False)

dataset = dataset.query('numberOfUsers > 0')
dataset = dataset.query('numberOfJobs > 0')
dataset = dataset.query("type == 'pl'")

# Make categorical the column  
def makeNonNumericalColCategorical(dataset, column):
    col = dataset[column].values.tolist()
    categoricalCol = pandas.factorize(col)[0]

    return categoricalCol
        

dataset = dataset.filter([
    'title',
    'originCommunity',
    'bookCount',
    'githubLanguage.repos'
]).dropna()

dataset['title'] = makeNonNumericalColCategorical(dataset, "title") 

dataset['originCommunity'] = makeNonNumericalColCategorical(dataset, "originCommunity")

