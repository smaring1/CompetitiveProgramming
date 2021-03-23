class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        times = {x: 0 for x in arr}
        for i in arr:
            times[i] += 1
        return len(times.values()) == len(set(times.values()))