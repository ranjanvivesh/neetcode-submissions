# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find Mid 
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        # here p1 will be the mid point 
        # reversing after the mid
        premid = p1
        precur = p1.next
        while precur and precur.next :
            cur = precur.next
            precur.next = cur.next
            cur.next = premid.next
            premid.next = cur
        # arranging
        p1 = head
        p2 = premid.next
        while p1 and p2:
            premid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = premid.next
