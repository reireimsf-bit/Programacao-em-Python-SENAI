# 1
try:
    num1 = int(input("Digite um número inteiro: "))
    print(f"{num1} é um número inteiro.\n")
except ValueError:
    print("Digite apenas números inteiros!\n")

# 2

try:
    num2 = float(input("Digite o dividendo: "))
    num3 = float(input("Digite o divisor: "))
    div = num2 / num3
    print(div)
except ZeroDivisionError:
    print("Erro: Divisor não pode ser zero.")

# 3

lista = ["mamão","laranja","banana","limão"]
num4 = input("Escolha: mamão, laranja, banana ou limão? ")

try:
    print(f"Index do item: {lista.index(num4)}")
except ValueError:
    print("Item não consta na lista!")
