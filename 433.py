# 第一版 DFS
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        vis = defaultdict(bool)
        
        def compare(s1, s2):
            cnt = 0
            for i in range(8):
                cnt += (s1[i] != s2[i])
            return cnt

        def dfs(snow, times, vis):
            if snow == end:
                return times
            ans = 1000000
            for s in bank:
                if vis[s] == True:
                    continue
                if compare(snow, s) == 1:
                    vis[s] = True
                    res = dfs(s, times+1, vis)
                    vis[s] = False
                    if res != -1:
                        ans = min(ans, res)
            return ans if ans != 1000000 else -1
        
        return dfs(start, 0, vis)

# 第二版，按答案改一波BFS
# 不会先6后4，BFS的层数就是答案，这时候就很好了
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def diffone(s1, s2):
            return sum(s1[i] != s2[i] for i in range(8)) == 1
        
        n = len(bank)
        adj = [[] for _ in range(n)]

        endind = -1
        for i in range(n):
            if bank[i] == end:
                endind = i
                continue
            for j in range(i+1, n):
                if diffone(bank[i], bank[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        
        if endind == -1:
            return -1
        q = [i for i, val in enumerate(bank) if diffone(start, val)]
        ans = 1
        vis = set(q)
        while q:
            temp = []
            for i in q:
                if i == endind:
                    return ans
                for j in adj[i]:
                    if j not in vis:
                        vis.add(j)
                        temp.append(j)
            q = temp
            ans += 1
        return -1
