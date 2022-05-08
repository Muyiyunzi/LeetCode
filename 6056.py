class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt, ans = 0, -1
        temp = num[0]
        for i in num:
            if i == temp:
                cnt += 1
            else:
                cnt = 1
                temp = i
            if cnt == 3:
                ans = max(ans, int(i))
        return str(ans) * 3 if ans != -1 else ""