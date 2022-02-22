# 第一版
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        choices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 6, 10, 14, 22, 26, 15, 21, 30]

        times = dict().fromkeys(choices, 0)
        ones = 0
        for i in nums:
            if i == 1:
                ones += 1
            elif i in choices:
                times[i] += 1

        prime_use = [0] * 31
        # ans = []

        def count(index):
            if index == len(choices):
                return 1
            num = choices[index]
            notuse = 1 * count(index + 1)
            if times[num] == 0 or prime_use[num]:
                return notuse
            if num == 1:
                use = times[num] * count(index + 1)
            else:
                for i in range(num, 31):
                    if gcd(i, num) != 1:
                        prime_use[i] += 1
                # ans.append(num)
                use = times[num] * count(index + 1)
                # print(ans)
                # ans.remove(num)
                for i in range(num, 31):
                    if gcd(i, num) != 1:
                        prime_use[i] -= 1
            return use + notuse

        return(((count(0) - 1) * 2 ** ones) % (10**9 + 7))


# 第二版
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        choices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 6, 10, 14, 22, 26, 15, 21, 30]
        times = Counter(nums)
        prime_lock = [0] * 31

        def count(index):
            if index == len(choices):
                return 1
            num = choices[index]

            # 不使用当前数字
            no_use = 1 * count(index + 1) 
            if times[num] == 0 or prime_lock[num]: # 不存在当前数字或已被其他非互质数占用，必然不可用
                return no_use
            
            # 使用当前数字，上锁→递归考察→解锁
            for i in range(num, 31):
                if gcd(i, num) != 1:
                    prime_lock[i] += 1

            use = times[num] * count(index + 1)

            for i in range(num, 31):
                if gcd(i, num) != 1:
                    prime_lock[i] -= 1

            return use + no_use

        return(((count(0) - 1) * 2 ** times[1]) % (10**9 + 7))