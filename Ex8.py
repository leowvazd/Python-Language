# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o sal�rio e n�mero de filhos. A prefeitura deseja saber:
# a) m�dia do sal�rio da popula��o;
# b) m�dia do n�mero de filhos da popula��o;
# c) percentual de pessoas com sal�rio <= R$1000,00 (at� 1000 reais, inclusive 1000 reais)
# Observa��es:
# N�o se sabe previamente o n�mero de entrevistados. Assim, a entrada de dados deve ser encerrada quando for digitado um sal�rio n�o positivo, ou seja, um sal�rio menor ou igual a zero.
# � obrigat�rio fazer a valida��o de dados do �n�mero de filhos�, ou seja, deve-se obrigar o usu�rio a digitar n�mero de filhos >=0.  
# Caso o �n�mero de filhos seja inv�lido� n�o se deve solicitar o sal�rio de novo. Somente o n�mero de filhos v�lido.
# Quando for lido �n�mero de filhos <0� deve se emitir a seguinte sa�da: 
# �Erro: Redigite o n�mero de filhos!�
# � obrigat�rio o uso de estruturas de repeti��o

# Entrada: 
# sal�rio = 4500; n�mero de filhos = 0
# sal�rio = 3500; n�mero de filhos = 0
# sal�rio = 4200; n�mero de filhos = 0
# sal�rio = 3600; n�mero de filhos = 1
# sal�rio = -1
# Sa�da Esperada: 
# M�dia Sal�rio = 3950.0
# M�dia N�mero de Filhos = 0.25
# Percentual Pessoas com sal�rio at� 1000 reais = 0.0 %

salario = int(input(""))

totalSalario = 0
totalPessoas = 0
totalFilhos = 0
pessoasSalarioAbaixoMil = 0

if salario <= 0:
    print("M�dia Sal�rio = 0.0")
    print("M�dia N�mero de Filhos = 0.0")
    print("Percentual Pessoas com sal�rio at� 1000 reais = 0.0 %")
    
else:
    while salario > 0:
        totalPessoas += 1
        filhos = int(input(""))
        while filhos < 0:
            print("Erro: Redigite o n�mero de filhos!")
            filhos = int(input(""))
        totalSalario += salario
        totalFilhos += filhos
        if salario <= 1000:
            pessoasSalarioAbaixoMil += 1
        salario = int(input(""))

    mediaSalarial = totalSalario / totalPessoas
    mediaFilhos = totalFilhos / totalPessoas
    percentualPessoasSalarioAbaixoMil = (100/totalPessoas) * pessoasSalarioAbaixoMil
    
    print("M�dia Sal�rio =",mediaSalarial)
    print("M�dia N�mero de Filhos =",mediaFilhos)
    print("Percentual Pessoas com sal�rio at� 1000 reais =", percentualPessoasSalarioAbaixoMil,"%")