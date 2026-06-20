# Python Questions

## 1. Word Frequencies

The provided `python/word_count_input.txt` contains this text:

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

→ Complete `python/word_count.py`

---

## 2. Shapes & Polymorphism

Build a small class hierarchy:

- A base class `Shape` with a method `area(self)` that raises `NotImplementedError`.
- A subclass `Circle(r)` storing radius `r` and overriding `area()` to return $\pi r^2$.
- A subclass `Rectangle(w, h)` storing width `w` and height `h` and overriding `area()` to return $w \cdot h$.
- A `__repr__` on `Shape` (or each subclass) so that printing a shape shows its type and area.

Then, given a list of **mixed** shapes (include at least two circles and two rectangles), use a **single
loop** to print each shape and accumulate the **total area** across all of them. Print the total at the end.

→ Complete `python/shapes.py`

---

## 3. Vectorized Pairwise Distances

**The goal.** Given two sets of points, compute the squared distance from *every* point in the first set to
*every* point in the second — using NumPy **broadcasting** instead of Python loops. (This is the core
operation behind k-nearest-neighbours and a lot of ML code.)

**Inputs.** `a` and `b` are 2D NumPy arrays where each **row is a point**. `a` has shape $n \times d$
($n$ points in $d$ dimensions); `b` has shape $m \times d$ ($m$ points, same dimension $d$).

**Output.** A NumPy array `D` of shape $n \times m$ where `D[i, j]` is the squared Euclidean distance
between row `i` of `a` and row `j` of `b`:

$$D[i,j] = \sum_{k=1}^{d} \left(a_{ik} - b_{jk}\right)^2.$$

**Concrete example.** For

```python
a = np.array([[0, 0], [3, 4], [1, 2]])   # 3 points, shape (3, 2)
b = np.array([[0, 0], [1, 1]])           # 2 points, shape (2, 2)
```

the answer is

```python
D = [[ 0,  2],     # e.g. D[1, 0] = (3-0)**2 + (4-0)**2 = 25
     [25, 13],
     [ 5,  1]]     # shape (3, 2)
```

**Your task.** Open the starter file **`python/distances.py`**. It already contains `slow` (the reference
implementation — don't change it) and a `fast` stub marked `TODO`. Fill in the body of `fast` so it returns
the **same** result as `slow`, using **only NumPy operations — no `for` loops or list comprehensions**.
Then run it (`python python/distances.py`); it should print `Match: True`.

→ Complete `python/distances.py`
