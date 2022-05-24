# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        ans = root.val
        def preOrder(root):
            if root is None:
                return True

            if root.val != ans:
                return False
            return preOrder(root.left) and preOrder(root.right)
        return preOrder(root)