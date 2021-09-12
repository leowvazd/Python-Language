# Nesta atividade o objetivo � que voc� treine a chamada de fun��es de usu�rio. 

# Em suma o programa deve:
# ler 3 n�meros (x1, x2 e x3)
# Obrigar que cada um dos 3 n�meros esteja dentro de um determinado intervalo. Vide detalhamento (limites) mais adiante.
# Exibir a soma dos 3 n�meros

# Note que:
# Parte do programa principal � disponibilizado a seguir
# A fun��o FVerificaLimites tamb�m � disponibilizada. 

# O trecho de programa principal disponibilizado:
# l� um n�mero (x1) obrigando que esteja entre entre 0 e 10
# A fun��o FVerificaLimites faz esta verifica��o (entre 0 e 10

# Voc� deve completar o programa principal que deve:
# Ler x2 e chamar a fun��o FVerificaLimites utilizando como limite inferior o valor de x1 e como limite superior o valor 50
# Ler x3 e chamar a fun��o FVerificaLimites utilizando como limite inferior o valor de x1 e como limite superior o valor x2
# Imprimir a soma dos 3 n�meros lidos pelo programa. 

def FVerificaLimites (valor, inferior, superior):
    if (valor < inferior or valor > superior):
	    print("[Erro - digitou: %d]. Digite um n�mero entre %d e %d:" % (valor, inferior, superior))
	    erro="S"
    else:
        erro="N"
    return erro
# ---- PROGRAMA PRINCIPAL ---------------------
valida='S'
while (valida=='S'):
    x1=int(input(""))
    valida=FVerificaLimites(x1, 0, 10)  # chama a fun��o que verifica os limites
#-----------	
# --- digite sua solu��o abaixo - tecle enter para criar novas linhas ---


valida='S'   
while (valida=='S'):
  x2=int(input(""))
  valida=FVerificaLimites(x2, x1 , 50)
    
valida='S'
while (valida=='S'):
  x3=int(input(""))
  valida=FVerificaLimites(x3, x1 , x2)

soma = x1+x2+x3
print(f'{x1} + {x2} + {x3} = {soma}')