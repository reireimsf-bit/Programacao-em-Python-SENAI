# 3
n = input(">>")

match n:
    case "":
        print("String está em branco!")
    case _:
        print(f"String é {n}")

# 5
idade = int(input(">>"))

match idade:
    case idade if idade <= 12:
        print("Criança")
    case idade if idade <= 17:
        print("Adolescente")
    case idade if idade <= 35:
        print("Jovem")
    case idade if idade <= 64:
        print("Adulto")
    case _:
        print("Idoso")