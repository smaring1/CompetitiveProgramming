class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxi = heights[-1]
        sol = [len(heights)-1]
        heights = heights[::-1]
        
        for i in range(1, len(heights)):
            if heights[i] > maxi:
                sol.append(len(heights)-i-1)
                maxi = heights[i]
        return sol [::-1]