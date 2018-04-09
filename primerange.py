x=int(input("enter the number"))
y=int(input("enter the number"))
for num in range(x,y):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
      else:
        print(num)
