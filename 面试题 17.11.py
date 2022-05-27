class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        d = defaultdict(list)
        for i, val in enumerate(words):
            d[val].append(i)
        l1, l2 = d[word1], d[word2]
        ans = 100000
        temp = 100000
        for i in l1:
            for j in l2:
                ans = min(ans, abs(j-i))
        return ans