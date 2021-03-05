class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        cont = 0
        for i in nums:
            if i == 1:
                cont += 1
            else:
                if cont > maximum:
                    maximum = cont
                cont = 0
        if cont > maximum:
            maximum = cont
        return maximum