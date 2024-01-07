#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - fuction checks linked list is a palindrome or not
 * @head: linked list to check
 * Return: return 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	int *list = malloc(sizeof(int));
	int size = 0, i = 0;
	listint_t *c_list = *head;

	while (c_list)
	{
		list = realloc(list, sizeof(int) * size + 1);
		list[size] = c_list->n;
		c_list = c_list->next;
		size++;
	}
	while (i < (size - 1) / 2)
	{
		if (list[i] != list[size - 1 - i])
		{
			free(list);
			return (0);
		}
		i++;
	}
	free(list);
	return (1);
}
