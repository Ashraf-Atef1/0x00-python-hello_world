#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	if (head && *head)
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
		newNode->next = NULL;
		*head = newNode;
		return (newNode);
	}

	return (*head);
}
