class Solution:
    def findComplement(self, num: int) -> int:
        return int('0b'+''.join(list(map(lambda x: '0' if x == '1' else '1', bin(num)[2:]))), 2)
    
    

class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)
        sol = list(map(lambda x: '0' if x == '1' else '1', num[2:]))
        return int('0b'+''.join(sol), 2)