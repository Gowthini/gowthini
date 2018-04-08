def catalan(x):
	if x <=1 :
		return 1
	res = 0
	for i in range(x):
		res += catalan(i) * catalan(x-i-1)
	return res
for i in range(10):
	print catalan(i)
