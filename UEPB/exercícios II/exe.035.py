'''
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
'''
print("Equação do 2º grau: ax² + bx + c = 0")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta == 0:
    raiz = -b / (2 * a)
    print(f"A equação possui apenas uma raiz real: {raiz}")
else:
    print("O delta não é zero. A equação não possui apenas uma raiz real.")
