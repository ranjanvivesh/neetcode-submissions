# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preorder(node):
            if node is None:
                return "#"
            return(
                ',' + str(node.val) + preorder(node.left) + preorder(node.right)
            )    
        fulltree = preorder(root)
        subtree = preorder(subRoot)
        if subtree in fulltree:
            return True
        else:
            return False    