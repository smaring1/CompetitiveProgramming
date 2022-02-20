import sys
case = 1
while(True):
    try:
        p = int(input())
    except:
        break
    scores = []
    for i in range (p):
        aux = input().split(';')
        player = aux[0]
        aScores = aux[1:]
        auxScore = 0
        for i in range(len(aScores)):
            pScore = aScores[i].split()
            for i in range(len(pScore)):
                if i == len(pScore)-1 and int(pScore[i]) == 1:
                    auxScore += 2
                else:
                    auxScore +=int(pScore[i])
        scores.append((player,auxScore))
    scores.sort(key = lambda x: (-x[1],x[0].lower()))
    print(f'Case {case}:')
    for score in scores:
        print(score[0],score[1])
    case += 1