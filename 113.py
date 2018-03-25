s = [11567, 675, 26, 37, 1, 2, 4, 5]

y = int(input("Enter number to search: "))

found = False

for i in range(len(s)):
 if s[i] == y:
  found = True
  print("%d found at %dth position"%(yi))
  break
 
if(found == False):
 print("%d is not in list"%y)
