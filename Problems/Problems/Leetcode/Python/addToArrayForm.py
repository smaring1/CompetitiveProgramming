class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = ""
        for i in num:
            number += str(i)
        conv = int(number)
        return list(str(k+conv))