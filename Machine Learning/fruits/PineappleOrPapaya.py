def PineappleOrPapaya():
    
    from sklearn import tree
    a=int(input('\nenter the weight of the fruit: '))
    b=input('is the texture is "thorny" or "smooth": ')
    print('is it has leaves on top?')
    d=input('type y for yes and n for no: ')
    f=input('is the inner colur is "yellow" or "orange": ')

    if 'thorny' in b:
        c=0
    elif 'smooth' in b:
        c=1

    if 'y' in d:
        e=0
    else:
        e=1

    if 'yellow' in f:
        g=0
    elif 'orange' in f:
        g=1

    features = [[200, 0, 0, 0],
                [210, 0, 0, 0],
                [220, 0, 0, 0],
                [250, 0, 0, 0],
                [270, 0, 0, 0],
                [300, 0, 0, 0],
                [150, 1, 1, 1],
                [160, 1, 1, 1],
                [170, 1, 1, 1],
                [180, 1, 1, 1],
                [190, 1, 1, 1],
                [200, 1, 1, 1]] #in (#1,#2,#3) #1 say about weight, #2 says about texture, #3 says about leaf on it or not
    
    labels = [0,0,0,0,0,0,1,1,1,1,1,1]   #the 0 is pineapple and 1 is papaya
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels)
    rst = clf.predict([[a, c, e, g]])

    print('\n +----------------+ ')
    if 0 in rst:
        print(' | its Pineapple  |')
    elif 1 in rst:
        print(' | its Papaya     |')
    print(' +----------------+ ')

#PineappleOrPapaya()
