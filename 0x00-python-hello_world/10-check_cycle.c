#include "lists.h"
/**
 *check_cycle - check if the is cycle in the list
 *@list: list Return: 1
 *Return: for cycle, 0 for no cylce
 */
int check_cycle(listint_t *list)
{
	listint_t *node, *node1;

	if (list == NULL)
		return (0);

	node = list;
	node1 = list;

	node1 = node1->next;
	while (node1 != NULL && node1->next != NULL)
	{
		if (node == node1)
			return (1);
		node1 = node->next->next;
		node = node->next;
	}
	return (0);
}
