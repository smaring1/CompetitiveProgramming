n = int(input())
triangle = [0]*n
for i in range(n):
    triangle[i] = list(map(int, input().split()))
    
cont = 0
for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] = max(triangle[i][j] + triangle[i+1][j], triangle[i][j] + triangle[i+1][j+1])
print(triangle[0][0])
    

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         cont = 0
#         n = len(triangle)
#         for i in range(n-2, -1, -1):
#             for j in range(len(triangle[i])):
#                 triangle[i][j] = max(triangle[i][j] + triangle[i+1][j], triangle[i][j] + triangle[i+1][j+1])
#         return triangle[0][0]