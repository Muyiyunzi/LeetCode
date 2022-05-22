class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # options = 1 << 20 - 1
        # def dfs(status, res):
        #     for i in range(maxChoosableInteger):
        #         if (status >> i) & 1:
        #             if res + i + 1 >= desiredTotal or not dfs(status - (1 << i), res + i + 1):
        #                 return True
        #     return False
        
        # return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(options, 0)
        @cache
        def dfs(status, res):
            for i in range(maxChoosableInteger):
                if (status >> i) & 1 == 1:
                    if res + i + 1 >= desiredTotal or not dfs(status - (1 << i), res + i + 1):
                        return True
            return False
        
        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs((1 << 20) - 1, 0)