# lambda一句话
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda x: (x.split(' ')[1][0].isnumeric(), (x.split(' ')[1:], x.split(' ')[0]) if x.split(' ')[1][0].isalpha() else None))