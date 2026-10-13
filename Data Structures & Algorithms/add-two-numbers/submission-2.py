# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 or curr2:
            x = curr1.val if curr1 else 0
            y = curr2.val if curr2 else 0
            add = x + y + carry
            if add >9:
                carry = 1
            else:
                carry = 0
            node = ListNode(add%10)
            curr.next = node
            curr = curr.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        if carry:
            curr.next = ListNode(carry)    
        return dummy.next
