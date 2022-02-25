class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        cont1 = 0
        cont2 = 0
        for i in range(len(version1)):
            cont1 += int(version1[i]) * (10**(i*(-1)))
        for i in range(len(version2)):
            cont2 += int(version2[i]) * (10**(i*(-1)))
        if cont1 > cont2:
            return 1
        if cont1 < cont2:
            return -1
        if cont1 == cont2:
            return 0