# 简直了，就是困难题好吧
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        G = [[] for _ in range(n)]
        for (i, j) in edges:
            G[i].append(j)
            G[j].append(i)
        
        parents = [0] * n
        def bfs(node):
            vis = [False] * n
            vis[node] = True
            q = deque()
            q.append(node)
            while q:
                temp = q.popleft() # 原来死在这里。。
                for i in G[temp]:
                    if not vis[i]:
                        vis[i] = True
                        q.append(i)
                        parents[i] = temp
            return temp # 返回最远的点
        
        nodemax = bfs(0)
        node_other = bfs(nodemax)

        path = []
        parents[nodemax] = -1
        while node_other != -1: # 这里一定要把最后一个结点也加进去，否则会不通过
            path.append(node_other)
            node_other = parents[node_other]
        p = len(path)
        return [path[p//2]] if p % 2 else [path[p//2-1], path[p//2]]
