class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        times = {x: 0 for x in nums}
        for i in nums:
            times[i] += 1
        total = 0
        for i in times.keys():
            if times[i] == 1:
                total += i
        return total