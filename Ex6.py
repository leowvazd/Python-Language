# Um n�mero inteiro x � perfeito se a soma de seus fatores (divisores), exceto ele mesmo, � igual a x.  Por exemplo, 6 � perfeito visto que 1 + 2 + 3 = 6.  Escreva um programa para informar se x � um n�mero perfeito. Deve-se tamb�m mostrar os divisores (independente de ser ou n�o um n�mero perfeito).

# CASO DE TESTE 1:
# Entrada:   N: 6    
# Sa�da Esperada: 
# 1
# 2
# 3
# 6 � um n�mero perfeito!

n = int(input())
soma = 0

for i in range(1,n):
    if n % i == 0:
        print(i)
        soma = soma + i 
        

if soma == n:
    print(n,' � um n�mero perfeito!')

if soma != n:
    print(n,' n�o � um n�mero perfeito!')