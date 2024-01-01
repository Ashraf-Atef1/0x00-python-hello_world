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
	unsigned int i = 0;
	unsigned int j = i - 1;

	while (list)
	{
		if (list->next && list <= list->next)
			return (1);
		list = list->next;
	}
	while (i < j)
	{
		i++;
	}
	return (0);
}
