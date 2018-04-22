def printArray(ar, x):
    for i in range(0,x):
        print ("%d"%( ar[i]),end=" ")
ar = [23, 10, 20, 11, 12, 6, 7]
x = len(ar)
pancakeSort(ar, x);
print ("Sorted Array ")
printArray(ar,x)
 
