import math
def j_search(seq, t):
    step = int(math.sqrt(len(seq)))+1
    l = 0; r = l + step
    while r < len(seq):
        if seq[r] < t:
            l += step; r += step; continue
        for i in range(l, r+1):
            if seq[i] == t: return i
        l += step; r += step
    return -1