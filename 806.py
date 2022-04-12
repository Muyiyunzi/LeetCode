class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        leftover = 0
        for i in s:
            temp = widths[ord(i) - ord('a')]
            leftover += temp
            if leftover > 100:
                # leftover -= temp
                lines += 1
                leftover = temp
        return [lines, leftover]