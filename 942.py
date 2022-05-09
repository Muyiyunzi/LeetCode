# 跟答案想法不太一样，但是搞出来个100%时间
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        ans = []
        low, high = 0, n
        if s[0] == 'D':
            ans.append(high)
            high -= 1
        else:
            ans.append(low)
            low += 1
        for i, val in enumerate(s):
            if i+1 < n:
                if s[i+1] != val:
                    if val == 'I':
                        ans.append(high)
                        high -= 1
                    else:
                        ans.append(low)
                        low += 1
                else :
                    if val == 'I':
                        ans.append(low)
                        low += 1
                    else:
                        ans.append(high)
                        high -= 1
            else:
                ans.append(high)
        return ans

# 按答案贪心来写一下
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        high = n = len(s)
        low = 0
        ans = [0] * (n+1)
        for i, val in enumerate(s):
            if val == 'I':
                ans[i] = low
                low += 1
            else:
                ans[i] = high
                high -= 1
        ans[n] = high
        return ans