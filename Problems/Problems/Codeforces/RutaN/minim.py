size = input()
v = input().split()
total = 0
for i in v:
    if i == '0':
        total += 2
    else:
        total += 1/int(i)
if total % int(total) == 0:
    print(int(total))
else:
    print(round(total, 4))