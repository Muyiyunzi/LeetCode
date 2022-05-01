# 被ind=0坑了
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashtable = defaultdict(int)
        ans = 1e6
        for ind, val in enumerate(cards):
            if hashtable[val]:
                ans = min(ans, ind - hashtable[val] + 2)
            hashtable[val] = ind + 1
        return ans if ans != 1e6 else -1