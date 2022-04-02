class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
        cont = 0
        for i in range(len(s)):
            if i < len(s)-1 and values[s[i]] < values[s[i+1]]:
                cont -= values[s[i]]
            else:
                cont += values[s[i]]
        return cont