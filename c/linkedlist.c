// C-2: Singly linked list of int with malloc/free. See ../c.md for the full task.
// Replace this comment with a one-sentence description of how prepend allocates
// and links a node, and how free_list avoids leaks and use-after-free.
//
// Graded with: gcc -Wall -Wextra -fsanitize=address -g -o linkedlist c/linkedlist.c && ./linkedlist

#include <stdio.h>
#include <stdlib.h>

// TODO: define a `node` struct holding an `int value` and a pointer to the next node.

// TODO: node *prepend(node *head, int value)
//       allocate a new node with malloc, store value, link it at the front,
//       and return the new head.

// TODO: a function that prints the list in order (e.g. "3 -> 2 -> 1").

// TODO: void free_list(node *head)  — free every node, leak-free.

int main(void)
{
    // TODO: starting from an empty list, use prepend to build 3 -> 2 -> 1,
    // print it, then free the whole list.
    return 0;
}
