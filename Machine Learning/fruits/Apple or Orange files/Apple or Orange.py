from sklearn import tree
#data 1---------------------

e=''


try:
    d=range(1,201)
    a=int(input('enter the weight of the fruit: ')) 
    if a in d:
        a=a
    else:
        a=0
        e=' An average fruit weight is about 100 - 250 g '

except ValueError:
    #e='you have to write a number'
    a=0
finally:
    print(e)

#data 2-----------------------
    
b=input('is the texture is smooth or bumpy: ')
if 'smooth' in b:
    c=0
elif 'bumpy' in b:
    c=1
else:
    c=2



#dataset training data------------------------
features = [[50, 0],[60, 0],[70, 0],[80, 0],[90, 0],[100, 0],[110, 1],[120, 1],[130, 1],[140, 1],[150, 1],[160, 1],[170, 1],[180, 1],[190, 1],[200, 1]]   #the 0 is smooth and 1 is bumpy
labels = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]        #the 0 is apple and 1 is orange

#tree making----------------------------------------
clf = tree.DecisionTreeClassifier()

#training algorithm
clf = clf.fit(features,labels)

#prediction------------------------------
rst = clf.predict([[a, c]])
if 1 in rst:
    print('\nits Orange')
elif 0 in rst:
    print('\nits Apple')
else:
    print('\nBoo...you have entered the data wrongly.......')

