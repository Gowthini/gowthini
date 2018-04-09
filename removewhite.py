str = input("Enter any string to remove all spaces: ")
if str == 'y':
    exit();
else:
    new_str = str.replace(" ","")
    print("\nNew string after removing all spaces:")
    print(new_str)
