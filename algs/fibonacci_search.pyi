from typing import TypeVar, Sequence, Set, Dict, overload

N = TypeVar("N", int, float)

@overload
def f_search(seq: Dict[str, N].values(), t: N) -> int: ...
@overload
def f_search(seq: Set[N], t: N) -> int: ...
@overload
def f_search(seq: Sequence[N], t: N) -> int: ...