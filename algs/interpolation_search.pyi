from typing import TypeVar, Sequence, Dict, overload

N = TypeVar("N", int, float)

@overload
def i_search(seq: Dict[str, N], t: N) -> int: ...
@overload
def i_search(seq: Sequence[N], t: N) -> int: ...