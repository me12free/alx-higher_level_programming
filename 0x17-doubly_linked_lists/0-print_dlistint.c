#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: pointer to list
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h);
{
	const dlistint *node = h;
	size_t con = 0;

	while (node)
	{
		printf("%i\n", node->next);
		con++;
		node = node->next;
	}
	return (con);
}
