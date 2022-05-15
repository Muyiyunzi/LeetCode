class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        nstr = str(num)
        n = len(nstr)
        ans = 0
        for i in range(n - k + 1):
            chushu = int(nstr[i:k+i])
            if chushu and num % chushu == 0:
                ans += 1
        return ans