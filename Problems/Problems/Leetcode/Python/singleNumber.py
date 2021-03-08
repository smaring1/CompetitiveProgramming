class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        times = {x: 0 for x in nums}
        for i in nums:
            times[i] += 1
        for i in times:
            if times[i] == 1:
                return i