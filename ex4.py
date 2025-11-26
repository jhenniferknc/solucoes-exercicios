nome = input("Nome do vendedor: ")
salarioFixo = float(input("Salário fixo: "))
totalVendas = float(input("Total de vendas: "))

salarioComComissao = salarioFixo + (totalVendas * 0.15)

print('TOTAL = R$ {:.2f}'.format(salarioComComissao))