class Solution:
    def get_steps(self, now, n) -> int:
        # now底下有多少个数，以最大最小来看，并观察是否越了n的界
        first = last = now
        steps = 0
        while(first <= n): # 注意这里的判定必须是first，因为只要first比n小就应该去count
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        # 不能想着一口吃个胖子，已经有了字典树之后就不要太贪了
        now = 1
        k -= 1 # 从1开始，所以k要-=1
        while k:
            steps = self.get_steps(now, n)
            if steps <= k: # 此数直接跳过
                k -= steps
                now += 1
            else:
                k -= 1
                now *= 10
        return now
            
