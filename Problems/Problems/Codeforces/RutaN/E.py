sRequired = list(map(int, input().split()))
sHackers = list(map(int, input().split()))
can = 0
hackerD = []
requiredD = []
for i in sHackers:
    for j in sRequired:
        if ((i > j) and (i not in hackerD) and (j not in requiredD)):           
            can += 1
            hackerD.append(i)
            requiredD.append(j)
       
print(can)