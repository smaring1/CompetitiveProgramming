ancho = int(input())
largo = int(input())

result = ""
for i in range(largo):
    for j in range(ancho):
        if j == ancho//2 or i == largo//2:
            result += "+"
        else:
            result += "0"
    print(result)
    result = ""
