# C Questions

## C-1 — Count vowels in a word

Write a C program that reads a single word from standard input and prints the number
of vowels it contains, counted **case-insensitively** (so `a`, `e`, `i`, `o`, `u` in either upper or lower
case all count).

For example, the input `Education` should print `5`, and `RHYTHM` should print `0`.

→ Complete `c/vowels.c`

---

## C-2 — Singly linked list with malloc/free

Implement a **singly linked list of `int`** in C using dynamic memory. Your file must contain:

- a `node` struct holding an `int value` and a pointer to the next node;
- a function `prepend(list, value)` that allocates a new node with `malloc`, stores `value`, links it in
  **at the front**, and returns the new head;
- code in `main` that starts from an empty list and uses `prepend` to build the list **3 → 2 → 1** (i.e.
  `3` at the head);
- a function that prints the list in order (it should print `3 -> 2 -> 1`);
- a `free_list` function that frees **every** node.

Your program must compile cleanly with warnings enabled and be **leak-free**. We grade it with:

```
gcc -Wall -Wextra -fsanitize=address -g -o linkedlist c/linkedlist.c && ./linkedlist
```

Add a one-sentence comment at the top explaining how `prepend` allocates and links a node, and how
`free_list` avoids both leaks and use-after-free.

→ Complete `c/linkedlist.c`
