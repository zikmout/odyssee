from sklearn.datasets import load_iris
iris = load_iris()

iris.keys()

#dict_keys(['DESCR', 'data', 'target_names', 'feature_names', 'target'])

print(iris['DESCR'][:193])

print(iris['target_names'])

print(iris['target'])
