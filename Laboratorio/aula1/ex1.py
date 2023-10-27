
lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("Equilatero")

elif lado1 == lado2 or lado1 == lado3:
    print("isosceles")

elif lado1 != lado2 and lado1 != lado3:
    print("escaleno")
