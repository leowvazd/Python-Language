# Escreva um programa que solicite ao usuário os números de votos válidos obtidos pelos partidos A, B e C, e o número de vagas na Câmara ou Assembleia. O programa deve informar o quociente eleitoral e uma das duas seguintes mensagens:
# Há partido com quociente partidário igual a zero!
# Nenhum partido obteve quociente partidário igual a zero!

# Sabe-se que:
# o quociente eleitoral é a divisão do número total de votos válidos pelo número de vagas (desprezando-se as casas decimais)
# o quociente partidário é a divisão do número total de votos no partido pelo quociente eleitoral (desprezando-se as casas decimais)

a = int(input("Indique a quantidade de votos obtidos pelo partidos A: "))
b = int(input("Indique a quantidade de votos obtidos pelo partidos B: "))
c = int(input("Indique a quantidade de votos obtidos pelo partidos C: "))

vagas_cam = int(input("Indique a quantidade de vagas disponíveis na câmera: "))
quociente_eleitoral = (a + b + c) // vagas_cam

# print('Quociente eleitoral:', quociente_eleitoral) # sua resposta
print('Quociente eleitoral =', quociente_eleitoral)  # corrigido pelo Professor
quociente_partidario_a = a // quociente_eleitoral
quociente_partidario_b = b // quociente_eleitoral
quociente_partidario_c = c // quociente_eleitoral

if quociente_partidario_a != 0 and quociente_partidario_b != 0 and quociente_partidario_c != 0:
    #print("Nenhum partido obteve quociente partidário igual a 0.") # sua resposta
    print("Nenhum partido obteve quociente partidário igual a zero!") # corrido pelo professor
else:
    #print("Há partido com quociente partidário igual a 0.") # sua resposta
    print("Há partido com quociente partidário igual a zero!") # corrido pelo professor
