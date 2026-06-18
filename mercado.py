print("Mercado Sintra")

produtos = ["", "1 - HD", "2 - Monitor", "3 - Teclado", "4 - Iphone 17"]

valores = [0, 500.0, 5000.0, 250.0, 14000.0]

print(f"""
{produtos[1]} = R${valores[1]}
{produtos[2]} = R${valores[2]}
{produtos[3]} = R${valores[3]}
{produtos[4]} = R${valores[4]}
""")

carrinho = []
total = []

produto1 = int(input("Produto: "))
produto2 = int(input("Produto: "))
produto3 = int(input("Produto: "))

carrinho.extend([produtos[produto1],produtos[produto2],produtos[produto3]])
total.extend([valores[produto1],valores[produto2],valores[produto3]])

print('**' *20)
print("R$", sum(total))
print("Produtos: ", carrinho)
print('**' *20)
print("Obrigado, volte sempre!")