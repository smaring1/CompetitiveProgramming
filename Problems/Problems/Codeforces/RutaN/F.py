t = int(input())
for i in range(t):
    n,m = map(int, input().split()) 
    waste = 0
    for bottle in map(int, input().split()):
        pulsations = 0
        while(pulsations < bottle):
            pulsations += m
        waste += pulsations - bottle
    print(waste)