def f_search(seq, t):
    """
        Performs fibonacci search on an ordered array of numbers.

        Cases:\n
        Best - O(1)\n
        Average - O(log n)\n
        Worst - O(log n)
    """
    if type(seq) == dict:
        seq = list(seq.values())
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m1 + fib_m2
    while (fib_m < len(seq)):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m1 + fib_m2
    index = -1
    while (fib_m > 1):
        i = min(index + fib_m2, (len(seq)-1))
        if (seq[i] < t):
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            index = i
        elif (seq[i] > t):
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else :
            return i
    if(fib_m1 and index < (len(seq)-1) and seq[index+1] == t):
        return index+1
    return -1