print("Bem vindos ao Hotel Estrela!")

nomes = [""]
idade = [""]
quarto = ["", "Simples", "Duplo", "Luxo"]
precos = ["", 100.00, 150.00, 200.00]


print("Cliente #1:")
cl1_name = input("Nome: ")
cl1_age = int(input("Idade: "))
nomes.append(cl1_name)
idade.append(cl1_age)
cl1_room = int(input("Selecione um quarto:\n1 - Simples\n2 - Duplo\n3 - Luxo\n>>"))
cl1_days = int(input("Número de dias:" ))


print("Cliente #2:")
cl2_name = input("Nome: ")
cl2_age = int(input("Idade: "))
nomes.append(cl2_name)
idade.append(cl2_age)
cl2_room = int(input("Selecione um quarto:\n1 - Simples\n2 - Duplo\n3 - Luxo\n>>"))
cl2_days = int(input("Número de dias:" ))

print("Cliente #3:")
cl3_name = input("Nome: ")
cl3_age = int(input("Idade: "))
nomes.append(cl3_name)
idade.append(cl3_age)
cl3_room = int(input("Selecione um quarto:\n1 - Simples\n2 - Duplo\n3 - Luxo\n>>"))
cl3_days = int(input("Número de dias:" ))

print(f"\n{nomes[1]} se hospedou em um quarto do tipo {quarto[cl1_room]}, por {cl1_days} {"dia" if cl1_days == 1 else "dias"}, com o valor total da diária de R${cl1_days * precos[cl1_room]}.")
print(f"\n{nomes[2]} se hospedou em um quarto do tipo {quarto[cl2_room]}, por {cl2_days} {"dia" if cl2_days == 1 else "dias"}, com o valor total da diária de R${cl2_days * precos[cl2_room]}.")
print(f"\n{nomes[3]} se hospedou em um quarto do tipo {quarto[cl3_room]}, por {cl3_days} {"dia" if cl3_days == 1 else "dias"}, com o valor total da diária de R${cl3_days * precos[cl3_room]}.")