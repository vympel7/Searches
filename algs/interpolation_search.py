def i_search(seq, t):
    """
        Performs interpolation search on an ordered array of numbers.

        Cases:
        Best - O(1)
		Average - O(log log n)
		Worst - O(n)
    """
	l, r = 0, len(seq) - 1
	while seq[r] != seq[l] and seq[l] <= t <= seq[r]:
		mid = l + (t - seq[l]) * (r - l) // (seq[r] - seq[l])
		if t == seq[mid]:
			return mid
		elif t < seq[mid]:
			r = mid - 1
		else:
			l = mid + 1
	if t == seq[l]:
		return l
	return -1
