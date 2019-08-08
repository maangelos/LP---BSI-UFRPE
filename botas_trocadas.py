#https://www.urionlinejudge.com.br/judge/en/problems/view/1245
N = int(input())
peDireito = [0]*31 #0 a 30
peEsquerdo = [0]*31 #0 a 30
minimo = float("inf")
maximo = 0
for i in range(N):
    M,L = input().split()
    if int(M) > maximo:
        maximo = int(M)
    elif int(M) < minimo:
        minimo = int(M)
    if L == "D":
        peDireito[int(M)-30] +=1
    elif L == "E":
        peEsquerdo[int(M)-30] += 1
minimo = minimo - 30
maximo = maximo - 29
totalPares = 0
for i in range(minimo,maximo):
    if peDireito[i] == peEsquerdo[i]:
        totalPares += peDireito[i]
    elif peDireito[i] < peEsquerdo[i]:
        totalPares += peDireito[i]
    elif peEsquerdo[i] < peDireito[i]:
        totalPares += peEsquerdo[i]
print(totalPares)
    
        
    
  
