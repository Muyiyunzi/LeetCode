class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashTable = dict()
        for ind, i in enumerate(list1):
            hashTable[i] = ind
        minSum, Sum = 2000, 0
        ans = []
        for ind, i in enumerate(list2):
            if i in hashTable:
                Sum = ind + hashTable[i]
                if Sum < minSum:
                    ans = [i]
                    minSum = Sum
                elif Sum == minSum:
                    ans.append(i)
        return ans

