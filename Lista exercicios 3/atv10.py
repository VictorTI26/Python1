salario_fixo = float(input("Digite o salário fixo do vendedor: "))
valor_vendas = float(input("Digite o valor das vendas efetuadas pelo vendedor: "))

if valor_vendas <= 1500:
    comissao = valor_vendas * 0.03
else:
    comissao = 1500 * 0.03 + (valor_vendas - 1500) * 0.05

salario_total = salario_fixo + comissao

print("O salário total do vendedor é:", salario_total)
