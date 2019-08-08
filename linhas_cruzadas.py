#https://olimpiada.ic.unicamp.br/pratique/p1/2015/f1/linhas/
qntNum = int(input())
ordemNum = input().split()
ordemNum = list(map(int, ordemNum))
trocas = 0

for i in range(qntNum):
    if ordemNum[i] > i+1: 
        for j in range(i+1,ordemNum[i]):
            if ordemNum[j] < ordemNum[i]:
                trocas+=1
    elif ordemNum[i] < i+1:
        k = ordemNum[i]-1
        h = i-1
        while h > k:
            if ordemNum[h] > ordemNum[i]:
                trocas+=1
            h-=1           
print(trocas)
