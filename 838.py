# 第一版
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i = 0
        dominoes = list(dominoes)
        while(i < len(dominoes) - 1):
            j = i + 1
            # 找到一个子序列
            while(j < len(dominoes) - 1 and dominoes[j] == '.'):
                j += 1
            # 左.或L
            if dominoes[i] == '.' or dominoes[i] == 'L':
                if dominoes[j] == 'L': # 右L
                    dominoes[i:j] = 'L' * (j - i)
                    j += 1
                # 右R: 什么也不用做
            else: # 左R:
                if dominoes[j] == 'L': # 右L
                    for k in range(i, j):
                        if k < (j + i) / 2:
                            dominoes[k] = 'R'
                        elif k > (j + i) / 2:
                            dominoes[k] = 'L'
                    j += 1
                else: # 右R或.
                    dominoes[i:j+1] = 'R' * (j + 1 - i)
            i = j
        return "".join(dominoes)

# 第二版
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i, j, n = 0, 1, len(dominoes)
        dominoes = list(dominoes)
        while(j < n):
            # 找到一个子序列
            while(j < n - 1 and dominoes[j] == '.'):
                j += 1
            # 左L/点、右L
            if (dominoes[i] == 'L' or dominoes[i] == '.') and dominoes[j] == 'L':
                dominoes[i:j] = 'L' * (j - i)
            # 左R、右L
            elif dominoes[i] == 'R' and dominoes[j] == 'L':
                k = j
                while(i < k):
                    dominoes[i] = 'R'
                    dominoes[k] = 'L'
                    i += 1
                    k -= 1
            # 左R、右R/点
            elif dominoes[i] == 'R' and (dominoes[j] == 'R' or dominoes[j] == '.'):
                dominoes[i:j+1] = 'R' * (j + 1 - i)
            # 左L/点、右R/点什么也不用做
            i = j
            j += 1
        return "".join(dominoes)

# 第三版 BFS
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        q = deque()
        for ind, value in enumerate(dominoes):
            if value != '.':
                q.append(ind)
        while(q):
            i = q.popleft()
            if dominoes[i] == 'L':
                if q:
                    j = q.pop()
                    if j == i-1:
                        dominoes[i-1] = '.'
                        continue
                    q.append(j)
                if(i - 1 >= 0 and dominoes[i-1] == '.'):
                    dominoes[i-1] = 'L'
                    q.append(i-1)
            else:
                if(i + 1 < len(dominoes) and dominoes[i+1] == '.'):
                    dominoes[i+1] = 'R'
                    q.append(i+1)
        return ''.join(dominoes)