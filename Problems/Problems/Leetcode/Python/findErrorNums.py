class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        conj = {x: 0 for x in range(1,n+1)}
        for i in nums:
            conj[i] += 1
        result = []
        for i in conj.keys():
            if conj[i] == 2:
                result.append(i)
        for i in conj.keys():
            if conj[i] == 0:
                result.append(i)
        return result