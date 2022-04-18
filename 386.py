# 用lambda偷懒2333
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = list(range(1, n+1))
        nums.sort(key=lambda x:(str(x)))
        return nums

# DFS
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        q = deque([1,2,3,4,5,6,7,8,9])
        ans = []
        while q:
            now = q.popleft()
            if now > n:
                continue
            else:
                ans.append(now)
                now = now * 10
                q.extendleft(list(range(now+9, now-1, -1)))
        return ans