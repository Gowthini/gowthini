number=int(input("enter the number"))
if number >1:
    for i in range(2,number):
        if(number%1)==0:
          print(number,"is not a prime")
          break
    else:
        print(number,"is aprime number")
      
