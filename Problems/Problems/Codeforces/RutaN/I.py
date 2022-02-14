t = int(input())
n = int(input())
array = list(map(int, input().split()))
ocurrences = {}
for i in array:
    if i in ocurrences.keys():
        ocurrences[i] += 1
    else:
        ocurrences[i] = 1
        