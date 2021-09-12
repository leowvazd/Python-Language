# Escreva um programa que solicite ao usuário o número de elementos (N) a serem armazenados em um vetor. Em seguida, crie um vetor do referido tamanho (N).
# O programa deve solicitar a digitação de N números, armazenando-os no vetor. Caso o usuário informe um valor valor para N, menor ou igual a zero, o programa deve simplesmente mostrar a mensagem “Nada a processar!”. Caso contrário o programa deve:
# Informar, dentre os números digitados, quais são os números maiores que o último elemento do vetor. 
# Informar,  quantos dos números digitados, são maiores que o último elemento do vetor.

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
    print('Os valores maiores que', ultimo, 'são:')
    
    for i in vetores [0:-1]:
        if i > ultimo:
            print(i)
            soma = soma+1
    print('A quantidade de elementos maiores que',ultimo,'são:',soma)