print("fibonacci series")
n=int(input("enter limit"))
f1=0
print(f1)
f2=1
print(f2)
for i in range(n-1):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
