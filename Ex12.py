# Escreva um programa que leia vários números armazenando-os em um vetor. A entrada deverá ser encerrada quando for lido um número negativo. Após a leitura dos elementos do vetor, você deve exibir solicitar ao usuário que ele digite um número “K” a ser pesquisado no vetor. O programa deve fornecer como saída quantas vezes o número “K” aparece no vetor, a quantidade de elementos do vetor e também o percentual de “K” em relação ao número de elementos no vetor.

# CASO DE TESTE 1:
# Entrada: 
# 4  10  5  10  1  10  7  2 -1
# K = 10
# Saída Esperada: 
# O 10 aparece 3 vezes entre os 8 elementos do vetor. 
# Isto corresponde a 37.5 %.

lista = list()
num = int(input())
porcent = 0
k = 0
cont = 0

while num >= 0:
    lista.append(num)
    num = int(input(''))
tamanho = len(lista)
k = int(input(''))
    
for i in range (tamanho):

    if lista[i] == k:
        cont = cont+1
        
porcent = cont/tamanho
print(k,'aparece',cont,'vezes entre os',tamanho,'elementos do Vetor')
print(f'Isto corresponde a {porcent:.1%}')        