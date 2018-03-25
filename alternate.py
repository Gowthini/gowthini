def gh(m, k):
	m.sort() 
	i = 0
	j = k-1
	while (i < j): 
		print(m[j], end =" ")
		j-= 1
		print(m[i], end =" ")
		i+= 1
	if (k % 2 != 0):
		print(m[i]) 
m = [10, 102, 49, 86, 757, 105] 
k = len(m)
gh(m, k)
