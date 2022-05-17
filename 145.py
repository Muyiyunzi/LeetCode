# 迭代，40ms，15.1M
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = []
        cur, prev = root, None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.right and prev != cur.right: # 如果有右节点，并且还没访问过
                stack.append(cur)
                cur = cur.right
            else:
                ans.append(cur.val)
                prev = cur
                cur = None
        return ans

# 递归，40ms，14.8M
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            ans.append(root.val)
        
        postOrder(root)
        return ans