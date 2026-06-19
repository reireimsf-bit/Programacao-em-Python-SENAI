#dicionario

estoque = {

"livros" : {"livro1" : 30.50,
            "livro2" : 35.00,
            "livro3" : 50.90},

"tablets" : {"t1" : 2000.00,
             "t2" : 3000.00,
             "t3" : 4000.00},

"fones" : {"fone1" : 45.50,
           "fone2" : 50.25,
           "fone3" : 100.75},
}

carrinho = []
total = []

sec = input(f"Seção:{estoque.keys()}: ")
print("Você acessou a seção: ", estoque[sec])

prod = input(f"Escolha produto: {estoque[sec]}")
print("Adicionar ao carrinho: ", estoque[sec][prod])

carrinho.append(prod)
total.append(estoque[sec][prod])

#---------------------------------

sec = input(f"Seção:{estoque.keys()}: ")
print("Você acessou a seção: ", estoque[sec])

prod = input(f"Escolha produto: {estoque[sec]}")
print("Adicionar ao carrinho: ", estoque[sec][prod])

carrinho.append(prod)
total.append(estoque[sec][prod])

#---------------------------------

sec = input(f"Seção:{estoque.keys()}: ")
print("Você acessou a seção: ", estoque[sec])

prod = input(f"Escolha produto: {estoque[sec]}")
print("Adicionar ao carrinho: ", estoque[sec][prod])

carrinho.append(prod)
total.append(estoque[sec][prod])

#---------------------------------

soma = sum(total)
print("Total: R$", soma)
formpag = ["", "1 - PIX", "2 - CC", "3 - CD"]
pag = int(input(f"Selecione uma forma de pagamento: \n{formpag[1]} \n{formpag[2]} \n{formpag[3]}\n>>"))
print("\nObrigado e volte sempre!")

input("\nAperte enter para sair...")