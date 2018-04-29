x=input("enter string")
y=input("enter string")
z=1
for letter in x: 
    if letter in y:
        z=0
        break
if(z==0):
    print("yes")
else:
    print("no")
