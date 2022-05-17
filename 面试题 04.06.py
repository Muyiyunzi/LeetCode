# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归写法，注意两点：1，pre这种东西应该是一个全局变量，因为要给回溯者修改标记；2.在访问的时候才修改pre，这样才符合逻辑

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = pre = None
        def inOrder(root):
            nonlocal ans, pre
            if not root:
                return
            inOrder(root.left)
            if pre == p:
                ans = root
            pre = root
            inOrder(root.right)
        inOrder(root)
        return ans