class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            valid = False
            for j in i:
                if not j in allowed:
                    valid = False
                    break
                else:
                    valid = True
            if valid:
                count += 1
        return count