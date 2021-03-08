class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        sol = []
        for i in candies:
            if i + extraCandies >= maximum:
                sol.append(True)
            else:
                sol.append(False)
        return sol