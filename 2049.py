# 建图（有点像邻接表）+DFS，O(n)
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for ind, parent in enumerate(parents):
            if parent != -1:
                children[parent].append(ind)
        maxScore, cnt = 0, 0
        def dfs(node) -> int: # 返回当前结点的子树个数
            size = n - 1
            score = 1
            for child in children[node]:
                size_child = dfs(child)
                size -= size_child
                score *= size_child
            if size:
                score *= size
            nonlocal maxScore, cnt
            if score > maxScore:
                maxScore = score
                cnt = 1
            elif score == maxScore:
                cnt += 1
            return n - size # 返回时应该包含自己，才能满足之前递归调用的目的
        dfs(0)
        return cnt

