# Escreva um programa que leia v�rios n�meros armazenando-os em um vetor. A entrada dever� ser encerrada quando for lido um n�mero negativo. Ap�s a leitura dos elementos do vetor, voc� deve exibir solicitar ao usu�rio que ele digite um n�mero �K� a ser pesquisado no vetor. O programa deve fornecer como sa�da quantas vezes o n�mero �K� aparece no vetor, a quantidade de elementos do vetor e tamb�m o percentual de �K� em rela��o ao n�mero de elementos no vetor.

# CASO DE TESTE 1:
# Entrada: 
# 4  10  5  10  1  10  7  2 -1
# K = 10
# Sa�da Esperada: 
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