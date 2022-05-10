# DP
class Solution:
    def numSquares(self, n: int) -> int:
        ans = [0] + [10000] * n
        fsquare = [i*i for i in range(1, int(sqrt(n))+1)]

        for i in range(n+1):
            for j in fsquare:
                if j > i: # 这里加上能提2000ms左右的速度
                    break
                ans[i] = min(ans[i], ans[i-j] + 1)
            
        return ans[n]

# 数学
class Solution:
    def numSquares(self, n: int) -> int:
        
        # 经证明，不断除以4的过程可以优先进行，不影响后续
        while(not n % 4):
            n //= 4
        if n % 8 == 7:
            return 4
        
        fsquare = set(i*i for i in range(1, int(sqrt(n))+1))

        if n in fsquare:
            return 1
        
        for i in fsquare:
            if (n - i) in fsquare:
                return 2
        
        return 3
