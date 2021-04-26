class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"
        phrase = ""
        s = s.lower()
        for i in s:
            if i in letters:
                phrase += i
                
        n = len(phrase)
        for i in range(len(phrase)):
            if not phrase[i] == phrase[n-1-i]:
                return False
        return True