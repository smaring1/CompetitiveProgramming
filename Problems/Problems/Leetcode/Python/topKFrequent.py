class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {n: 0 for n in nums}
        for i in nums:
            x[i] += 1
        sort = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
        vals = list(sort.keys())
        sol = [0]*k
        for i in range(k):
            sol[i] = vals[i]
        return sol