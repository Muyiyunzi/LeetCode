class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = num1.split('+')
        a2, b2 = num2.split('+')
        a1, a2 = int(a1), int(a2)
        b1, b2 = int(b1[:-1]), int(b2[:-1])
        ans_a = a1 * a2 - b1 * b2
        ans_b = a1 * b2 + b1 * a2
        return str(ans_a)+'+'+str(ans_b)+'i'