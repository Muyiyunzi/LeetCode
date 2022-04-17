class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt = Counter()
        word = ''
        n = len(paragraph)
        for i in range(n+1): # 这题坑在单词结尾怎么办
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in banned:
                    cnt[word] += 1
                word = ''
        maxtime = 0
        ans = ''
        for key in cnt.keys():
            if cnt[key] > maxtime:
                ans = key
                maxtime = cnt[key]
        return ans