import pandas as pd

test = pd.read_csv('data/test.csv')

print(test.shape)
print(test.head(10))
print(test.isnull().sum())

print(test.info)