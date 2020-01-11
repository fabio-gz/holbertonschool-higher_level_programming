#!/usr/bin/python3
class Node:
    """class to create a node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """check correctness"""
        if not isinstance(self.__data, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrieve next node data"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """check for correctness"""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class to inser node in linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        list1 = []
        tmp = self.__head
        while tmp:
            list1.append(str(tmp.data))
            tmp = tmp.next_node
        list1.sort(key=int)
        return ('\n'.join(list1))

    def sorted_insert(self, value):
        if self.__head is None:
            n_node = Node(value)
            n_node.data = value
            n_node.next_node = self.__head
            self.__head = n_node
        else:
            n_node = Node(value, None)
            n_node.data = value
            n_node.next_node = self.__head
            self.__head = n_node
