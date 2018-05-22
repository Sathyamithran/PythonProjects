def AppleOrOrangeOrMosambiOrLemonOrChiku():
    from sklearn import tree
    a=int(input('\nenter the weight of the fruit: '))
    b=input('is the texture is "smooth" or "bumpy" or "velvet": ')
    d=input('is the outer colur is "dark red" or "orange" or "green" or "yellow" or "mud brown": ')
    f=input('is the inner colour is "pale white" or "orange" or "pale yellow" or "pale brown": ')
    
    if 'smooth' in b:
        c=0
    elif 'bumpy' in b:
        c=1
    elif 'velvet' in b:
        c=2

    if 'red' in d:
        e=0
    elif 'orange' in d:
        e=1
    elif 'green' in d:
        e=2
    elif 'yellow' in d:
        e=3
    elif 'brown' in d:
        e=4

    if 'white' in f:
        g=0
    elif 'orange' in f:
        g=1
    elif 'yellow' in f:
        g=2
    elif 'brown' in f:
        g=3
        
    features = [[50,  0, 0, 0],
                [60,  0, 0, 0],
                [70,  0, 0, 0],
                [80,  0, 0, 0],
                [90,  0, 0, 0],
                [100, 0, 0, 0],
                [110, 1, 1, 1],
                [120, 1, 1, 1],
                [130, 1, 1, 1],
                [140, 1, 1, 1],
                [150, 1, 1, 1],
                [160, 1, 1, 1],
                [170, 1, 1, 1],
                [180, 1, 1, 1],
                [190, 1, 1, 1],
                [200, 1, 1, 1],
                [110, 1, 2, 0],
                [120, 1, 2, 0],
                [130, 1, 2, 0],
                [140, 1, 2, 0],
                [150, 1, 2, 0],
                [160, 1, 2, 0],
                [170, 1, 2, 0],
                [180, 1, 2, 0],
                [190, 1, 2, 0],
                [200, 1, 2, 0],
                [40,  0, 3, 2],
                [50,  0, 3, 2],
                [60,  0, 3, 2],
                [70,  0, 3, 2],
                [80,  0, 3, 2],
                [50,  2, 4, 3],
                [60,  2, 4, 3],
                [70,  2, 4, 3],
                [80,  2, 4, 3],
                [90,  2, 4, 3],
                [100, 2, 4, 3],
                [110, 2, 4, 3]]   #the 0 is smooth and 1 is bumpy
    
    labels = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4]   #the 0 is apple and 1 is orange
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels)
    rst = clf.predict([[a, c, e, g]])

    print('\n +----------------+ ')
    if 0 in rst:
        print(' | its Apple      |')
    elif 1 in rst:
        print(' | its Orange     |')
    elif 2 in rst:
        print(' | its Mosambi    |')
    elif 3 in rst:
        print(' | its Lemon      |')
    elif 4 in rst:
        print(' | its Chiku      |')
    print(' +----------------+ ')

#AppleOrOrangeOrMosambiOrLemonOrChiku()
