# Searches
Search algorithms for python.

### Algorithms
- [x] Binary search
- [x] Jump search
- [x] Interpolation search
- [x] Exponential search
- [x] Fibonacci search

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

array = [3, 4, 6, 9, 11, 14, 21, 36]
result = e_search(array, 21)
print(result)

array = [1, 2, 5, 9, 17, 28, 35, 41]
result = f_search(array, 17)
print(result)
```  

```shell
4
-1
7
6
4
```

#### Note
These algorithms only work if the input sequence is sorted.  
When the input sequence is a dictionary, these algorithms will search in the values.  
Value -1 is returned when target is not found.