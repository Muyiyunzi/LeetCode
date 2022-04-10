class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = defaultdict(bool)
        vocab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = 0
        for i in words:
            temp = ""
            for j in i:
                temp += vocab[ord(j) - ord('a')]
            if not d[temp]:
                d[temp] = True
                ans += 1
        return ans

# 小薇好强，还是set自动去重厉害~
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = set()
        vocab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            temp = ""
            for j in i:
                temp += vocab[ord(j) - ord('a')]
            d.add(temp)
        return len(d)
            