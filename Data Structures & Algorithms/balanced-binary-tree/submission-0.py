# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def differ(node):
            nonlocal balance
            if node is None:
                return 0
            left = differ(node.left)
            right = differ(node.right)
            if abs(left-right) > 1:
                balance = False 
            return 1 + max(left,right)
        differ(root)    
        return balance       
            