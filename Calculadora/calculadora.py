def calcula(n1, n2, operador):
    if operador == "+":
        return n1 + n2
    if operador == "-":
        return n1 - n2
    if operador == "*":
        return n1 * n2
    if operador == "/":
        if n2 == 0:
            print("divisão por zero")
            exit()
        return n1 / n2
    print(f"Operador inválido: {operador}")
    exit()


#BP
n1 = float(input("1o num: "))
n2 = float(input("2o num: "))
operador = input("operador: ")
resultado = calcula(n1, n2, operador)
print(resultado)