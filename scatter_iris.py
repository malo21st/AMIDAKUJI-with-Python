from sklearn.datasets import load_iris
import pandas as pld
import mglearn
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], test_size=0.3, random_state=0)

#print(iris_dataset['DESCR'])
#print(iris_dataset.keys())

iris_dataframe = pld.DataFrame(x_train, columns=iris_dataset.feature_names)

grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins':20}, s=60, alpha=8, cmap=mglearn.cm3)
plt.show()
