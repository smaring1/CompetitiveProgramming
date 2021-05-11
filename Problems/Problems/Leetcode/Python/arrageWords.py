class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        words = text.split()
        words.sort(key=len)
        words[0] = words[0].capitalize()
        sol = ""
        for i in words:
            sol += i + " "
        return sol.rstrip()