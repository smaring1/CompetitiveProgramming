while(True):
    entr = input().split()
    if entr == ['0', '0']:
        break
    a = set(input().split())
    b = set(input().split())
    sol = str(len(a.difference(b))) + " " + str(len(a.intersection(b))) + " "  + str(len(b.difference(a))) + " " + str(len(a.union(b)))
    print(sol)