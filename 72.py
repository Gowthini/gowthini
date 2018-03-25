def uk(x, low, high, y):
	mid = low + (high - low)/2
	mid = int(mid)
	if ((mid == 0 or x[mid - 1] <= x[mid]) and
	(mid == n - 1 or x[mid + 1] <= x[mid])):
		return mid
	elif (mid > 0 and x[mid - 1] > x[mid]):
		return uk(x, low, (mid - 1), y)
	else:
		return uk(x, (mid + 1), high, y)
def Peak(x, y):
	return uk(x, 0, y - 1, y)
x = [1, 3, 20, 4, 1, 0]
y = len(x)
print("Index of a peak point is", Peak(x, y))
