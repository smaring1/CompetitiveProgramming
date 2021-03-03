class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        times = {x: 0 for x in range(0, n+1)}
        for i in nums:
            times[i] += 1
        for i in times.keys():
            if times[i] == 0:
                return i