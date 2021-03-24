class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n < 3:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
        else:
            values = [0]*(n+1)
            values[0] = 0
            values[1] = 1
            values[2] = 1
            for i in range(3, n+1):
                values[i] = values[i-1] + values[i-2] + values[i-3]
            return values[n]