# 第一版
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i = 0
        dominoes = list(dominoes)
        while(i < len(dominoes) - 1):
            j = i + 1
            while(j < len(dominoes) - 1 and dominoes[j] == '.'):
                j += 1
            if dominoes[i] == '.' or dominoes[i] == 'L':
                if dominoes[j] == 'L':
                    dominoes[i:j] = 'L' * (j - i)
                    j += 1
                # dominoes[j] == 'R': do nothing
            else: # dominoes[i] == 'R':
                if dominoes[j] == 'L':
                    for k in range(i, j):
                        if k < (j + i) / 2:
                            dominoes[k] = 'R'
                        elif k > (j + i) / 2:
                            dominoes[k] = 'L'
                    j += 1
                else: # dominoes[j] == 'R' or '.' with the last:
                    dominoes[i:j+1] = 'R' * (j + 1 - i)
            i = j
        return "".join(dominoes)