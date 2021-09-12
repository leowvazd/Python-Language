# Escreva um algoritmo que solicite ao usuário o valor de N e em seguida a idade de N pessoas (N idades maiores que zero). O programa deverá exibir, ao final,  “a menor idade” informada.  

# Observações:
# Caso “N” seja zero o programa deve mostrar a mensagem: “"Nada a processar!"
# É obrigatório fazer a validação de dados da idade, ou seja, deve-se obrigar o usuário a digitar uma idade maior que ZERO). 
# Quando for lida uma idade <=0 deve se emitir a seguinte saída: 
# “Erro: Redigite a idade!”
# É obrigatório o uso de estruturas de repetição
# Não é permitido o uso de N variáveis de entrada de dados, ou seja, ler cada uma das “N  idades” em variáveis distintas (n1, n2, n3, ... n10).

num = int(input()) 
x = 1
a = 9999

if num > 0:
    for x in range(num):
        valor = int(input())
        if valor <= 0:
            print('Erro: Redigite a idade!')
        if valor < a and valor >=0:
            a = valor
        valor = 1
                
    print('Menor idade =',a)    

else: 
    print('Nada a processar!')
       
