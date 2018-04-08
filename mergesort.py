def ppp(x, y, res, n, m):
	i, j, k = 0, 0, 0
	while (i < n):
		res[k] = x[i]
		i += 1
		k += 1
	while (j < m):
		res[k] = y[j]
		j += 1
		k += 1
	res.sort()
x = [ 70, 52, 5 ]
y = [ 70, 13, 32, 13 ]
n = len(x)
m = len(y)
res = [0 for i in range(n + m)]
ppp(x, y, res, n, m)
print "Sorted merged list :"
for i in range(n + m):
	print res[i],
