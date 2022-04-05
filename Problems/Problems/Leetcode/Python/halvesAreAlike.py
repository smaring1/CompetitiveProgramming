class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = s[len(s)//2:]
        r = s[:len(s)//2]
        vowels = "aeiouAEIOU"
        cont1 = 0
        cont2 = 0
        for i in range(len(l)):
            if l[i] in vowels:
                cont1 += 1
            if r[i] in vowels:
                cont2 += 1
        return cont1 == cont2