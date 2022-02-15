import seaborn as sns

print(sns.get_dataset_names())

data_titanic = sns.load_dataset('titanic')
print(data_titanic)