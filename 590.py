# 跟前天的589很像。deque永远的神
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            node = q.pop()
            q.extend(node.children)
            ans.append(node.val)
        return ans[::-1]