class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {x:0 for x in s}
        for i in s:
            letters[i] += 1
        sorte = {k: v for k, v in sorted(letters.items(), key=lambda item: item[1], reverse=True)}
        sol = ""
        for i in sorte.keys():
            for j in range(sorte[i]):
                sol += i
        return sol