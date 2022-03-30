# 困难，CV大法了。。
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heappush(busy, (start + t, id))
            available.remove(id)
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]