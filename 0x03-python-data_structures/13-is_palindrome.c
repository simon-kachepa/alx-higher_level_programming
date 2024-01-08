#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev_n = NULL;
	listint_t *next_n = NULL;
	listint_t *current = *head;

	if (!(*head))
		return (1);

	while (current)
	{
		next_n = current->next;
		current->next = prev_n;
		prev_n = current;
		current = next_n;
	}
	current = prev_n;

	while (*head && (*head)->next && current && current->next)
	{
		if ((*head)->n != current->n)
			return (0);
		*head = (*head)->next;
		current = current->next;
	}
	return (1);
}
