class Solution:
    def findComplement(self, num: int) -> int:
        sol = ''
        binary = bin(num)
        for i in binary[2:]:
            if i == '0':
                sol += '1'
            else:
                sol += '0'
        sol = int('0b' + sol, 2)
        return sol