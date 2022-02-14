t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    ids = [0]*n
    for j in range(n):
        ids[j] = int(input().split('/')[-1])
    ids.sort()
    strtp = ""
    for a in range(k):
        strtp += str(ids[a]) + ' '
    print(strtp[:-1])