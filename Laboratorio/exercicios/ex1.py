
salario = float(input('Informe seu salario: '))
imposto = 0.0
deducao = 0.0

if salario <= 1903.98:
    print('Inseneto')
elif salario >= 1903.99 and salario <= 2826.65:
    imposto = 7.5
    deducao = 142.80
elif salario >= 2826.66 and salario <= 3751.05:
    imposto = 0.15
    deducao = 354.80
elif salario >= 3751.06 and salario <= 4664.68:
    imposto = 0.22
    deducao = 636.13
elif salario >= 4664.698:
    imposto = 0.27
    deducao = 869.36


novoSalario = (salario * imposto) - deducao

print(f'O salario atualizado do funcionario: {novoSalario}')


