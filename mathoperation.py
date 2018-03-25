print("*****math operations******")
n1=int(input("enter your number"))
n2=int(input("enter your number"))
x=0
while x==0:
  ch=int(input("enetr youroptions"))
  if ch==1:
    print("    addition   ")
    print("the value is",n1+n2)
  elif ch==2:
    print("    subtration   ")
    print("the value is",n1-n2)
  elif ch==3:
    print("    multiplication   ")
    print("the value is",n1*n2)
  elif ch==4:
    print("    division   ")
    print("the value is",n1/n2)
  elif ch==5:
    print("    reminder   ")
    print("the value is",n1%n2)
  else:
    print("invalid")
  x=int(input("enter 0 to continue 1 to exist" ))
