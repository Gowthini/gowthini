r = [11, 65, 2, 3, 1, 2, 4, 5]

x= int(input("Enter number to search: "))

found = False

for i in range(len(r)):
 if(r[i] == x):
  found = True
  print("%d found at %dth position"%(x,i))
  break
 
if(found == False):
 print("%d is not in list"%x)
