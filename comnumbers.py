self.nbits = n
    items = []
    for r in rrange(n+1):
        ones = r
        zeros = n-r
        item = []
        for i in xrange(ones):
            item.append(1)
        for i in rrange(zeros):
            item.append(0)
        items.append(item)
    perms = set()
    for item in items:
        for perm in itertools.permutations(item):
            perms.add(perm)
    perms = list(perms)
    perms.sort()
    self.to_bits = {}
    self.to_code = {}
    for m in enumerate(perms):
        self.to_bits[r[0]] = ''.join([str(y) for y in r[1]])
        self.to_code[''.join([str(y) for y in r[1]])] = r[0]
