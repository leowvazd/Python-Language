# Escreva um algoritmo que solicite ao usu�rio o valor de N e uma sequ�ncia de N n�meros inteiros positivos. O programa deve exibir ao final:
# A quantidade de valores nulos
# A quantidade de n�meros divis�veis por 3
# A quantidade de n�meros n�o divis�veis por 3
# Observa��es:
# N�o � necess�rio fazer a valida��o de dados (obrigar a digitar um n�mero positivo)
# Um n�mero negativo tamb�m pode ser computado como m�ltiplo de outro.
# O n�mero zero (nulo) n�o deve ser computado como divis�vel ou n�o divis�vel por 3.
# � obrigat�rio o uso de estruturas de repeti��o

# Entrada:   N: 5    Valores : 11, 15, 23, 45, 13
# Sa�da Esperada: 
# Nulos = 0
# Divis�veis por 3 = 2
# N�o divis�veis por 3 = 3

# CASO DE TESTE 2:
# Entrada:  N: 9    Valores : 22, 14, -2, 12, 0, 33, 76, 5, 99 
# Sa�da Esperada: 
# Nulos = 1
# Divis�veis por 3 = 3
# N�o divis�veis por 3 = 5

n = int(input(""))
nulo = 0
divisivel = 0
ndivisivel = 0

for i in range(n):
    a = int(input(""))

    if a == 0:
        nulo = nulo + 1

    if a % 3 == 0 and a != 0:
        divisivel = divisivel + 1
        
    if a % 3 != 0:
        ndivisivel = ndivisivel + 1

print('Nulos =', nulo)
print('Divis�veis por 3 =', divisivel)
print('N�o divis�veis por 3 =', ndivisivel)