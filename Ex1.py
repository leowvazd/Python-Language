# Escreva um algoritmo para mostrar a m�dia final de um aluno a partir de 4 notas. 
# Considere que as notas podem ter casas decimais.
# Para o c�lculo da m�dia final, deve-se utilizar m�dia ponderada, aplicando-se a seguinte f�rmula:

#               M = ( ( p1 x 30) + (p2 x 40) + (t1 x 10) + (t2 x 20) ) / 100


P1 = float(input('nota da primeira prova:'))
P2 = float(input('nota da segunda prova:'))
T1 = float(input('nota do primeiro trabalho:'))
T2 = float(input('nota do segundo trabalho:'))
M = ((P1*30)+(P2*40)+(T1*10)+(T2*20))/100
print('A m�dia �:',M)
