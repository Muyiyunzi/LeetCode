# 注意，维护nums是没有意义的，因为有可能某些拿数的情况下是不行的
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        target = sum(matchsticks)
        if target % 4 != 0:
            return False
        else:
            target //= 4
        
        n = len(matchsticks)
        
        @cache
        def dfs(status, tarnow):
            if status == (1 << n) - 1 and tarnow == target:
                return True

            for i in range(n):
                if (1 << i) & status == 0:
                    if matchsticks[i] > tarnow:
                        continue
                    if matchsticks[i] == tarnow:
                        return dfs(status | (1 << i), target)
                    else:
                        if dfs(status | (1 << i), tarnow - matchsticks[i]):
                            return True
            return False
        
        return dfs(0, target)

# 根据题解可以将小于等于合并
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        target = sum(matchsticks)
        if target % 4 != 0:
            return False
        else:
            target //= 4
        
        n = len(matchsticks)
        
        nums = 0
        @cache
        def dfs(status, tarnow):
            nonlocal nums
            if tarnow == 0:
                tarnow = target
                if status == (1 << n) - 1:
                    return True

            for i in range(n):
                if (1 << i) & status == 0 and matchsticks[i] <= tarnow:
                    if dfs(status | (1 << i), tarnow - matchsticks[i]):
                        return True
            return False
        
        return dfs(0, target)


# 答案不是记忆化搜索，时间上差了很多
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLen = sum(matchsticks)
        if totalLen % 4:
            return False
        tLen = totalLen // 4

        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= tLen:
                    dp[s] = (dp[s1] + v) % tLen
                    break
        return dp[-1] == 0