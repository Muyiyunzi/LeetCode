# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def sumtree(node):
            nonlocal cnt
            if node is None:
                return [0, 0]
            leftres = sumtree(node.left)
            rightres = sumtree(node.right)
            res = [node.val + leftres[0] + rightres[0], 1 + leftres[1] + rightres[1]]
            if (res[0] // res[1]) == node.val:
                cnt += 1
            return res
        sumtree(root)
        return cnt
            