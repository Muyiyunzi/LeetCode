class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        l, r = 0, len(ans) - 1
        while(l < r):
            while(l < r and not ans[l].isalpha()):
                l += 1
            while(l < r and not ans[r].isalpha()):
                r -= 1
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        
        return ''.join(ans)