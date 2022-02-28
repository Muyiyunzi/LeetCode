# 4、9特判的除法
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        hashMap = dict(zip([1000,500,100,50,10,5,1], ['M','D','C','L','X','V','I']))
        for k in hashMap.keys():
            val = num // k
            if val == 4:
                if ans and ans[-1] == hashMap[k*5]: # 9
                    ans = ans[:-1] + hashMap[k] + hashMap[k*10]
                else:
                    ans += hashMap[k] + hashMap[k*5]
            else:
                ans += hashMap[k] * (num // k)
            num -= num // k * k
        return ans

# 将4、9硬编码
class Solution:
    def intToRoman(self, num: int) -> str:
        d = dict(zip([1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']))
        ans = ''
        for key in d.keys():
            while num >= key:
                ans += d[key]
                num -= key
        return ans