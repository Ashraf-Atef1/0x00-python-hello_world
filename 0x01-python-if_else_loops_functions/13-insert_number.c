#include "lists.h"
/**
 * insert_node - Insert a new node according to number postion
 * @head: pointer to a linked list
 * @number: the number to coparewith and add to the new node
 * Return: return a pointer to the new node if added or NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	if (head && *head && (*head)->n < number)
	{
		listint_t *cNode = *head;

		while (cNode)
		{
			if (!cNode->next || cNode->next->n > number)
			{
				listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));
				if (!newNode)
				{
					free(newNode);
					return (NULL);
				}
				newNode->n = number;
				newNode->next = cNode->next;
				cNode->next = newNode;
				return (newNode);
			}
			cNode = cNode->next;
		}
	}
	else
	{
		listint_t *newNode = (listint_t *)malloc(sizeof(listint_t));

		if (!newNode)
		{
			free(newNode);
			return (NULL);
		}
		newNode->n = number;
		if (head)
			newNode->next = *head;
		else
			newNode->next = NULL;
		*head = newNode;
		return (newNode);
	}
	return (*head);
}
