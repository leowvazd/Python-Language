# Escreva um algoritmo que solicite ao usu�rio o valor de N e em seguida a idade de N pessoas (N idades maiores que zero). O programa dever� exibir, ao final,  �a menor idade� informada.  

# Observa��es:
# Caso �N� seja zero o programa deve mostrar a mensagem: �"Nada a processar!"
# � obrigat�rio fazer a valida��o de dados da idade, ou seja, deve-se obrigar o usu�rio a digitar uma idade maior que ZERO). 
# Quando for lida uma idade <=0 deve se emitir a seguinte sa�da: 
# �Erro: Redigite a idade!�
# � obrigat�rio o uso de estruturas de repeti��o
# N�o � permitido o uso de N vari�veis de entrada de dados, ou seja, ler cada uma das �N  idades� em vari�veis distintas (n1, n2, n3, ... n10).

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
       
