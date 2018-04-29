def changeCap(str):
    for i in range(len(str)):
        if str[i].islower():
            print(str[i].upper())
        else:
            print(str[i].lower())
changeCaps("EXAMINation")
