# Escreva um programa que solicite ao usu�rio o n�mero de elementos (N) a serem armazenados em um vetor. Em seguida, crie um vetor do referido tamanho (N).
# O programa deve solicitar a digita��o de N n�meros, armazenando-os no vetor. Caso o usu�rio informe um valor valor para N, menor ou igual a zero, o programa deve simplesmente mostrar a mensagem �Nada a processar!�. Caso contr�rio o programa deve:
# Informar, dentre os n�meros digitados, quais s�o os n�meros maiores que o �ltimo elemento do vetor. 
# Informar,  quantos dos n�meros digitados, s�o maiores que o �ltimo elemento do vetor.

n = int(input(""))
vetores = []
soma = 0

if (n <= 0):
    print ("Nada a processar!")

else:
    for i in range(n):
        v = int(input(""))
        vetores .append(v)
    ultimo = vetores[-1]
    print('Os valores maiores que', ultimo, 's�o:')
    
    for i in vetores [0:-1]:
        if i > ultimo:
            print(i)
            soma = soma+1
    print('A quantidade de elementos maiores que',ultimo,'s�o:',soma)