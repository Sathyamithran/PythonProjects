from sklearn import datasets #importing the predefined dataset
iris = datasets.load_iris()  #this is where importing IRIS dataset is done

x = iris.data     # 'x' stores the features of the iris
y = iris.target   # 'y' stores the labels of the iris

from sklearn.cross_validation import train_test_split  #we are going to split the entire 150 datas in IRIS dataset into two halves...1. 75 datas for training and 2. 75 datas for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5) # 'x_train' , 'y_train' has the feature and labels for training datas and 'x_test' , 'y_test' has the feature and labels for testing the datas

#####create a Classfier

## 1st decision tree
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)
print (predictions)
