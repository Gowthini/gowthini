a=int(input("enter the t1 hour"))
b=int(input("enter the t1 minute"))
c=int(input("enter the t2 hour"))
d=int(input("enter the t2 minute"))
e=a*60+b
f=c*60+d
g=e-f
print(g//60,g%60)
