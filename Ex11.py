# Escreva um programa que solicite ao usu�rio o n�mero de elementos (N) a serem armazenados em um vetor. Em seguida, crie um vetor do referido tamanho (N).
# O programa deve solicitar a digita��o de N n�meros, armazenando-os no vetor. Caso o usu�rio informe um valor valor para N, menor ou igual a zero, o programa deve simplesmente mostrar a mensagem �Nada a processar!�. Caso contr�rio o programa deve:
# Exibir os n�meros na ordem inversa em que foram digitados.
# DICA: Quando queremos percorrer 1 vetor de �N� elementos, �pra frente� usamos uma vari�vel que vai de 0 at� N-1 (incrementando de 1 em 1); Para percorr�-lo na ordem inversa, basta come�ar a percorrer da posi��o �N-1� at� a posi��o 0 (decrementando de 1 em 1). A ideia nessa atividade n�o � usar �fun��es prontas� para percorrer na ordem inversa.
# Mostrar quantos dos n�meros s�o pares e quantos s�o �mpares.

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
    
    print('Os elementos na ordem inversa da entrada s�o:',lista)
    
    
    print('Quantidade de pares: ',par)
    print('Quantidade de �mpares: ',impar)