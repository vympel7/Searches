from typing import TypeVar, Sequence, Dict, overload

N = TypeVar("N", int, float)

@overload
def j_search(seq: Dict[str, N], t: N) -> int: ...
@overload
def j_search(seq: Sequence[N], t: N) -> int: ...