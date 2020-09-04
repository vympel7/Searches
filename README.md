# Searches
Search algorithms for python.

### Algorithms
- [x] Binary search
- [x] Jump search
- [ ] Interpolation search
- [ ] Exponential search
- [ ] Fibonacci search

### Use example
```python
from algs import *

array = [1, 3, 4, 6, 7, 9, 13]
result = b_search(array, 7)
print(result)
```  
```python
from algs import *

array = [0, 3, 5, 8, 11, 15, 23]
result = j_search(array, 7)
print(result)
```  

```shell
4
-1
```

#### Note
These algorithms only work if the array is sorted.