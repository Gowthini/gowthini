x=str(input("enter the string"))
x=x.split()
x=list(map(lambda x:x.capitalize(),x))
b=' '.join(x)
print(b)
