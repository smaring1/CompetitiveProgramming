class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = {x: 0 for x in nums}
        for i in nums:
            numbers[i] += 1
            
        maximum = 0
        for i in numbers.values():
            if i > maximum:
                maximum = i
        if maximum >= 2:
            return True
        else:
            return False