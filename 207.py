# 拓扑排序模板题
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = defaultdict(list)
        in_deg = {}
        for i, j in prerequisites:
            in_deg.setdefault(i, 0)
            in_deg.setdefault(j, 0)
            G[j].append(i)
            in_deg[i] += 1

        q = [course for course, deg in in_deg.items() if deg == 0]
        for u in q:
            for v in G[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        return True if len(q) == len(in_deg) else False



        