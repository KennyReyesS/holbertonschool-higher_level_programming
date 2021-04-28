#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: pointer to beggining.
 *Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL)
	{
		return (0);
	}
	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		if (fast == slow)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
