def xx(y):
	left,right = 0,len(r)-1
	while left < right:
		while (y[left]%2==0 and left < right):
			left += 1
		while (y[right]%2 == 1 and left < right):
			right -= 1
		if (left < right):
			y[left],y[right] = y[right],y[left]
			left += 1
			right = right-1
y = [17, 34, 74, 99, 8, 90, 53]
xx(y)
print ("Array after segregation "),
for i in range(0,len(y)):print y[i]
