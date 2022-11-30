class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        https://leetcode.com/problems/reverse-linked-list/

        Given the head of a singly linked list, reverse the list, and return the
        reversed list (the head of it).

        Example 1:
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Example 2:
        Input: head = [1,2]
        Output: [2,1]

        Example 3:
        Input: head = []
        Output: []

        Constraints:
        The number of nodes in the list is the range [0, 5000].
        -5000 <= Node.val <= 5000

        Algorithm:

        We know that a singly linked list is a set of Node class instances that each has 2
        attributes: a "value" and a "next" variable containing the next node in the list. The
        list is given by passing the first node. The last node's "next" value will be null (None).

        So, given example 1 where the input is the head of a linked list containing values [1,2,
        3,4,5], the input linked list will look like this: (1)->(2)->(3)->(4)->(5)->None

        The first node will have value = 1 and a pointer "->" to Node(2).

        We want to iterate through each Node(x), x : [1:5] and change its "next" value from
        Node(x+1) to Node(x-1). However, for the first node, there is no Node before itself no
        Node(0), so we have to use None, a null value just like for Node(5).

        So, first we initialize a variable called "prev_node" set to None.
        Then we iterate through through each node, and
            a) create a temp copy of the current node's next node
            b) change the node's "next" pointer to point to prev_node.
            c) update prev_node to the current node to set things up for the next iteration.
            d) update current_node to the next_node to set things up for the next iteration.
        """
        prev_node = None
        current_node = head
        while current_node:
            # save a temporary copy of the next node
            next_node = current_node.next
            # change the next node to the previous node
            current_node.next = prev_node
            # set things up for the next iteration,
            prev_node = current_node
            current_node = next_node
        return prev_node



"""Linked List implementation in Python"""


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_data):
        new_node = Node(new_data)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert(self, new_data, position):
        new_node = Node(new_data)
        count = 1
        current = self.head
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        while current:
            if count + 1 == position:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                count += 1
                current = current.next
            # break
        pass

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            prev = current
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


# To create a linked list of two values 1 and 2, first define them as individual nodes n1 and n2
n1 = Node(1)
n2 = Node(2)
# Then link them together by defining n1's "next" attribute to be n2
n1.next = n2
# Then instantiate a LinkedList class instance with its head set to n1
mylinkedlist = LinkedList(n1)
# To test the print method of this linked list, call its print_list method
mylinkedlist.print_list()

