"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while(q):
            node = q.popleft()
            ans.append(node.val)
            q.extendleft(node.children[::-1])
        return ans