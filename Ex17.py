# Escreva um programa que solicite ao usuário o número de elementos (N) a serem armazenados em um vetor. Em seguida, crie um vetor do referido tamanho (N).
# O programa deve solicitar a digitação de N números, armazenando-os no vetor. Caso o usuário informe um valor valor para N, menor ou igual a zero, o programa deve simplesmente mostrar a mensagem “Nada a processar!”. Caso contrário o programa deve:
# Informar, dentre os números digitados, quais são os números maiores que o último elemento do vetor. 
# Informar,  quantos dos números digitados, são maiores que o último elemento do vetor.

def LerVetor(Vet,tamanho):
    for ind in range (0,tamanho):
        aux=int(input(""))
        Vet.append(aux)
    return Vet

#Complete a função ImprimeMaiores -------
def ImprimeMaiores(Vet,tamanho, elemento):
    print("Os valores maiores que", elemento, "são:")
    
    k = 0
    for i in range(N):
        if Vet[i] > elemento:
            k = k+1
            print(Vet[i])
    print("A quantidade de elementos maiores que",ultimo,"são:",k)
        
    # complete esta função conforme enunciado

    
#------------ PRINCIPAL
#N = int(input("Quantos elementos deve ter o vetor? "))

N = int(input(""))
if (N<=0):
    print("Nada a processar!")
else:
    Vet = LerVetor([], N)
    ultimo = Vet[N-1]
    ImprimeMaiores(Vet, N, ultimo)
    