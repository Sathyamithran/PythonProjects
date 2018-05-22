j=1
while j==1:
    print("\nDo you want to identify what type of fruit....")
    print("then answer few questions to find it out....\n\n Let's start....")
    print('\nis it a single fruit or bunch of furits: ')
    z=input('type "1" for single, "bunch" for bunch: ')
    if '1' in z:
        y=input('\nis the fruit is "big" or "small": ')
        if 'big' in y:
            from PineappleOrPapayaOrChiku import PineappleOrPapayaOrChiku
            PineappleOrPapayaOrChiku()
        else:
            from AppleOrOrangeOrMosambiOrLemon import AppleOrOrangeOrMosambiOrLemon
            AppleOrOrangeOrMosambiOrLemon()
    else:
        from GrapeOrBanana import GrapeOrBanana
        GrapeOrBanana()





    k=input('\ndo you want to continue: ')
    if k=='y':
        j=1
    else:
        j=0
