import math 
sNumber = input()
number = int(sNumber) 
print(math.log(int(sNumber),10))
tenCondition = 1 if str(math.log(int(sNumber),10))[-1] == '0' else 0
multiplication = 10 ** (len(sNumber) - 1 - tenCondition)

if multiplication > 0 and number > 10:
    aux = str(10 - (int(sNumber[0])))
    resta = int(aux*(len(sNumber) - 1))
    print((number * multiplication) - resta)
else:
    print(number-1)