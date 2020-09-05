def b_search(seq, t):
    """
        Performs binary search on an ordered array of numbers.

        Cases:
        Best - O(1)
        Average - O(log n)
        Worst - O(log n)
    """
    l = 0; r = len(seq)-1
    while l <= r:
        mid = l + (r - l) // 2
        if seq[mid] == t:
            return mid
        if seq[mid] > t:
            r = mid-1
        elif seq[mid] < t:
            l = mid+1
    return -1