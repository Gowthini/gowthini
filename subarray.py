def ll(m):
	n = len(m)
	ss = 1
	pp = 1
	gg = 1
	for i in range(0,n):
		if m[i] > 0:
			ss = ss*m[i]
			pp = min (pp * m[i], 1)
		elif m[i] == 0:
			ss = 1
			pp = 1
		else:
			temp = ss
			ss = max (pp * m[i], 1)
			pp = temp * m[i]
		if (gg < ss):
			gg = ss
	return gg
m = [9, -5, 4, -1, 3, 6,-8]
print "Maximum product subarray is:",ll(m)
