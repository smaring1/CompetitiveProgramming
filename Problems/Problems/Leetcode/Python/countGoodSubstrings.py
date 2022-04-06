class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cont = 0
        for i in range(0, len(s)-2):
            diff = set()
            
            for j in range(i, i+3):
                diff.add(s[j])
            
            if len(diff) == 3:
                cont += 1
        
        return cont