x=int(input("Enter a number"))
sum=0
while(x>0):
  dig=x%10
  sum=sum+(dig*dig)
  x=x//10
print(sum)
