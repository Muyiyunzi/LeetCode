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

# 按照答案的方式，获取length，用for改写了一下，时间上慢不少。
# 似乎这种边pop边append的方式要慢不少。pop时的长度似乎很影响时间？
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            layer = []
            lq = len(q)
            for i in range(lq):
                node = q.popleft()
                layer.append(node.val) # 注意这里加val，就避免了最后-1的尴尬
                for i in node.children:
                    q.append(i)
            ans.append(layer)
        return ans