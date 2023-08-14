#include "lists.h"


/**
 * palindrome - check if is palindrome with recursion
 * @l: l
 * @r: r
 * Return: 1 or 0
 */

int palindrome(listint_t **l, listint_t *r)
{
	int response;

	if (r != NULL)
	{
		response = palindrome(l, r->next);
		if (response != 0)
		{
			response = (r->n == (*l)->n);
			*l = (*l)->next;
			return (response);
		}
		return (0);

	}
	return (1);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of linked list
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
