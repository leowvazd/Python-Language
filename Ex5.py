# Realizou-se uma pesquisa com N pessoas que responderam à seguinte pergunta:    
# Quantos filhos você tem? 
# Escreva um algoritmo para processar essa pesquisa informando quantas, das N pessoas possuem até 2 filhos e quantas possuem mais de 2 filhos. Informar também a média de filhos das “N” pessoas. O valor de N deverá ser informado pelo usuário. 

# Entrada:   N: 6    Número de filhos: 0, 1, 5, 3, 1, 2
# Saída Esperada: 
# Quantidade de pessoas até 2 filhos = 4
# Quantidade de pessoas com mais de 2 filhos = 2
# Média de filhos por pessoa = 2.0

n = int(input(""))
media = 0
k = 0
j = 0
i = 0

for i in range(n):
    a = int(input(""))

    if a <= 2:
        k = k + 1
        media = a + media

    if a > 2:
        j = j + 1
        media = a + media
    i = i + 1

media = media / n

print('Quantidade de pessoas até 2 filhos =',k)
print('Quantidade de pessoas com mais de 2 filhos =',j)
print('Média de filhos por pessoa =',media)