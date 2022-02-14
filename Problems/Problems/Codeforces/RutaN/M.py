import sys
import math
def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

t = int(sys.stdin.readline().rstrip('\n'))
for i in range(t):
    n,r,p = map(int, sys.stdin.readline().rstrip('\n').split())
    years = math.ceil(ln(p)/ln(n*(1 +r)))
    sys.stdout.write(f'Case {i+1}: {years}\n')