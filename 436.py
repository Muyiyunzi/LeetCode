# 双指针。2*O(nlogn)+O(n).OrderedDict真没必要感觉。。
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hashTable = dict()
        for i, (j, k) in enumerate(intervals):
            hashTable[j] = i
        interight = sorted(intervals, key=lambda x: x[1])
        lefts = list(hashTable.keys())
        lefts.sort()
        p, n = 0, len(lefts)
        ans = [-1] * n
        for i, j in interight:
            while p < n and j > lefts[p]:
                p += 1
            if p == n:
                break
            ans[hashTable[i]] = hashTable[lefts[p]]
        return ans
            
# 再写个二分
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, val in enumerate(intervals):
            val.append(i) # 这样比哈希表操作好的一点在于可以应对重复情况
        intervals.sort()
        n = len(intervals)
        ans = [-1] * n
        for left, right, ind in intervals:
            i = bisect_left(intervals, [right])
            # 别忘了判断越界的问题
            if i < n:
                ans[ind] = intervals[i][2]
        return ans