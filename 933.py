# 注意deque是可以用q[0]也可以用len这种操作的
class RecentCounter:

    def __init__(self):
        self.logs = deque()

    def ping(self, t: int) -> int:
        self.logs.append(t)
        while(self.logs[0] < t - 3000):
            self.logs.popleft()
        return len(self.logs)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)