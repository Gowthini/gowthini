def findmean(a,n):
  sum=0
  for i in range(0,n):
    sum+=a[i]
 return flaot(sum/n)
def findmedian(a,n):
  sorted(a)
  if n%2=0:
    return float(a[n/2])
  return flaot((a[int((n-1)(2)]+a[int(n/2)])/2.0)
a=[1,3,4,2,7,5,8,6]
n=len(a)
print("median",findmedian(a,n))
