# Python Questions

## 1. Word Frequencies

Create a file `python/word_count_input.txt` containing exactly this text:

```
The cat sat on the mat. The cat saw the dog,
and the dog ran. The cat, the cat, the dog and the bird.
A bird sat near the cat while the dog slept.
```

Write a program that:

1. Reads the text from `python/word_count_input.txt`.
2. Builds a dictionary mapping each **lowercased** word to its frequency. Treat words case-insensitively
   (`The` and `the` are the same word) and strip surrounding punctuation so `dog.` and `dog` count as the
   same word.
3. Prints the **3 most frequent** words and their counts, most frequent first.

**Standard library only** (no third-party packages). Choose a sensible, deterministic tie-break if two
words have the same count.

→ Save as `python/word_count.py`

---

## 2. Shapes & Polymorphism

Build a small class hierarchy:

- A base class `Shape` with a method `area(self)` that raises `NotImplementedError`.
- A subclass `Circle(r)` storing radius `r` and overriding `area()` to return $\pi r^2$.
- A subclass `Rectangle(w, h)` storing width `w` and height `h` and overriding `area()` to return $w \cdot h$.
- A `__repr__` on `Shape` (or each subclass) so that printing a shape shows its type and area.

Then, given a list of **mixed** shapes (include at least two circles and two rectangles), use a **single
loop** to print each shape and accumulate the **total area** across all of them. Print the total at the end.

→ Save as `python/shapes.py`

---

## 3. Vectorized Pairwise Distances

Put the reference function below into a file `python/slow_distances.py` (do **not** modify it). It computes,
with nested Python loops, the **squared Euclidean distance** between every row of `a` and every row of `b`:
for 2D arrays `a` (shape $n \times d$) and `b` (shape $m \times d$) it returns an $n \times m$ result whose
entry $(i, j)$ is $\sum_{k} (a_{ik} - b_{jk})^2$.

```python
def slow(a, b):
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
```

Write `def fast(a, b)` that computes the **same** result using **only NumPy broadcasting / vectorization —
no Python `for` loops** in `fast`. Import `slow` from `slow_distances.py`, then verify your implementation
against it with `np.allclose(...)` on a small example and print whether they match.

→ Save as `python/distances.py` (keep `slow_distances.py` alongside it so the import works)
