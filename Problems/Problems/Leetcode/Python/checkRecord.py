class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i in s:
            if i == 'A':
                absent += 1
            if absent >= 2:
                return False
        return not 'LLL' in s