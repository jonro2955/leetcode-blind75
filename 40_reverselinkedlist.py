# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
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
        :type head: ListNode
        :rtype: ListNode

        Algorithm:
        Initialize a variable called "prev_node" set to None.
        Go through each node, and a) Change the node's "next" pointer to point to the prev_node.
        b) set prev_node to the current node
        """
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node



"""
Linked List implementation in Python
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

        def append(self, new_node):
            current = self.head
            if current:
                while current.next:
                    current = current.next
                current.next = new_node
            else:
                self.head = new_node

        def delete(self, value):
            current = self.head
            if current.value == value:
                self.head = current.next
            else:
                while current:
                    if current.value == value:
                        break
                    prev = current
                    current = current.next
                if current is None:
                    return
                prev.next = current.next
                current = None

        def insert(self, new_element, position):
            count = 1
            current = self.head
            if position == 1:
                new_element.next = self.head
                self.head = new_element
            while current:
                if count + 1 == position:
                    new_element.next = current.next
                    current.next = new_element
                    return
                else:
                    count += 1
                    current = current.next
                # break
            pass

        def print_list(self):
            current = self.head
            while current:
                print(current.value)
                current = current.next
