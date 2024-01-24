#!/usr/bin/python3
"""A class called  Node used to struct linked list node & class SinglyLinkedList"""


class Node:
    """Class for singly linked list node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter for data attr"""
        return(self.__data)
    @property
    def next_node(self):
        """ getter for next_node attribute"""
        return(self.__next_node)

    @data.setter
    def data(self, value):
        """setter for data attr"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setter for next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class for  singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts new node"""
        newNode = Node(value)
        if self.__head is None:
            self.__head = newNode
        else:
            temp = self.__head
            if temp.data > newNode.data:
                newNode.next_node = temp
                self.__head = newNode
                return
            while temp.next_node is not None:
                temp2 = temp.next_node
                if temp2.data < newNode.data:
                    temp = temp2
                else:
                    newNode.next_node = temp.next_node
                    temp.next_node = newNode
                    return
            temp.next_node = newNode

    def stringrep(self):
        stringRep = ""
        temp = self.__head
        while temp is not None:
            dataVal = temp.data
            stringRep = stringRep + str(dataVal)
            temp = temp.next_node
            if temp:
                stringRep = stringRep + "\n"
        return stringRep

    def __repr__(self):
        return(self.stringrep())
