# 迭代，40ms，14.9M
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                ans.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return ans

# 递归，56ms，14.8M
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preOrder(root):
            if not root:
                return
            ans.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return ans


