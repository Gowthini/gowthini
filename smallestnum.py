x=int(input("enter number"))
y=[]
for i in range(0,x):
  c=int(input())
  y.append(c)
y.sort()
s=int(input("enter s"))
print(y[s-1])
