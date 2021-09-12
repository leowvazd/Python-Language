# Escreva um algoritmo que solicite ao usuário o valor de N e uma sequência de N números inteiros positivos. O programa deve exibir ao final:
# A quantidade de valores nulos
# A quantidade de números divisíveis por 3
# A quantidade de números não divisíveis por 3
# Observações:
# Não é necessário fazer a validação de dados (obrigar a digitar um número positivo)
# Um número negativo também pode ser computado como múltiplo de outro.
# O número zero (nulo) não deve ser computado como divisível ou não divisível por 3.
# É obrigatório o uso de estruturas de repetição

# Entrada:   N: 5    Valores : 11, 15, 23, 45, 13
# Saída Esperada: 
# Nulos = 0
# Divisíveis por 3 = 2
# Não divisíveis por 3 = 3

# CASO DE TESTE 2:
# Entrada:  N: 9    Valores : 22, 14, -2, 12, 0, 33, 76, 5, 99 
# Saída Esperada: 
# Nulos = 1
# Divisíveis por 3 = 3
# Não divisíveis por 3 = 5

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
print('Divisíveis por 3 =', divisivel)
print('Não divisíveis por 3 =', ndivisivel)