class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in range(n):
            ind = arr.index(max(arr[:n-i]))
            arr[:ind+1] = arr[ind::-1]
            arr[:n-i] = arr[n-1-i::-1]
            ans.append(ind+1)
            ans.append(n-i)
        return ans