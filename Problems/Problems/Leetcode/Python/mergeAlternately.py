class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = ''
        cur = 0
        for i in range(len(min(word1, word2, key=len))):
            sol += word1[i]
            sol += word2[i]
            cur = i
        sol += max(word1, word2, key=len)[cur+1:]
        return sol