number=int(input("enter the number"))
sum=0
while(number>0):
  remainder=number%10
  sum=sum+remainder
  number=number//10
print("\n sum of the digit of the given number=%d" %sum)
