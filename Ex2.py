# Sabe-se que um quilowatt de energia custa 1/500 avos do sal�rio m�nimo.  Fa�a um algoritmo que receba o valor do sal�rio m�nimo e quantidade de quilowatts consumida por uma resid�ncia. 
# Calcule e mostre:
# - O valor, em reais, de cada quilowatt;
# - O valor, em reais, da conta ser paga por essa resid�ncia;
# - O valor, em reais, a ser pago com desconto de 15%.

SM = float(input('Digite o salario minimo:'))
Quilo = float(input('Digite a quantidade de quilowatts:'))
VQ = SM / 500
VT = VQ * Quilo
Desconto = VT - (VT * 0.15)
print('O valor de {}'.format(VQ))
print('O valor de {}'.format(VT))
print('O valor de {}'.format(Desconto))