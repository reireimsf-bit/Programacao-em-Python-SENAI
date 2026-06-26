
# 1
def par_ou (num1,num2):
    num1_check = num1 % 2
    num2_check = num2 % 2
    if num1_check == 0 and num2_check == 1:
        print(f"{num1} é um número par, porém {num2} é impar.\n")
    elif num1_check == 1 and num2_check == 0:
        print(f"{num1} é um número impar, porém {num2} é par.\n")
    elif num1_check == 0 and num2_check == 0:
        print(f"Tanto {num1} quanto {num2} são pares.\n")
    else:
        print(f"Tanto {num1} quanto {num2} são impares.\n")


par_ou(2, 4)
par_ou(1, 3)
par_ou(2, 1)
par_ou(1, 2)

# 2
def mult3 (num1,num2,num3):
    multt = num1 * num2 * num3
    return multt

print(mult3(2,3,2), "\n")

# 3
def elev (num):
    return num**2

print(elev(10), "\n")

# 4
def bebidacheck(idd):
    if idd >= 18:
        print("Já pode beber!\n")
    else:
        print("Não pode beber. Muito jovem!\n")

bebidacheck(int(input("Quantos anos você tem? ")))

# 5
def idadecheck(ano_a):
    ano_b = 2026 - ano_a
    print(f"Você tem {ano_b} anos de idade!\n")

idadecheck(int(input("Em qual ano você nasceu? ")))

# 6
def copa99(winner):
    if winner == "Brasil":
        print("Correto! Brasil ganhou a Copa América em 1999!\n")
    else:
        print("Errado! Tente novamente.\n")

copa99(input("Quem ganhou a Copa de 1999? "))

# 7

def oi(nome):
    print(f"Olá, {nome}!\n")

def lanche():
    nomee = input("Digite o seu nome: ")
    oi(nomee)

    menu = ["", "Salada", "Macarronada", "Sanduiche", "Sorvete", "Refri"]
    preco = ["", 20.99, 35.00, 25.50, 15.99, 5.00]
    total = [0.00]
    carrinho = []
    esc = 0

    while esc != "Finalizar":
        print(f"""O que gostaria de pedir?
            
                {menu[1]} - R${preco[1]}
                {menu[2]} - R${preco[2]}
                {menu[3]} - R${preco[3]}
                {menu[4]} - R${preco[4]}
                {menu[5]} - R${preco[5]}
                Finalizar - Total R${sum(total):.2f}\n""")
        esc = input("Digite uma opção: ")
        if esc in menu:
            carrinho.append(esc)
            total.append(preco[menu.index(esc)])
        elif esc == "Finalizar":
            pass
        else:
            print("Digite um item do menu!")
    
    print(f"Carrinho: {carrinho}")
    print("**" * 10)
    print(f"Total da compra: R${sum(total):.2f}")
    print("**" * 10)
    input("Selecione um método de pagamento:\n1 - PIX\n2 - CC\n3 - CD\n \n>>")
    print("Obrigado pela compra, volte sempre!\n \n \n")

def loop():
    while True:
        lanche()

loop()