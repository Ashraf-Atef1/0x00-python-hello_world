#!/usr/bin/python3
"""singly linked list class."""


class Node:
    """Singly linked-list node class"""

    def __init__(self, data, next_node=None):
        """initalization function"""

        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """get data"""
        return self.__data

    @data.setter
    def data(self, data):
        """set data"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """set next_node"""
        if not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """SinglyLinkedList head class"""

    def __init__(self):
        """initalization function"""
        self.__head = None

    def sorted_insert(self, value):
        """insert new node in a sorted order"""
        new_node = Node(value)
        head = self.__head
        if head:
            c_node = head
            while c_node:
                if c_node.data >= value:
                    new_node.next_node = c_node
                    self.__head = new_node
                    break
                elif c_node.next_node and c_node.next_node.data >= value:
                    new_node.next_node = c_node.next_node
                    c_node.next_node = new_node
                    break
                elif not c_node.next_node:
                    c_node.next_node = new_node
                    break
                c_node = c_node.next_node
        else:
            self.__head = new_node

    def __str__(self):
        """print all linked list elements"""
        head = self.__head
        string = ""
        while head:
            string += '{:d}'.format(head.data)
            head = head.next_node
            if head:
                string += "\n"
        return string
