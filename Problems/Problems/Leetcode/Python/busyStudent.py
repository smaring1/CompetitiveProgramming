class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        doing = 0
        n = len(startTime)
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                doing += 1
        return doing