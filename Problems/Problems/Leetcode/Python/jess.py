'''
Código por: Simón Marín Giraldo
Para asesorías, escribir por WhatsApp:
3218547580
Instagram: @simonmarin_
'''

def suma_digitos(num):
    order = 0
    if num == 0:
        order = 1
    else:
        cur = 0
        order = 0
        mod = 10
        while(cur != num):
            order += 1
            cur = num % mod
            mod *= 10
    total = 0
    for i in range(order):
        total += (num//10**(order-1-i)%10)
    return total

def suma_digitos_rango(start, end):
    total = 0
    for i in range(start, end+1):
        total += suma_digitos(i)
    return total

def generar_tripletas():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                yield [k, j, i]

def manos_arriba(n):
    personas = [0, 0, 0]
    if n == 0:
        return personas
    else:
        sol = []
        gen = generar_tripletas()
        for i in range(n+1):
            sol = next(gen)
        return sol

print(manos_arriba(9))
