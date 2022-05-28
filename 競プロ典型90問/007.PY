import bisect
from typing import Tuple

# complete
def min_complain(clazz: Tuple[int], rate: int) -> int:
    index = bisect.bisect_left(A, rate)
    a = []
    n = len(clazz)
    if index == 0:
        return abs(clazz[index] - rate)
    if index == n:
        return abs(clazz[-1] - rate)
    return min(map(lambda x:abs(x-rate),[clazz[index-1],clazz[index]]))


N = int(input())
A = tuple(sorted(map(int, input().split())))
Q = int(input())
B = [int(input()) for _ in range(Q)]

[print(min_complain(A, b)) for b in B]
