# Escreva um programa que leia v�rios n�meros armazenando-os em um vetor �V�. A entrada dever� ser encerrada quando for lido um n�mero negativo. 
# Caso o primeiro n�mero informado seja negativo o programa deve simplesmente mostrar a mensagem �Nada a processar!�. 
# Ap�s ler e armazenar os elementos do vetor V, seu programa deve:
# exibir os elementos do Vetor �V�. 
# exibir o elemento que est� na posi��o �  e na posi��o  �  do vetor
# Aten��o: Em python para obter a posi��o �  do vetor use a seguinte express�o  (N*3//4). Note que � preciso usar o operador // (divis�o inteira) ao inv�s do /
# Em seguida o programa deve �inverter� os conte�dos de V, fazendo com que o �ltimo elemento passe a ser o primeiro, o pen�ltimo passe a ser o segundo e assim por diante �
# Ap�s a invers�o dos elementos do vetor V, seu programa deve:
# exibir os elementos do Vetor �V� (na nova ordem). 
# exibir o elemento que est� na posi��o �  e na posi��o  �  do vetor (na nova ordem)

# Entrada: 23, 27, 19, 18, 22, 25, 29, 24, 23, 22, -1
# Sa�da Esperada: 
# Vetor original:
# 23
# 27
# 19
# 18
# 12
# 15
# 29
# 24
# 23
# 22
# O vetor tem 10 elementos
# Elemento da posi��o 1/4, ou seja, posi��o 2 = 19
# Elemento da posi��o 3/4, ou seja, posi��o 7 = 24
# Vetor invertido:
# 22
# 23
# 24
# 29
# 15
# 12
# 18
# 19
# 27
# 23
# Elemento da posi��o 1/4, ou seja, posi��o 2 = 24
# Elemento da posi��o 3/4, ou seja, posi��o 7 = 19

v = list()
num = int(input())
x = 0
cont = 0
j = 0
k = 0

if num < 0:
    print('Nada a processar!')
    
else:
    while num >= 0:
        n=0
        n2=0
        m = 0
        m2 = 0
        v.append(num)
        num = int(input(''))
        tamanho = len(v)

    
    for i in range (tamanho):
        tamanho = v[::-1]
        cont = cont+1
    n = v[(cont*1//4)]
    n2 = v[(cont*3//4)]
    m = (cont*1//4)
    m2 = (cont*3//4)
    
    
    print('Vetor original:')

    for j in range (cont):
        print(v[j])
        j = j+1
    

    print('O vetor tem',cont,'elementos')
    print('Elemento da posi��o 1/4, ou seja, posi��o',m,' = ',n)
    print('Elemento da posi��o 3/4, ou seja, posi��o',m2,' = ',n2)
    print('Vetor invertido:')
    
    copia1 = n
    copia2 = n2
    
    for k in range (cont):
        print(v[cont-1])
        cont = cont-1
    
    print('Elemento da posi��o 1/4, ou seja, posi��o',m,' = ',n2)
    print('Elemento da posi��o 3/4, ou seja, posi��o',m2,' = ',n)
        
