# BFS空间换时间击败99.7%
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root 
        q = deque()
        q.append(root)
        ans = [[root.val]]
        while q:
            layer = []
            nodes = []
            while q:
                node = q.popleft()
                for i in node.children:
                    nodes.append(i)
                    layer.append(i.val)
            ans.append(layer)
            q.extend(nodes)
        return ans[:-1]