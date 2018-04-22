x=int(input("enter a number"))
y=int(input("enter a number"))
for i in range(2,1000):
    if x%i==0 and y%i==0:
        break
print(i)
