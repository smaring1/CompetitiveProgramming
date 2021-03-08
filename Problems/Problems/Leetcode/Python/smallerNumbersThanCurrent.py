class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = []
        for i in range(n):
            cont = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    cont += 1
            sol.append(cont)
        return sol