def square(x, y):
     lists=[]
    for i in range (x,y+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists 
print(square(1,20))
