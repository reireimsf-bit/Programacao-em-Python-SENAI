# 1

user_num = float(input("Digite um número: "))

if user_num > 0:
    print("\nO número digitado é positivo!\n")
elif user_num == 0:
    print("\nO número digitado é zero!\n")
else:
    print("\nO número digitado é negativo!\n")

# 2

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("\nO seu voto é obrigatório.\n")
elif idade >= 16 and idade < 18:
    print("\nO seu voto é facultativo.\n")
else:
    print("\nVocê não tem idade para votar!\n")

# 3

par_ou = int(input("Digite outro número: "))

if par_ou % 2 == 0:
    print("\nO número digitado é par.\n")
else:
    print("\nO número digitado é impar.\n")

# 4

lado1 = int(input("Triângulo:\nmedida do lado 1: "))
lado2 = int(input("medida do lado 2: "))
lado3 = int(input("medida do lado 3: "))

if lado1 == lado2 == lado3:
    print("\nO triângulo é equilátero.\n")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("\nO triângulo é isósceles.\n")
else:
    print("\nO triângulo é escaleno.\n")

# 5

mult = int(input("Digite um número: "))

if mult % 5 == 0 and mult % 7 == 0:
    print("\nO número é múltiplo de 5 e 7!\n")
elif mult % 5 == 0 and mult % 7 != 0:
    print("\nO número é múltiplo de 5, mas não de 7!\n")
elif mult % 5 != 0 and mult % 7 == 0:
    print("\nO número é múltiplo de 7, mas não de 5!\n")
else:
    print("\nO número não é múltiplo de 5, e nem de 7!\n")

# 6

user_num2 = float(input("Digite mais um número: "))

if user_num2 < 0:
    print("\nO número digitado é negativo e menor que 10!\n")
elif user_num2 > 0 and user_num2 < 10:
    print("\nO número digitado é positivo, porém menor que 10!\n")
else:
    print("\nO número digitado é positivo e maior que 10!\n")

# 7

divnum = int(input("Digite um número: "))

if divnum % 3 == 0 and divnum % 5 == 0:
    print("\nO número é divisível por 3 e 5!\n")
elif divnum % 3 == 0 and divnum % 5 != 0:
    print("\nO número é divisível por 3, mas não por 5!\n")
elif divnum % 3 != 0 and divnum % 5 == 0:
    print("\nO número é divisível por 5, mas não por 3!\n")
else:
    print("\nO número não é divisível por 3, e nem por 5!\n")