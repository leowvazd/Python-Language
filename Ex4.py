# Escreva um programa que peça como entrada o peso (em quilogramas) e a altura (em metros) da pessoa e calcule o seu IMC – Índice de Massa Corpórea. 

# O IMC é calculado da seguinte forma: divide-se o peso (quilogramas) pela altura ao quadrado (em metros).

# Exemplo1: peso = 65, altura = 1.67  IMC = 65 / (1.67 * 1.67) = 23.30
# Exemplo2: peso = 85, altura = 1.60  IMC = 85 / (1.60 * 1.60) = 33.20

peso = int(input("peso:"))
altura = float(input("altura:"))
IMC = peso / (altura**2)

#print("{:.2f}".format(IMC))  ## sua resposta
print("IMC =", IMC) ## corrigido pelo professor
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("No peso ideal")
elif IMC > 24.9 and IMC <= 29.9:
    print("Acima do peso ideal")
elif IMC > 29.9 and IMC <= 34.9:
    print("Obesidade grau I")
elif IMC > 34.9 and IMC <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
