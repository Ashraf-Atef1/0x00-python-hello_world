#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cNode = *head;
	while (cNode)
	{
		if (!cNode->next)
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

	return (*head);
}
