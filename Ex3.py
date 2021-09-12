# Escreva um programa que solicite ao usu�rio os n�meros de votos v�lidos obtidos pelos partidos A, B e C, e o n�mero de vagas na C�mara ou Assembleia. O programa deve informar o quociente eleitoral e uma das duas seguintes mensagens:
# H� partido com quociente partid�rio igual a zero!
# Nenhum partido obteve quociente partid�rio igual a zero!

# Sabe-se que:
# o quociente eleitoral � a divis�o do n�mero total de votos v�lidos pelo n�mero de vagas (desprezando-se as casas decimais)
# o quociente partid�rio � a divis�o do n�mero total de votos no partido pelo quociente eleitoral (desprezando-se as casas decimais)

a = int(input("Indique a quantidade de votos obtidos pelo partidos A: "))
b = int(input("Indique a quantidade de votos obtidos pelo partidos B: "))
c = int(input("Indique a quantidade de votos obtidos pelo partidos C: "))

vagas_cam = int(input("Indique a quantidade de vagas dispon�veis na c�mera: "))
quociente_eleitoral = (a + b + c) // vagas_cam

# print('Quociente eleitoral:', quociente_eleitoral) # sua resposta
print('Quociente eleitoral =', quociente_eleitoral)  # corrigido pelo Professor
quociente_partidario_a = a // quociente_eleitoral
quociente_partidario_b = b // quociente_eleitoral
quociente_partidario_c = c // quociente_eleitoral

if quociente_partidario_a != 0 and quociente_partidario_b != 0 and quociente_partidario_c != 0:
    #print("Nenhum partido obteve quociente partid�rio igual a 0.") # sua resposta
    print("Nenhum partido obteve quociente partid�rio igual a zero!") # corrido pelo professor
else:
    #print("H� partido com quociente partid�rio igual a 0.") # sua resposta
    print("H� partido com quociente partid�rio igual a zero!") # corrido pelo professor
