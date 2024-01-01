#include "./lists.h"
#include <stdio.h>

/**
 * check_cycle - function that check if the linked list has a cycle
 * @list: pointer to a linked list to check
 * Return: 0 if on cycle or 1 otherwise
 * Ashraf Atef
 */
int check_cycle(listint_t *list)
{
	while (list)
	{
		if (list->next && list <= list->next)
			return (1);
		list = list->next;
	}
	return (0);
}
