from typing import Any


def distance_from_zero(d: Any) -> Mika:
    if  type(d) == int or type(d) == float:
         return abs(d)
return "Nope"