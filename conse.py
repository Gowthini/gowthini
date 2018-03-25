from sets import Set
def conseq(s, n):
	x = Set()
	t=0
	for ele in p:
		x.add(ele)
	for i in range(n):
		if (p[i]-1) not in x:
			j=p[i]
			while(j in x):
				j+=1
			t=max(t, j-p[i])
	return t 
if __name__=='__main__':
	n = 7
	s = [1, 8, 6, 17, 4, 248, 2]
	print "Length of the Longest contiguous subsequence is ", 
	print conseq(s, n)
