n = int(input())
nums = []
for _ in range(n):
    nums.append(float(input()))

if n < 3:
    if n == 2:
        print(1 if nums[0] == nums[1] else 0)
else:
    cont = 0
    for i in range(n):
        if sum(nums[:i]) == sum(nums[i:]):
            cont += 1
    print(cont-1)