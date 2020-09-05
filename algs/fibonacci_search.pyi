from typing import TypeVar, Sequence, Dict, overload

N = TypeVar("N", int, float)

@overload
def f_search(seq: Dict[str, N], t: N) -> int: ...
@overload
def f_search(seq: Sequence[N], t: N) -> int: ...