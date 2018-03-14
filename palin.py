my_str=str(input("enter the number"))
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("yes")
else:
    print("no") 
