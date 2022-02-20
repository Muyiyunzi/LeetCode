# 正序
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        flag = False
        while(i < len(bits)):
            if bits[i] == 1:
                i += 2
                flag = False
            else: # bits[i] == 0
                i += 1
                flag = True
        return flag

# 逆序
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = len(bits) - 2
        while(i >= 0):
            if bits[i] != 0:
                i -= 1
            else: break
        return True if (len(bits) - i) % 2 == 0 else False

# 正序简洁
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while(i < n - 1):
            i += 1 + bits[i]
        return i == n - 1

# 逆序简洁
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = len(bits) - 2
        while(i >= 0 and bits[i]):
            i -= 1
        return (len(bits) - i) % 2 == 0
