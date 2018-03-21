def hrk(r,n,k):
    count=0
    for i in range(0,n):
    for j in range(i+1,n):
      if((r[i]-r[j]==k)
      count+=1
      return count
 r=[1,4,6,4,5,3,7]
 n=len(r)
 k=3
 print("count of pairs",hrk(r,n,k))
