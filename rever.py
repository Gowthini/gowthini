number=int(input("enter the number"))
reverse=0
while(number>0):
    remainder=number%10
    reverse=(reverse*10)+remainder
    number=number//10
print("reverse of entered number is =%d"%reverse)
