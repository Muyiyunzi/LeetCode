# 朴素sort，40ms，15.2M
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def trans(s):
            return [order.index(i) for i in s]
        return sorted(words, key=trans) == words

# pairwise，36ms，15.1M
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {val : i for i, val in enumerate(order)}
        mat = []
        for word in words:
            mat.append([index[c] for c in word])
        for i, j in pairwise(mat):
            if i > j:
                return False
        return True

# lambda+sort
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda x: [order.index(i) for i in x]) == words