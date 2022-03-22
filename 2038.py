class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt_a, cnt_b = 0, 0
        alice, bob = 0, 0
        for i in list(colors):
            if i == 'A':
                cnt_b = 0
                cnt_a += 1
                if cnt_a >= 3:
                    alice += 1
            else:
                cnt_b += 1
                cnt_a = 0
                if cnt_b >= 3:
                    bob += 1
        if bob >= alice:
            return False
        return True