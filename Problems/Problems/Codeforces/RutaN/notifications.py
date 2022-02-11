cases = int(input())
finished = 0
for i in range(cases):
    time, pending = map(int, input().split())
    if finished >= time:
        finished += pending
    else:
        finished = time + pending
print(finished)