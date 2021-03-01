class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        types = {x: 0 for x in candyType}
        c = len(types.keys())
        if c > n/2:
            return int(n/2)
        if c < n/2:
            return c
        if c == n/2:
            return int(n/2)
        