MAX_CHARS = 256
def areIsomorphic(string1, string2):
    x = len(string1)
    y = len(string2)
    if x != y:
        return False
    marked = [False] * MAX_CHARS
    map = [-1] * MAX_CHARS
    for i in xrange(y):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return False
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return False
    return True
print areIsomorphic("a","x")
print areIsomorphic("aab","x")
