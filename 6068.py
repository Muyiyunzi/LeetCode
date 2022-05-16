# 来自灵神的讨论右端点在瓷砖右侧。注意注释部分的坑点，0变-1的灵异事件。
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        left = ans = cover = 0
        for tileLeft, tileRight in tiles:
            cover += tileRight - tileLeft + 1
            # while tileRight - carpetLen + 1 >= tiles[left][0]:
            while tileRight - carpetLen + 1 > tiles[left][1]:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # ans = max(ans, cover + max(tiles[left-1][1] - tileRight + carpetLen, 0)) # 这样一开始会搞出来个-1，就gg了
            ans = max(ans, cover - max(tileRight - carpetLen + 1 - tiles[left][0], 0))
        return ans

# 来自另一个评论区的固定左端点瓷砖左侧，更好想一些，也不错
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        right = ans = cover = 0
        n = len(tiles)
        for left in range(n):
            while right < n and tiles[right][1] < tiles[left][0] + carpetLen - 1:
                cover += tiles[right][1] - tiles[right][0] + 1
                right += 1
            if right < n and tiles[right][0] <= tiles[left][0] + carpetLen - 1:
                ans = max(ans, cover + tiles[left][0] + carpetLen - tiles[right][0])
            else:
                ans = max(ans, cover)
            cover -= tiles[left][1] - tiles[left][0] + 1
        return ans