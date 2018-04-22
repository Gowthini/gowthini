def findSingle( ax, y):
    res = x[0]
    for i in range(1,y):
        res = res ^ x[i]
    return res
 x = [2, 3, 5, 4, 5, 3, 4]
print "Element occuring once is", findSingle(x, len(x))
