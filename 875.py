# 典型二分模板题
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        MAX = 10 ** 9
        MIN = 1
        
        # cal_time
        def bisect_hour(left, right):
            if left + 1 == right:
                return right
            mid = (left + right) >> 1
            total_time = sum(ceil(i / mid) for i in piles)
            if total_time <= h: # ok
                return bisect_hour(left, mid)
            else:
                return bisect_hour(mid, right)
        
        return bisect_hour(0, 10**9)

# 可是我还是败给了答案

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(max(piles)), -h, lo=1, key=lambda x: -sum(ceil(pile / x) for pile in piles)