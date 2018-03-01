r=int(input("enter the number"))
for a in range(2,r+1):
  k=o
  for i in range(2,a//2+1):
    if(a%i==0):
      k=k+1
  if(k<=0):
      print(a)
