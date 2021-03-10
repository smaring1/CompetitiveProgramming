class Solution:
    def totalMoney(self, n: int) -> int:
        week = n//7
        res = n%7
        return int(week*21+7*(week+1)*(week)/2 + res*(week+1)+(res-1)*res/2)