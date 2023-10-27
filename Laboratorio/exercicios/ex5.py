class Bomba:

    def __init__(self,combustivel, valor, quantidade ) -> None:
        self.combustivel = combustivel
        self.valorLitro = valor
        self.quantidade  = quantidade

    def abastecer_valor(self, valor):
        self.quantidade = valor / self.valorLitro
        print(f'A quantidade de litros no carro {self.quantidade}')

    def abastecer_qtd (self, qtde):
        self.quantidade =  self.valorLitro / qtde
        print(f'A quantidade abastecido {self.quantidade}')


c1 = Bomba('sla',2, 0)
c1.abastecer_valor(10)
c1.abastecer_qtd(10)
