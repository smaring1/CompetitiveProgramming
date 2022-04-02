class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for i in range(10)]
        for i in range(0, len(rings), 2):
            pole = int(rings[i+1])
            curring = rings[i]
            rods[pole].add(curring)
        cont = 0
        for i in rods:
            if len(i) == 3:
                cont += 1
        return cont