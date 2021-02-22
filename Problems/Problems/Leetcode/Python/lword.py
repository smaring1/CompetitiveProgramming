class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        estan = []
        for word in d:
            i = 0
            for j in range(len(s)):
                if i >= len(word): break
                if s[j] == word[i]: i += 1
            if len(word) == i:
                estan.append(word)
        estan.sort()
        estan.sort(key = lambda x: len(x), reverse = True)
        if estan:
            return estan[0]
        else:
            return ""