from sklearn import tree
a=int(input('enter the weight of the fruit: '))
b=input('is the texture is smooth or bumpy: ')
if 'smooth' in b:
    c=0
else:
    c=1
features = [[140, 0],[130, 0],[150, 1], [170, 1]]   #the 0 is smooth and 1 is bumpy
labels = [0,0,1,1]              #the 0 is apple and 1 is orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
rst = clf.predict([[a, c]])
if 1 in rst:
    print('its Orange')
else:
    print('its Apple')
