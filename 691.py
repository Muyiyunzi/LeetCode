class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(target)
        # 问题，这个状压压在何处了呢 # cache就是为了有些mask的时候能够得到答案吧
        @cache
        def dp(mask):
            if mask == 0: # 递归不要忘了边界条件
                return 0
            res = m + 1 #最多m个stickers就够了，m+1表示没找到
            for sticker in stickers:
                left = mask # 遍历每个词的时候，都应该生成一个left，不能放在循环外边 # 一个词是可以用多遍的
                cnt = Counter(sticker)
                for i, ch in enumerate(target):
                    if (mask >> i) & 1 and cnt[ch]:
                        cnt[ch] -= 1
                        left = left ^ (1 << i)
                if left < mask:
                    res = min(res, dp(left) + 1) # 加上使用了自己这1个词
            return res

        res = dp((1 << m) - 1)
        return res if res <= m else -1