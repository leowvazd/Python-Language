# Um número inteiro x é perfeito se a soma de seus fatores (divisores), exceto ele mesmo, é igual a x.  Por exemplo, 6 é perfeito visto que 1 + 2 + 3 = 6.  Escreva um programa para informar se x é um número perfeito. Deve-se também mostrar os divisores (independente de ser ou não um número perfeito).

# CASO DE TESTE 1:
# Entrada:   N: 6    
# Saída Esperada: 
# 1
# 2
# 3
# 6 é um número perfeito!

n = int(input())
soma = 0

for i in range(1,n):
    if n % i == 0:
        print(i)
        soma = soma + i 
        

if soma == n:
    print(n,' é um número perfeito!')

if soma != n:
    print(n,' não é um número perfeito!')