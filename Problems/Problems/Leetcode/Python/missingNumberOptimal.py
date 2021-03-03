class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n+1) / 2
        real = sum(nums)
        missing = total - real
        return int(missing)