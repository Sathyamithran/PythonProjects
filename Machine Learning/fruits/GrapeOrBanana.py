def GrapeOrBanana():
    from sklearn import tree
    a=int(input('\nenter the weight of the fruit: '))
    b=input('is the Shape is sphere or elliptic cylinder: ')
    d=input('is the color is yellow or green/violet: ')
    if 'sphere' in b:
        c=0
    else:
        c=1
    if 'green' in d:
        e=0
    elif 'violet' in d:
        e=0
    else:
        e=1
    features = [[20, 0, 0],
                [30, 0, 0],
                [40, 0, 0],
                [50, 0, 0],
                [80, 0, 1],
                [90, 1, 1],
                [100, 1, 1],
                [110, 1, 1],
                [120, 1, 1],
                [130, 1, 1]]   ##the [#1,#2,#3] #1 is weight ,#2 is shape, #3 is color
    
    labels = [0,0,0,0,1,1,1,1,1,1]   #the 0 is apple and 1 is orange
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels)
    rst = clf.predict([[a, c, e]])

    print('\n +----------------+ ')
    if 0 in rst:
        print(' | its Grapes     |')
    else:
        print(' | its Banana     |')
    print(' +----------------+ ')

#GrapeOrBanana()        
