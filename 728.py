# 注意打表应该是最快的办法（先打，手动把表输进去，避免On）
# 这样边查边输出是O(n log right)
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def judge(i: int) -> bool:
            s = str(i)
            for j in s:
                if j == '0' or i % int(j):
                    return False
            return True
        ans = []
        for i in range(left, right + 1):
            if judge(i):
                ans.append(i)
        return ans