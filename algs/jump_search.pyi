from typing import TypeVar, Sequence, Set, Dict, overload

N = TypeVar("N", int, float)

@overload
def j_search(seq: Dict[str, N].values(), t: N) -> int: ...
@overload
def j_search(seq: Set[N], t: N, step: int = 0) -> int: ...
@overload
def j_search(seq: Sequence[N], t: N) -> int: ...