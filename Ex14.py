# Escreva um programa para ler os elementos de uma matriz “A” de NxM. Os valores de N e M também serão informados previamente pelo usuário. Após ler todos os NxM elementos da matriz “A” o programa deve:
# Imprimir a matriz (os valores devem ser separados por “|”)
# Use print("%4d" % A[l][c], end="|")
# O %4d faz com que os números sejam ajustados em 4 posições inteiras, independentemente do número de dígitos
# Solicitar ao usuário que digite o valor de “K” a ser procurado na matriz.
# Exibir quantas vezes o valor “K” aparece em cada linha.
# Observações: 
# Note que o valor de “K” somente será lido após toda a matriz ser lida

n = int(input())
m = int(input())
i = 0
c = 0
M = []
v = 0
j = 0

for i in range(0,n):
    linha = []
    for v in range(0,m):
        d = int(input())
        linha.append(d)
    M.append(linha)
        
k = int(input())

print ('Elementos da Matriz:')

for l in range(0,n):       
    for c in range (0,m):  
      print('%4d' %M[l][c], end="| ")
    print("")

for l in range(0,n):
    for v in range(0,m):
        if M[l][v] == k:
            j = j+1
    print('{} aparece {} vezes na linha {}' .format(k,j,l))
    j = 0
    