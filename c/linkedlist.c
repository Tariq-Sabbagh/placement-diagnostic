// C-2: Singly linked list of int with malloc/free. See ../c.md for the full task.
// Replace this comment with a one-sentence description of how prepend allocates
// and links a node, and how free_list avoids leaks and use-after-free.
//
// Graded with: gcc -Wall -Wextra -fsanitize=address -g -o linkedlist c/linkedlist.c && ./linkedlist

#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int value;
    struct Node *next;
};

// TODO: node *prepend(node *head, int value)
//       allocate a new node with malloc, store value, link it at the front,
//       and return the new head.

//prepend function in first check if list null (doesn't have nodes) the fun make a head first node else we add new value and make the next node is head.
struct Node *prepend(struct Node *head, int value)
{
    struct Node* newnode = malloc(sizeof(struct Node));
    if (newnode == NULL) {
        return head; 
    }
    newnode->value = value; 
    newnode->next = head;
    return newnode;
}

// TODO: a function that prints the list in order (e.g. "3 -> 2 -> 1").

void printList(struct Node* node) {
    while (node !=NULL) {
        if (node->next !=NULL){
        printf("%d -> ", node->value);
    }
    else 
    {
        printf("%d ", node->value);
    }
        node = node->next;
    }
}

// TODO: void free_list(node *head)  — free every node, leak-free.
//free list takes the head and save next node before remove the head then, that moves to the next node and repeats that until the list is empty
void free_list(struct Node *head)
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        struct Node *next = temp->next;
        free(temp);
        temp = next;
    }
}

int main(void)
{
    // TODO: starting from an empty list, use prepend to build 3 -> 2 -> 1,
    struct Node *head = NULL;
    head = prepend(head, 1);
    head = prepend(head, 2);
    head = prepend(head, 3);

    printList(head);
    // print it, then free the whole list.
    free_list(head);
    return 0;
}
