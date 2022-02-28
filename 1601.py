# 最大流最小割，44ms
class Edge:
    def __init__(self, frm, to, cap, cost, flow):
        self.frm = frm
        self.to = to
        self.cap = cap
        self.cost = cost
        self.flow = flow

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        s = n # 虚拟源
        t = n + 1 # 虚拟宿
        N = n + 2 # 总节点数
        deg = [0] * n # 度
        edges = [] # 存储边的class
        G = [[] for _ in range(N)] # 邻接表,G[x]存储与x上边的编号

        def addEdge(frm, to, cap, cost):
            m = len(edges)
            edges.append(Edge(frm, to, cap, cost, 0))
            G[frm].append(m) # 编为m号边
            edges.append(Edge(to, frm, 0, -cost, 0))
            G[to].append(m+1) # 编为m+1号边

        for req in requests: # 更新所有请求形成的边和度
            deg[req[0]] -= 1
            deg[req[1]] += 1
            addEdge(req[0], req[1], 1, 1)

        for ind, d in enumerate(deg):
            if d > 0: # 有没出完的度 →t
                addEdge(ind, t, d, 0)
            elif d < 0: # 需要入一些度 s→
                addEdge(s, ind, -d, 0)
        
        minCost = 0
        flow = 0
        p = [0] * N # 路径，存储最近一次搜索某个点的上一条边
        vis = [False] * N
        
        while True:
            a = [0] * N #
            dis = [float('inf')] * N 
            a[s] = float('inf')
            dis[s] = 0

            queue = [s]
            while queue:
                x = queue.pop()
                vis[x] = False
                for i in G[x]:
                    e = edges[i]
                    if e.cap > e.flow and dis[e.to] > dis[e.frm] + e.cost:
                        dis[e.to] = dis[e.frm] + e.cost
                        a[e.to] = min(e.cap - e.flow, a[x]) # 流之前要比一下，源头够不够流这些capacity
                        p[e.to] = i
                        if not vis[e.to]:
                            vis[e.to] = True
                            queue.append(e.to)
            
            if a[t] == 0: break # 宿的流量为0，所有增广路径都被切除
            u = t
            while u != s:
                edges[p[u]].flow += a[t]
                edges[p[u]^1].flow -= a[t]
                minCost += a[t] * edges[p[u]].cost
                u = edges[p[u]].frm
            flow += a[t]
        
        return len(requests) - minCost

# 暴力方法，枚举组合，1204ms
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        base = 0
        for u, v in requests:
            if u == v: base += 1
        for res in range(len(requests), -1, -1):
            for choices in itertools.combinations(requests, res):
                c = [0] * n
                for u, v in choices:
                    c[u], c[v] = c[u] + 1, c[v] - 1
                if all(t == 0 for t in c): return res + base
        return 0

# 去掉入度或出度为0的结点包含的所有边后再枚举，48ms，时间就离谱啊
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        base, reqs, indeg, outdeg = 0, [], [0] * n, [0] * n
        for u, v in requests:
            if u == v: base += 1
            else:
                outdeg[u], indeg[v] = outdeg[u] + 1, indeg[v] + 1
                reqs.append((u, v))
        requests = []
        for u, v in reqs:
            if 0 not in (outdeg[v], indeg[u]):
                requests.append((u, v))
        for res in range(len(requests), -1, -1):
            for choices in itertools.combinations(requests, res):
                c = [0] * n
                for u, v in choices:
                    c[u], c[v] = c[u] + 1, c[v] - 1
                if all(t == 0 for t in c): return res + base
        return 0