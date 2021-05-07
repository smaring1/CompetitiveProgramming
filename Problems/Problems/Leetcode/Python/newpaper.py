tests = int(input())
for i in range(tests):
    charnum = int(input())
    chars = {}
    for _ in range(charnum):
        cur = input().split()
        chars.update({cur[0]: int(cur[1])})
    lines = int(input())
    total = 0
    for j in range(lines):
        curline = input()
        for i in curline:
            try:
                total += chars[i]
            except:
                pass
    sol = total/100.0
    out = str(sol)
    if len(out.split(".")[1]) < 2:
        out += "0"
    print(out+"$")