class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutives = 0
        maximum = 0
        for i in arr:
            if consecutives >= maximum:
                maximum = consecutives
            if i % 2 != 0:
                consecutives += 1
            else:
                consecutives = 0
        if consecutives >= maximum:
            maximum = consecutives
        return maximum >= 3