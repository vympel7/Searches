from typing import TypeVar, Sequence, Set, Dict, overload

N = TypeVar("N", int, float)

@overload
def b_search(seq: Dict[str, N], t: N) -> N: ...
@overload
def b_search(seq: Set[N], t: N) -> N: ...
@overload
def b_search(seq: Sequence[N], t: N) -> N: ...