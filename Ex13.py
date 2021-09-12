# Escreva um programa que leia vários números armazenando-os em um vetor “V”. A entrada deverá ser encerrada quando for lido um número negativo. 
# Caso o primeiro número informado seja negativo o programa deve simplesmente mostrar a mensagem “Nada a processar!”. 
# Após ler e armazenar os elementos do vetor V, seu programa deve:
# exibir os elementos do Vetor “V”. 
# exibir o elemento que está na posição ¼  e na posição  ¾  do vetor
# Atenção: Em python para obter a posição ¾  do vetor use a seguinte expressão  (N*3//4). Note que é preciso usar o operador // (divisão inteira) ao invés do /
# Em seguida o programa deve “inverter” os conteúdos de V, fazendo com que o último elemento passe a ser o primeiro, o penúltimo passe a ser o segundo e assim por diante …
# Após a inversão dos elementos do vetor V, seu programa deve:
# exibir os elementos do Vetor “V” (na nova ordem). 
# exibir o elemento que está na posição ¼  e na posição  ¾  do vetor (na nova ordem)

# Entrada: 23, 27, 19, 18, 22, 25, 29, 24, 23, 22, -1
# Saída Esperada: 
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
# Elemento da posição 1/4, ou seja, posição 2 = 19
# Elemento da posição 3/4, ou seja, posição 7 = 24
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
# Elemento da posição 1/4, ou seja, posição 2 = 24
# Elemento da posição 3/4, ou seja, posição 7 = 19

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
    print('Elemento da posição 1/4, ou seja, posição',m,' = ',n)
    print('Elemento da posição 3/4, ou seja, posição',m2,' = ',n2)
    print('Vetor invertido:')
    
    copia1 = n
    copia2 = n2
    
    for k in range (cont):
        print(v[cont-1])
        cont = cont-1
    
    print('Elemento da posição 1/4, ou seja, posição',m,' = ',n2)
    print('Elemento da posição 3/4, ou seja, posição',m2,' = ',n)
        
