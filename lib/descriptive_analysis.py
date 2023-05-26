from process_data import dataset

descriptive_dataset = dataset.agg(
    ['mean', 'median', 'min', 'max', 'std', 'var']
)

csv = descriptive_dataset.to_csv("output.csv", index=False, header=True)

print("Descriptive Analysis of Dataset")

print(descriptive_dataset)
