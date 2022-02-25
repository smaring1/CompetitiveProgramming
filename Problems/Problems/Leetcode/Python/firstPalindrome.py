class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s: str):
            n = len(s)
            for i in range(n):
                if s[i] != s[n-i-1]:
                    return False
            return True
        
        for i in words:
            if isPalindrome(i):
                return i
        return ""