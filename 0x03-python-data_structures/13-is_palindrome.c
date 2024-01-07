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
	int list[1000];
	int size = 0, i = 0;
	listint_t *c_list = *head;

	while (c_list)
	{
		list[size] = c_list->n;
		c_list = c_list->next;
		size++;
	}
	while (i < (size - 1) / 2)
	{
		if (list[i] != list[size - 1 - i])
			return (0);
		i++;
	}
	return (1);
}
