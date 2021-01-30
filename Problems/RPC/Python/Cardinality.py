def intersecctionn(a:list, b:list):
    a = set(a)
    b = set(b)
    return len(a.intersection(b))

def diff(a:list, b:list):
    a = set(a)
    b = set(b)
    return len(a.difference(b))

def join(a:list, b:list):
    return len(set(a + b))
    

cases = []
while True:
    cases = input()
    if cases == '0 0':
        break
    m = int(cases.split()[0])
    n = int(cases.split()[1])
    a =  list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(str(diff(a, b)) + " " + str(intersecctionn(a, b)) + " " + str(diff(b, a)) + " " + str(join(a, b)))
