
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x:(-len(x), x), reverse=True)
        ans = ""
        candidate = {""}
        for word in words:
            if word[:-1] in candidate:
                ans = word
                candidate.add(word)
        return ans