class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = left = 0
        ans = ""
        for i, val in enumerate(s):
            if stack == 0:
                left = i
            if val == '(':
                stack += 1
            else:
                stack -= 1
                if stack == 0:
                    ans += s[left+1:i]
        return ans
