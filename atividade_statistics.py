import modulo as m

notas = []

def sis_escola():
    print("Bem vindo ao sistema de notas.\n \n1. Adicionar notas\n2. Consultar notas\n3. Consultar a média\n4. Consultar a moda\n5. Desvio de padrão\n6. Menor e maior notas")
    sel = int(input("\n>>"))
    if sel == 1:
        adnot = float(input("Registre uma nota: "))
        if adnot > 10 or adnot < 0:
            input("Valor inválido! Apenas notas de 0 a 10 permitidas.\n")
        else:
            notas.append(adnot)
            input("Nota registrada com sucesso.\n")
    elif sel == 2:
        input(f"Notas registradas no sistema:\n{notas}\n")
    elif sel == 3:
        try:
            input(f"A média entre todas as notas registradas é: {m.media0(notas):.1f}\n")
        except:
            input("Não existem notas registradas.\n")
    elif sel == 4:
        try:
            input(f"A moda entre as notas da turma é: {m.moda0(notas):.1f}\n")
        except:
            input("Não existem notas registradas.\n")
    elif sel == 5:
        try:
            input(f"O desvio padrão da turma é: {m.moda0(notas):.1f}\n")
        except:
            input("Não existem notas registradas.\n")
    elif sel == 6:
        try:
            input(f"A maior nota da turma é: {m.maior0(notas):.1f}\nA menor nota da turma é: {m.menor0(notas):.1f}\n")
        except:
            input("Não existem notas registradas.\n")
    else:
        input("Selecione uma ação válida!\n")

while True:
    sis_escola()