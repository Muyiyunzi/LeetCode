# 接受拒绝采样是这类问题最稳的方式。
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.center = [x_center, y_center]
        self.r = radius


    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [self.center[0] + x, self.center[1] + y]

# 当然如果要去推断概率密度函数什么的，通俗理解就是，表达式忽略系数的逆函数