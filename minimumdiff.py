def x(r, size):
	y = r[1] - r[0]
	for i in range( 0, size ):
		for j in range( i+1, size ):
			if(r[j] - r[i] < y): 
				y = r[j] - r[i]
	return y
r = [15, 22, 65, 70, 119]
size1 = len(r)
print ("Maximum difference is", x(r, size1))
