def fulCom(graph,visited,s):
    if not visited[s]:
        print(s)
        visited[s] = True
        for i in graph[s]:
            if not visited[i]:
                fulCom(graph,visited,i)
    return visited

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append([])
for i in range(m):
    conexions = list(map(int, input().split()))
    if conexions[0] == 1:
        graph[conexions[1]-1].append(conexions[2]-1)
    else:
        for i in range(1,conexions[0]-1):
            graph[conexions[i]-1].append(conexions[i+1]-1)
            graph[conexions[i+1]-1].append(conexions[i]-1)
can = True
for i in range(n):
    visited = [False]*n
    visited = fulCom(graph,visited,i)
    print(visited)
    if False in visited:
        print("NO")
        can = False
        break
if can:
    print("YES")
    