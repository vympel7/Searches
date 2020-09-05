from .binary_search import b_search
def e_search(seq, t):
    """
        Performs exponential search on an ordered array of numbers.

        Cases:\n
        i is the index of the target element\n
        Best - O(1)\n
        Average - O(log i)\n
        Worst - O(log i)
    """
    if seq[0] == t:
        return 0
    i = 1
    while i < len(seq) and seq[i] <= t: 
        i *= 2
    return b_search(seq[:min(i, len(seq))], t)