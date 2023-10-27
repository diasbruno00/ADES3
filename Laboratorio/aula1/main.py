
lista = [12, 13, 14, 31]

for numero in lista:
    if numero >= 10 and numero <= 30:
        print(numero)
        
altura = float( input("digite algo: "))

if altura >= 1.85:
    print("alto")
elif altura < 1.85 and altura >= 1.6:
    print("medio")
else:
    print("Baixo")
    if(altura < 1.4):
        print("anão ou criança")




