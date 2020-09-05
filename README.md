# Searches
Search algorithms for python.

### Algorithms
- [x] Binary search
- [x] Jump search
- [x] Interpolation search
- [ ] Exponential search
- [ ] Fibonacci search

### Use example
```python
from algs import *

array = [1, 3, 4, 6, 7, 9, 13]
result = b_search(array, 7)
print(result)

array = [0, 3, 5, 8, 11, 15, 23]
result = j_search(array, 7)
print(result)

array = [2, 3, 4, 4, 6, 8, 11, 16, 25]
result = i_search(array, 16)
print(result)
```  

```shell
4
-1
7
```

#### Note
These algorithms only work if the array is sorted.  
Value -1 is returned when target is not found.