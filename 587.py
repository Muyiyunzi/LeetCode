class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p, q, r): 
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])
        
        n = len(trees)
        p = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[p][0]:
                p = i
        
        vis = [False] * n
        ans = []
        begin = p
        while True:
            q = (p + 1) % n
            for i in range(n):
                # if vis[i]: # 这里可不能跳，跳了就找不到最远的边界了
                #     continue
                if cross(trees[p], trees[q], trees[i]) < 0:
                    q = i
            for i in range(n):
                if not vis[i] and p != i and q != i and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True
            if not vis[q]:
                vis[q] = True
                ans.append(trees[q])
            p = q
            if p == begin:
                break
        return ans
        