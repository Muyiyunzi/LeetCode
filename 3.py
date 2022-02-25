# 第一版，双指针滑窗
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        slow, fast = 0, 0
        count = 1
        s = list(s)
        hashMap = defaultdict(bool)
        while(slow < len(s) - 1):
            while(fast < len(s) and not hashMap[s[fast]]):
                hashMap[s[fast]] = True
                fast += 1
            count_now = fast - slow
            count = max(count, count_now)
            if fast == len(s):
                break
            while(s[slow] != s[fast]):
                hashMap[s[slow]] = False
                slow += 1
            slow += 1
            fast += 1
        return count

# 第二版，set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = fast = count = 0
        occ = set()
        while(slow < len(s)):
            while(fast < len(s) and s[fast] not in occ):
                occ.add(s[fast])
                fast += 1
            count = max(count, fast - slow)
            if fast == len(s):
                break
            while(s[slow] != s[fast]):
                occ.remove(s[slow])
                slow += 1
            slow += 1
            fast += 1
        return count