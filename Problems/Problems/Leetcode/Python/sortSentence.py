class Solution:
    def sortSentence(self, s: str) -> str:
        n = len(s.split())
        words = [0] * n
        for i in s.split():
            words[int(i[-1])-1] = i[:-1]
        return " ".join(words)