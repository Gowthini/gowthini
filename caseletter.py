while True:
	print("Enter 'y' for exit.")
	str = input("Enter any string: ")
	if str == 'y':
		break
	else:
		str_in_lowercase = str.lower()
		print("Str in Lowercase =",str_in_lowercase,"\n")
