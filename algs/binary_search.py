def b_search(seq, t):
    l = 0; r = len(seq)
    while l <= r:
        mid = l + (r - l) // 2
        if seq[mid] > t:
            r = mid-1
        elif seq[mid] < t:
            l = mid+1
        else:
            return seq[mid]
    return -1