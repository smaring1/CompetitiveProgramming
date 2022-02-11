tests = int(input())
nodes = list(map(int, input().split()))
mini = 0
if len(nodes) > 1:
    temp = nodes[0] + nodes[1]
    mini = min(temp,nodes[0],0)
    
    for i in range(2, len(nodes)):
        temp += nodes[i]
        if temp < mini:
            mini = temp 
print(abs(mini))
