class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        cur = ""
        sol = []
        for i in searchWord:
            cur += i
            prods = []
            for j in products:
                if j.startswith(cur):
                    prods.append(j)
            prods.sort()
            sol.append(prods[:3])
        return sol