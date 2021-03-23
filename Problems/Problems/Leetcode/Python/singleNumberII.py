class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 1
        else:
            for i in range(1, len(nums)-1):
                if nums[i-1] != nums[i] and nums[i-1] != nums[i+1] and i == 1:
                    return nums[i-1]
                if nums[i+1] != nums[i] and nums[i+1] != nums[i-1] and i == len(nums)-2:
                    return nums[i+1]
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]