import sys
def aaa(st,low,high) :
	sys.stdout.write(st[low : high + 1])
	sys.stdout.flush()
	return ''
def hhh(st) :
	n = len(st) 
	table = [[0 for x in range(n)] for y in range(n)]
	maxLength = 1
	i = 0
	while (i < n) :
		table[i][i] = True
		i = i + 1
	start = 0
	a = 0
	while a < n - 1 :
		if (st[a] == st[a + 1]) :
			table[a][a + 1] = True
			start = a
			maxLength = 2
		a = a + 1
	m = 3
	while m <= n :
		a = 0
		while a < (n - m + 1) :
			j = a + m - 1
			if (table[a + 1][j - 1] and
					st[a] == st[j]) :
				table[a][j] = True
				if (m > maxLength) :
					start = a
					maxLength = m
			a = a + 1
		m = m + 1
	print "Longest palindrome substring is: ",(st, start,start + maxLength - 1)
	return maxLength

st = "madam malayalam"
l = hhh(st)
print "Length is:", l
