#https://www.urionlinejudge.com.br/judge/en/problems/view/1121

def novaDirecao(direcao,comando):
    if direcao == "N":
        if comando == "D":
            direcao = "L"
        else:
            direcao = "O"
    elif direcao == "S":
        if comando == "D":
            direcao = "O"
        else:
            direcao = "L"
    elif direcao == "L":
        if comando == "D":
            direcao = "S"
        else:
            direcao = "N"
    elif direcao == "O":
        if comando == "D":
            direcao = "N"
        else:
            direcao = "S"
    return direcao

def norte(arena,posicaoInicial):
    figurinhas = 0
    if arena[posicaoInicial[0]-1][posicaoInicial[1]] == "*":
        figurinhas+= 1
        arena[posicaoInicial[0]-1][posicaoInicial[1]] = "."
        posicaoInicial[0] = posicaoInicial[0] - 1
    elif arena[posicaoInicial[0]-1][posicaoInicial[1]] == ".":
        posicaoInicial[0] = posicaoInicial[0] - 1
    return figurinhas

def sul(arena,posicaoInicial):
    figurinhas = 0
    if arena[posicaoInicial[0]+1][posicaoInicial[1]] == "*":
        figurinhas+= 1
        arena[posicaoInicial[0]+1][posicaoInicial[1]] = "."
        posicaoInicial[0] = posicaoInicial[0] + 1
    elif arena[posicaoInicial[0]+1][posicaoInicial[1]] == ".":
        posicaoInicial[0] = posicaoInicial[0] + 1
    return figurinhas

def leste(arena,posicaoInicial):
    figurinhas = 0
    if arena[posicaoInicial[0]][posicaoInicial[1]+1] == "*":
        figurinhas+= 1
        arena[posicaoInicial[0]][posicaoInicial[1]+1] = "."
        posicaoInicial[1] = posicaoInicial[1] + 1
    elif arena[posicaoInicial[0]][posicaoInicial[1]+1] == ".":
        posicaoInicial[1] = posicaoInicial[1] + 1
    return figurinhas

def oeste(arena,posicaoInicial):
    figurinhas = 0
    if arena[posicaoInicial[0]][posicaoInicial[1]-1] == "*":
        figurinhas+= 1
        arena[posicaoInicial[0]][posicaoInicial[1]-1] = "."
        posicaoInicial[1] = posicaoInicial[1] - 1
    elif arena[posicaoInicial[0]][posicaoInicial[1]-1] == ".":
        posicaoInicial[1] = posicaoInicial[1] - 1
    return figurinhas

while True:
        #entrada de Dados 
        entrada = input().split()
        if entrada == ["0","0","0"]:
            break
        nLinhas = int(entrada[0])
        nColunas = int(entrada[1])
        nComandos = int(entrada[2])

        #plotar arena
        arena = []
        posicaoInicial = [None,None]
        linhaNula = ["!"]*(nColunas+2) #limite da arena
        arena.append(linhaNula)
        for i in range(nLinhas):
            linha = list(input())
            if posicaoInicial[0] == None:
                for j in linha:
                    if j == "N" or j == "S" or j == "L" or j == "O":
                        posicaoInicial[0]=(i+1)
                        posicaoInicial[1]=(linha.index(j)+1)
            linha.insert(0,"!")
            linha.append("!")
            arena.append(linha)
        arena.append(linhaNula)


        #entrada comandos
        comandos = list(input())
        
        #executar
        figurinhasGlobal = 0
        direcaoAtual = arena[posicaoInicial[0]][posicaoInicial[1]]
        arena[posicaoInicial[0]][posicaoInicial[1]] = "."
        for i in range(nComandos):
            if comandos[i] == "F":
                if direcaoAtual == "N":
                    x = norte(arena,posicaoInicial)
                    if x == 1:
                        figurinhasGlobal+=1
                elif direcaoAtual == "S":
                    x = sul(arena,posicaoInicial)
                    if x == 1:
                        figurinhasGlobal+=1
                elif direcaoAtual == "L":
                    x = leste(arena,posicaoInicial)
                    if x == 1:
                        figurinhasGlobal+=1
                elif direcaoAtual == "O":
                    x = oeste(arena,posicaoInicial)
                    if x == 1:
                        figurinhasGlobal+=1
            elif comandos[i] == "D":
                y = novaDirecao(direcaoAtual,"D")
                direcaoAtual = y
            else:
                y = novaDirecao(direcaoAtual,"E")
                direcaoAtual = y
        print(figurinhasGlobal)


            



        
        

    

    
    
            
        
            
                

   

    

    





    
        
        
        
