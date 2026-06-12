print("-Calculadora-\nSelecione uma operação:\n \n1. Adição \n2. Subtração \n3. Multiplicação\n4. Divisão")
op = int(input(">>"))

print("Digite o primeiro número:")
num1 = int(input(">>"))
print("Digite o segundo número:")
num2 = int(input(">>"))

resultado = (op == 1 and (num1 + num2)) or (op == 2 and (num1 - num2)) or (op == 3 and (num1 * num2)) or (num1 / num2)

print("Resultado:")
print(resultado)
