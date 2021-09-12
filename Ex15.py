# Escreva um programa para calcular f(x) = 2x3 + cos(x) + 10, para “n” termos a partir de um valor inicial de “x”. Para os n-1 termos seguintes, deve-se incrementar 0.5 a partir do valor inicial de x.
# Exemplo:  Se o usuário informar que quer calcular f(x) para n=4 (3 termos) a partir de x=0, o seu programa deve calcular f(x), para x=0, x=0.5, x=1.0 e x=1.5
# Observações: 
# É obrigatório o uso da função “pow” para calcular 2x3. 
# Faça isso para treinar o uso de bibliotecas do Python 


import math 

n=float(input(" "))
n2=n
xinicial = float(input(""))

def funcao(x):
    return round((2*(pow(x,3)) + math.cos(x)+10),1)
    
while (n2>0):
    print("f("+ str(xinicial)+")=" + str(funcao(xinicial)))
    n2= n2 - 1
    xinicial = xinicial+0.5