import collections
g = 'tkhiuiguguygiugiiiogigikgdfsfa'
h = collections.defaultdict(int)
for c in g:
    h[c] += 1
for c in sorted(h, key=h.get, reverse=True):
  if h[c] > 1:
      print('%s %d' % (c, h[c]))
