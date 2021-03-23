class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = A + ' ' + B
        words = {x: 0 for x in c.split()}
        for i in c.split():
            words[i] += 1
        sol = []
        for i in words.keys():
            if words[i] == 1:
                sol.append(i)
        return sol