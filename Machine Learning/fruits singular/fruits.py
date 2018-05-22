def Fruits():
    from sklearn import tree
    weight=int(input('\nenter the weight of the fruit: '))
    print('The texture of the fruit: \n\t\t 1. smooth \n\t\t 2. bumpy \n\t\t 3. thorny \n\t\t 4. velvet \n')
    o_texture=input('enter the texture of the fruit: ')
    size=input('is the size of the fruit is "small" or "medium" or "big": ')
    print('The shape of the fruits: \n\t\t 1. sphere \n\t\t 2. elliptical cylinder \n\t\t 3. ovaloid \n')
    shape=input('\nenter the shape of the fruit: ')
    print('The outer colur is: \n\t\t 1. dark red \n\t\t 2. orange \n\t\t 3. green \n\t\t 4. yellow \n\t\t 5. violet \n\t\t 6. mud brown \n')
    o_color=input('enter anyone of the above outer colour of the fruit: ')
    print('The inner colour is: \n\t\t 1. pale white \n\t\t 2. orange \n\t\t 3. pale yellow \n\t\t 4. pale green \n\t\t 5. violet \n\t\t 6. green \n\t\t 7. white \n\t\t 8. yellow \n\t\t 9. pale brown \n')
    i_color=input('enter the inner colour from the above: ')
    


    if 'smooth' in o_texture:
        a=0
    elif 'bumpy' in o_texture:
        a=1
    elif 'thorny' in o_texture:
        a=2
    elif 'velvet' in o_texture:
        a=3

    if 'small' in size:
        b=0
    elif 'medium' in size:
        b=1
    elif 'big' in size:
        b=2

    if 'sphere' in shape:
        c=0
    if 'elliptical' in shape:
        c=1
    if 'ovaloid' in shape:
        c=2

    if 'dark red' in o_color:
        d=0
    elif 'orange' in o_color:
        d=1
    elif 'green' in o_color:
        d=2
    elif 'yellow' in o_color:
        d=3
    elif 'violet' in o_color:
        d=4
    elif 'brown' in o_color:
        d=5

    if 'pale white' in i_color:
        e=0
    elif 'orange' in i_color:
        e=1
    elif 'pale yellow' in i_color:
        e=2
    elif 'pale green' in i_color:
        e=3
    elif 'violet' in i_color:
        e=4
    elif 'green' in i_color:
        e=5
    elif 'white' in i_color:
        e=6
    elif 'yellow' in i_color:
        e=7
    elif 'pale brown' in i_color:
        e=8

    #           +---------------------------------------------------------------------------+
    #feature    | weight     outer_texture     size    shape   outer_color     inner_color | 
    features = [[   50,          0,              1,      0,         0,              0       ],
                [   60,          0,              1,      0,         0,              0       ],
                [   70,          0,              1,      0,         0,              0       ],
                [   80,          0,              1,      0,         0,              0       ],
                [   90,          0,              1,      0,         0,              0       ],
                [   100,         0,              1,      0,         0,              0       ],
                [   110,         0,              1,      0,         0,              0       ],
                [   120,         0,              1,      0,         0,              0       ],
                [   130,         0,              1,      0,         0,              0       ],
                [   140,         0,              1,      0,         0,              0       ],
                [   150,         0,              1,      0,         0,              0       ],
                [   160,         0,              1,      0,         0,              0       ],
#                [   150,         1,              1,      0,         1,              1       ],
#                [   160,         1,              1,      0,         1,              1       ],
#                [   170,         1,              1,      0,         1,              1       ],
#                [   180,         1,              1,      0,         1,              1       ],
#                [   190,         1,              1,      0,         1,              1       ],
#                [   200,         1,              1,      0,         1,              1       ],
#                [   210,         1,              1,      0,         1,              1       ],
#                [   220,         1,              1,      0,         1,              1       ],
#                [   150,         1,              1,      0,         1,              1       ]]
#                [180, 1, 1, 1],
#                [190, 1, 1, 1],
#                [200, 1, 1, 1],
#                [110, 1, 2, 0],
#                [120, 1, 2, 0],
#                [130, 1, 2, 0],
#                [140, 1, 2, 0],
#                [150, 1, 2, 0],
#                [160, 1, 2, 0],
#                [170, 1, 2, 0],
#                [180, 1, 2, 0],
#                [190, 1, 2, 0],
#                [200, 1, 2, 0],
#                [40,  0, 3, 2],
#                [50,  0, 3, 2],
#                [60,  0, 3, 2],
#                [70,  0, 3, 2],
#                [80,  0, 3, 2]]   #the 0 is smooth and 1 is bumpy
    
    labels = [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]   #the 0 is apple and 1 is orange
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels)
    rst = clf.predict([[a, b, c, d, e]])

    print('\n +----------------+ ')
    if 0 in rst:
        print(' | its Apple      |')
    elif 1 in rst:
        print(' | its Orange     |')
    print(' +----------------+ ')

Fruits()
