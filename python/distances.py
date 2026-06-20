# Task 3: Vectorized Pairwise Distances. See ../python.md for the full task.
# Complete the `fast` function below, then run this file:  python distances.py
# It should print:  Match: True

import numpy as np


def slow(a, b):
    # Reference implementation — do NOT modify.
    n, m = len(a), len(b)
    out = [[0.0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            total = 0.0
            for k in range(len(a[i])):
                diff = a[i][k] - b[j][k]
                total += diff * diff
            out[i][j] = total
    return out


def fast(a, b):
    # TODO: return the same result as slow(a, b), using only NumPy operations
    # here — no `for` loops or list comprehensions.
    raise NotImplementedError("Implement fast() using NumPy broadcasting.")


if __name__ == "__main__":
    a = np.array([[0, 0], [3, 4], [1, 2]])
    b = np.array([[0, 0], [1, 1]])
    print("Match:", np.allclose(np.array(slow(a, b)), fast(a, b)))
