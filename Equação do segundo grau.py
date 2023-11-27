a = float(input("Insira o valor de a: "))
if a == 0:
    print("Esta equação não é do segundo grau")

else:
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))

delta = (b ** 2) - (4 * a * c) 

if delta < 0:
    print(" A equação não possui raizes reais")

elif delta == 0:
    print("A equação possui apenas uma raiz: ", (-b) + (delta ** 0.5) / (2*a))

else:
    print("Raiz 1: ",(-b) + (delta ** 0.5) / (2*a), "\n" "Raiz 2: ",(-b) - (delta ** 0.5) / (2*a))