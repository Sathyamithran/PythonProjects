from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree


iris = load_iris()


##### Import DataSet IRIS
#print(iris.feature_names)<----------flower's petal length,width and sepal length,width
#print(iris.target_names) <--------flower names inthe target column

#print(iris.data[0],iris.target[0])<----------printing the first column in the table

#to print entire iris dataset
#print('sl.no\t\tdatas\t\t\ttarget')
#for i in range(len(iris.target)):
#    print(i,'\t',iris.data[i],'\t\t',iris.target[i])

test_idx = [0,50,100] #<------------------removing 1st row of data for three types of flower
#training data<------which has all data except testing data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
#             |
#             |
#             +--------------------------------------+
#testing data<------which has all the 1st columns    |
test_target = iris.target[test_idx]   #              |   
test_data = iris.data[test_idx]       #              |
#                                                    |
#                                                    |
clf = tree.DecisionTreeClassifier()  #<--------------+
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))


