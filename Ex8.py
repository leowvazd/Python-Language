# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
# a) média do salário da população;
# b) média do número de filhos da população;
# c) percentual de pessoas com salário <= R$1000,00 (até 1000 reais, inclusive 1000 reais)
# Observações:
# Não se sabe previamente o número de entrevistados. Assim, a entrada de dados deve ser encerrada quando for digitado um salário não positivo, ou seja, um salário menor ou igual a zero.
# É obrigatório fazer a validação de dados do “número de filhos”, ou seja, deve-se obrigar o usuário a digitar número de filhos >=0.  
# Caso o “número de filhos seja inválido” não se deve solicitar o salário de novo. Somente o número de filhos válido.
# Quando for lido “número de filhos <0” deve se emitir a seguinte saída: 
# “Erro: Redigite o número de filhos!”
# É obrigatório o uso de estruturas de repetição

# Entrada: 
# salário = 4500; número de filhos = 0
# salário = 3500; número de filhos = 0
# salário = 4200; número de filhos = 0
# salário = 3600; número de filhos = 1
# salário = -1
# Saída Esperada: 
# Média Salário = 3950.0
# Média Número de Filhos = 0.25
# Percentual Pessoas com salário até 1000 reais = 0.0 %

salario = int(input(""))

totalSalario = 0
totalPessoas = 0
totalFilhos = 0
pessoasSalarioAbaixoMil = 0

if salario <= 0:
    print("Média Salário = 0.0")
    print("Média Número de Filhos = 0.0")
    print("Percentual Pessoas com salário até 1000 reais = 0.0 %")
    
else:
    while salario > 0:
        totalPessoas += 1
        filhos = int(input(""))
        while filhos < 0:
            print("Erro: Redigite o número de filhos!")
            filhos = int(input(""))
        totalSalario += salario
        totalFilhos += filhos
        if salario <= 1000:
            pessoasSalarioAbaixoMil += 1
        salario = int(input(""))

    mediaSalarial = totalSalario / totalPessoas
    mediaFilhos = totalFilhos / totalPessoas
    percentualPessoasSalarioAbaixoMil = (100/totalPessoas) * pessoasSalarioAbaixoMil
    
    print("Média Salário =",mediaSalarial)
    print("Média Número de Filhos =",mediaFilhos)
    print("Percentual Pessoas com salário até 1000 reais =", percentualPessoasSalarioAbaixoMil,"%")