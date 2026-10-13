"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        curr = head
        while curr:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        #newHead = Node()
        newHead = head.next
        #newcurr = Node()
        newcurr = newHead
        while curr:
            curr.next = newcurr.next
            curr = curr.next
            if curr:
                newcurr.next = curr.next
                newcurr = newcurr.next
        return newHead        

