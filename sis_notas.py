print("Sistema de notas\n")

notas = []
esc = 0

for t in range(3):
    s_log = input("Login: ")
    s_sen = input("Senha: ")
    if s_log == "prof" and s_sen == "12345":
        print("Seja Bem vindo\n")
        while esc < 3:
            print("1 - Adicionar nota\n2 - Somar a média de todas as notas\n3 - Sair do sistema")
            esc = int(input(">>"))
            if esc == 1:
                nt = int(input("Adicione uma nota: "))
                notas.append(nt)
                print(f"Sucesso!\nNotas registradas: {notas}\n")
                esc = 0
            elif esc == 2:
                print(f"\nNotas registradas: {notas}\nMédia da turma:")
                print(sum(notas) / len(notas) , "\n")
                esc = 0
            elif esc == 3:
                print("\nLogoff...\n")
                esc = 0
                break

    else:
        print("Login ou senha errados!\n")

else:
    input("Erro: Acesso negado")