# 暴力双指针 O(n2), 288ms
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = 0
        for i in range(n-1):
            Max = Min = nums[i]
            for j in range(i+1, n):
                Max = max(Max, nums[j])
                Min = min(Min, nums[j])
                Sum += (Max - Min)
        return Sum

# 单调栈 O(n), 68ms
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        Sum_min, Sum_max = 0, 0 # 记录当前 总的最小值和 与 总的最大值和
        minleft, minright = [0]*n, [0]*n
        maxleft, maxright = [0]*n, [0]*n
        minStack, maxStack = [], [] # minStack：递增栈，maxStack：递减栈

        for i in range(n):
            while(minStack and nums[i] < nums[minStack[-1]]): # 如果当前数压不到栈里去，就要出栈再压
                minStack.pop()
            # 压得到，则栈尾为最近的最小数，压栈
            minleft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            while(maxStack and nums[i] >= nums[maxStack[-1]]): # 如果当前数压不到栈里去，就要出栈再压
                maxStack.pop()
            # 压得到，则栈尾为最近的最小数，压栈
            maxleft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minStack, maxStack = [], [] # clear，后面操作类似
        for i in range(n-1, -1, -1):
            while(minStack and nums[i] <= nums[minStack[-1]]): # 注意这里要取等而上面不取
                minStack.pop()
            minright[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while(maxStack and nums[i] > nums[maxStack[-1]]): # 注意这里不取等而上面取
                maxStack.pop()
            maxright[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)
        
        for i in range(n):
            Sum_min += (i - minleft[i]) * (minright[i] - i) * nums[i]
            Sum_max += (i - maxleft[i]) * (maxright[i] - i) * nums[i]

        return Sum_max - Sum_min