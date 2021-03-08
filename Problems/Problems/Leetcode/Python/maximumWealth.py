class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sol = [0]*len(accounts)
        for i in range(len(accounts)):
            sol[i] = sum(accounts[i])
        return max(sol)