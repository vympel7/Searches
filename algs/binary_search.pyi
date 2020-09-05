from typing import TypeVar, Sequence, Dict, overload

N = TypeVar("N", int, float)

@overload
def b_search(seq: Dict[str, N], t: N) -> int: ...
@overload
def b_search(seq: Sequence[N], t: N) -> int: ...