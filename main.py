from lib.process_data import dataset

descriptive_statistics = dataset.filter(
    ['languageRank', 'numberOfUsers', 'numberOfJobs', 'tiobe.currentRank'])

print(descriptive_statistics.agg(
    ['mean', 'median', 'min', 'max', 'std', 'var']
))
