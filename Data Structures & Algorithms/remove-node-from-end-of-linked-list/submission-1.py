# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy=ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy
        count = 0
        while count <= n:
            p2 = p2.next
            count += 1
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next    
        p1.next = p1.next.next
        return dummy.next