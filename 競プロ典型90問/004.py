from functools import lru_cache
from itertools import chain

#complete
H, W = map(int, input().split())
A = chain.from_iterable([map(int, input().split()) for i in range(H)])
A = tuple(A)


@lru_cache(maxsize=None)
def w_line(h_i: int, w: int):
    start, end = h_i * w, h_i * w + w
    return sum(A[start:end])


@lru_cache(maxsize=None)
def h_line(w_i: int, w: int, h: int):
    t_idx = [i * w + w_i for i in range(h)]
    return sum([A[i] for i in t_idx])


B = [w_line(i // W, W) + h_line(i % W, W, H) - v for i, v in enumerate(A)]
for i in range(H):
    print(' '.join(map(str, B[i * W:(i + 1) * W])))
