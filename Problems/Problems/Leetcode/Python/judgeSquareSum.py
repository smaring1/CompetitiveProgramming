import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            calc = (l*l) + (r*r)
            if calc == c:
                return True
            if calc < c:
                l += 1
            if calc > c:
                r -= 1
        return False