import collect
s='dsfsafdfsafseff'
d=collect.default dict(int)
for c in s:
 d[c]+=1
for c in sorted(d,key=get reverse=true):
    if(d[c]>1):
      print(%s%d,%(c,c[d]))
