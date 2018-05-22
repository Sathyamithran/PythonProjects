from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target
                                                        #   ||==============||
from sklearn.cross_validation import train_test_split   #   \/              ||
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5) # ||======= it is to take half of datas for training and half for testing
                                                                          #           i.e. iris has 150 datas [75 for training and 75 for testing]

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)
print(predictions)