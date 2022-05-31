class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G = defaultdict(list)
        in_deg = {c: 0 for c in words[0]}
        for i, j in pairwise(words):
            for c in j:
                in_deg.setdefault(c, 0)
            for m, n in zip(i, j):
                if m != n:
                    G[m].append(n)
                    in_deg[n] += 1
                    break
            else:
                if len(i) > len(j):
                    return ""
        
        q = [c for c, d in in_deg.items() if d == 0]
        for u in q:
            for v in G[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        return "".join(q) if len(q) == len(in_deg) else ""