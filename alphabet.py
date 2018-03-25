import collections
x = 'tkhiuiguguygiugiiiogigikgdfsfa'
y = collections.defaultdict(int)
for c in x:
    y[c] += 1
for c in sorted(y, key=y.get, reverse=True):
  if y[c] > 1:
      print('%s %d' % (c, y[c]))
