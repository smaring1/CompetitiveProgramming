class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub not in mapping:
                mapping.update({nums[i]: i})
            else:
                return [mapping[sub], i]