import seaborn as sns

#print(sns.get_dataset_names())

data_titanic = sns.load_dataset('titanic')
print(data_titanic.head())
print(data_titanic.info())
print(data_titanic.describe()
print(data_titanic.describe(include='0'))

# cara 1 full drof na
# data_titanic_clean

# cara 2 menggunakan kondisi
#khusus sisakan data pria berumur maksimal 30 tahun
data_titanic_clean = data_titanic
data_titanic_clean = data_titanic_clean(data_titanic_clean['sex'] != 'female')
data_titanic_clean = data_titanic_clean(data_titanic_clean['age'] <= 30
print(data_titanic_clean)

#cara 3 memberikan nilai NaN
data_titanic_fill = data_titanic
data_titanic_fill = data_titanic_fill['age'].fillna(value = data_titanic_fill['age'].mean())
print(data_titanic_fill)


                                        
                            