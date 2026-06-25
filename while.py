# 1

num = 0

while num <= 1000:
    print(num, end = ", ")
    num = num + 1
print("\n")

# 2

nomes = [""]

nomu = 1

while nomu <= 10:
    nomi = input(f"Nome nº{nomu}: ")
    nomu = nomu + 1
    nomes.append(nomi)

print(nomes[1:])