n=['a','e','i','o','u']
x=input("enter the string")
l=[]
for i in range(len(x)):
    if x[i] not in n:
        l.append(x[i])
y=l[::-1]
print(str(y))
