class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        ans = []
        for ind, word in enumerate(words):
            if word[0] not in vowel:
                ans.append(word[1:] + word[0] + 'ma' + 'a' * (ind + 1))
            else:
                ans.append(word + 'ma' + 'a' * (ind + 1))
        return ' '.join(ans)