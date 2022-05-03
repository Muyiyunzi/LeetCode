# lambda一句话
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=lambda x: (x.split(' ')[1][0].isnumeric(), (x.split(' ')[1:], x.split(' ')[0]) if x.split(' ')[1][0].isalpha() else None))

#按照官解，写了一版自定义函数
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str):
            a, b = log.split(' ', 1)
            if b[0].isalpha():
                return (0, b, a)
            return (1, )
        return sorted(logs, key=trans)