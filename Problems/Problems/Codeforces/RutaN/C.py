import sys

sys.setrecursionlimit(100000)


def combinationsM(word,combination, i = 0, j = 1):
    try:
        word[i:j]
    except:
        return
    if i >= j:
        combinationsM(word,combination, i, j+1)
        return 
    
    if i < len(word) and word[i].isupper():
        combinationsM(word,combination, i+1, j)
        return
    
    if len(word[i:j]) == 0:
        return
    
    if word[i:j] in combination:
        return
    
    
    combination.append(word[i:j])
    combinationsM(word,combination, i+1, j+1)
    combinationsM(word,combination, i, j+1)
    combinationsM(word,combination, i+1, j)
    return


camelCase = input()
combinations = []
combinationsM(camelCase,combinations)
print(len(combinations))
