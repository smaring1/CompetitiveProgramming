class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        i = int(len(b)/len(a)) + 1
        if b in a*(i-1):
            return i-1
        elif b in a*i:
            return i
        elif b in a*(i+1):
            return i+1
        return -1