
valorHoras = float(input('Digite o valor que vc ganha por horas: '))
numeroHoras = float(input('Digite o numero de horas trabalhadas: '))

salarioBruto = valorHoras * numeroHoras

descontoImpostoDeRenda =  salarioBruto * 0.15

valorInss = salarioBruto * 0.10

valorSindicado = salarioBruto * 0.02

salarioLiquido = (((salarioBruto - descontoImpostoDeRenda) - valorInss) - valorSindicado)

print(f'O salario Bruto {salarioBruto}')
print(f'A quantia paga ao INSS {valorInss}')
print(f'A quantia ao sindicato {valorSindicado}')
print(f'O salario liquido {salarioLiquido}')
