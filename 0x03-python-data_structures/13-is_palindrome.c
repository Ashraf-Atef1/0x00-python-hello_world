#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome_helper - fuction checks linked list is a palindrome or not
 * @head: linked list to check
 * @c_list: current node
 * @is_palindrome: the value to return
 * Return: return 1 if palindrome and 0 if not
 */
int is_palindrome_helper(listint_t **head, listint_t *c_list, int is_palindrome)
{
	if (!c_list)
		return (is_palindrome);
	is_palindrome_helper(head, c_list->next, is_palindrome);
	if ((*head)->n != c_list->n)
		is_palindrome = 0;
	*head = (*head)->next;
	return (is_palindrome);
}
/**
 * is_palindrome - fuction checks linked list is a palindrome or not
 * @head: linked list to check
 * Return: return 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	return (is_palindrome_helper(head, *head, 1));
}
