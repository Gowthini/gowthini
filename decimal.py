def bbTod(binarys):
    binary1 = binarys
    decimal, i, n = 0, 0, 0
    while(binarys != 0):
        dec = binarys % 10
        decimal = decimal + dec * pow(2, i)
        binarys = binarys//10
        i += 1
    print(decimal)    
if __name__ == '__main__':
    bbTod(100)
    bbTod(101)
    bbTod(1001)
