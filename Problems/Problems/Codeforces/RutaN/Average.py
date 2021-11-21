size = int(input())

for i in range(size):
    tests,students = input().split()
    scores = input().split()
    scores = [int(i) for i in scores]
    totalPoints = sum(scores)
    for i in range(int(students)):
        studentScores = input().split()
        studentScore = 0
        for i in range(int(tests)):
            studentScore += (int(scores[i]) * int(studentScores[i]) / 100)
        studentScore = studentScore / totalPoints * 100
        
        studentScoreAux = str(studentScore).split('.')
        studentScoreAux[1] = float(studentScoreAux[0][-1] + '.' + studentScoreAux[1])
        studentScoreAux[0] = studentScoreAux[0][1] if len(studentScoreAux[0]) == 2 else 0
    
        if  int(studentScoreAux[1]) > 7.5:
            print(int(f'{studentScoreAux[0]+1}0'),'UP')
        elif int(5 > studentScoreAux[1]) < 7.5:
            print(int(f'{studentScoreAux[0]}5'),'DOWN')
        elif int(2.5 > studentScoreAux[1]) < 5:
            print(int(f'{studentScoreAux[0]}5'),'UP')
        if  int(studentScoreAux[1]) < 2.5:
            print(int(f'{studentScoreAux[0]}0'),'DOWN')    
        else:
            print(int(f'{studentScoreAux[0]}5'),'SAME')
        