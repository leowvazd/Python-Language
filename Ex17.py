# Escreva um programa que solicite ao usu�rio o n�mero de elementos (N) a serem armazenados em um vetor. Em seguida, crie um vetor do referido tamanho (N).
# O programa deve solicitar a digita��o de N n�meros, armazenando-os no vetor. Caso o usu�rio informe um valor valor para N, menor ou igual a zero, o programa deve simplesmente mostrar a mensagem �Nada a processar!�. Caso contr�rio o programa deve:
# Informar, dentre os n�meros digitados, quais s�o os n�meros maiores que o �ltimo elemento do vetor. 
# Informar,  quantos dos n�meros digitados, s�o maiores que o �ltimo elemento do vetor.

def LerVetor(Vet,tamanho):
    for ind in range (0,tamanho):
        aux=int(input(""))
        Vet.append(aux)
    return Vet

#Complete a fun��o ImprimeMaiores -------
def ImprimeMaiores(Vet,tamanho, elemento):
    print("Os valores maiores que", elemento, "s�o:")
    
    k = 0
    for i in range(N):
        if Vet[i] > elemento:
            k = k+1
            print(Vet[i])
    print("A quantidade de elementos maiores que",ultimo,"s�o:",k)
        
    # complete esta fun��o conforme enunciado

    
#------------ PRINCIPAL
#N = int(input("Quantos elementos deve ter o vetor? "))

N = int(input(""))
if (N<=0):
    print("Nada a processar!")
else:
    Vet = LerVetor([], N)
    ultimo = Vet[N-1]
    ImprimeMaiores(Vet, N, ultimo)
    