class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            d = dict()
            for ind, ch in enumerate(word):
                keyflag = ch in d.keys()
                valueflag = pattern[ind] in d.values()
                if not keyflag and not valueflag:
                    d[ch] = pattern[ind]
                elif keyflag and valueflag and d[ch] == pattern[ind]:
                    continue
                else:
                    break
            else:
                ans.append(word)
        return ans
