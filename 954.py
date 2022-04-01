# 忘了Counter这厮了。其实反正都要排序，不如Onlogn起步想想怎么搞，有时间再来写一下
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        values = set()
        times = dict()
        for i in arr:
            if i not in values:
                values.add(i)
                times[i] = 1
            else:
                times[i] += 1
        values = list(values)
        values.sort(key=lambda x:(abs(x)))
        for val in values:
            if times[val] == 0:
                continue
            else:
                if 2*val not in values or times[2*val] < times[val]:
                    return False
                times[2*val] -= times[val]
        return True