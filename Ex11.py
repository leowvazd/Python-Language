# Escreva um programa que solicite ao usuário o número de elementos (N) a serem armazenados em um vetor. Em seguida, crie um vetor do referido tamanho (N).
# O programa deve solicitar a digitação de N números, armazenando-os no vetor. Caso o usuário informe um valor valor para N, menor ou igual a zero, o programa deve simplesmente mostrar a mensagem “Nada a processar!”. Caso contrário o programa deve:
# Exibir os números na ordem inversa em que foram digitados.
# DICA: Quando queremos percorrer 1 vetor de “N” elementos, “pra frente” usamos uma variável que vai de 0 até N-1 (incrementando de 1 em 1); Para percorrê-lo na ordem inversa, basta começar a percorrer da posição “N-1” até a posição 0 (decrementando de 1 em 1). A ideia nessa atividade não é usar “funções prontas” para percorrer na ordem inversa.
# Mostrar quantos dos números são pares e quantos são ímpares.

n = int(input())
vetores = []
a = n
soma = 0
par = impar = 0

if n <= 0 or n==0:
    print('Nada a processar!')

else:
    
    for i in range(a):
        v = int(input(''))
        if v % 2 == 0:
            par = par + 1

        else:
            impar = impar + 1
        vetores .append(v)
    lista = vetores [::-1]
    
    print('Os elementos na ordem inversa da entrada são:',lista)
    
    
    print('Quantidade de pares: ',par)
    print('Quantidade de ímpares: ',impar)