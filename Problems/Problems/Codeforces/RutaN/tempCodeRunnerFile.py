

t = int(sys.stdin.readline().rstrip('\n'))
for i in range(t):
    n,r,p = map(int, sys.stdin.readline().rstrip('\n').split())
    years = math.ceil((ln(p)-ln(n))/ln((