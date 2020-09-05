from typing import TypeVar, Sequence, Set, Dict, overload

N = TypeVar("N", int, float)

@overload
def i_search(seq: Dict[str, N].values(), t: N) -> int: ...
@overload
def i_search(seq: Set[N], t: N, step: int = 0) -> int: ...
@overload
def i_search(seq: Sequence[N], t: N) -> int: ...