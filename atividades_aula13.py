import modulo_aula13 as m

# 1

input("Aperte enter para receber um número aleatório de 5 até 10:")
print(m.cinco_a_dez(), "\n")

# 2

input("Aperte enter para receber 3 números aleatórios:")
print(m.tres_num(), "\n")

# 3

input("Aperte enter para receber um número aleatório de 10 até 30:")
print(m.dez_a_trinta(), "\n")

# 4

input("Aperte enter para iniciar uma contagem regressiva:")
m.atirar()
print("")

# 5

ab = m.soma_pares(int(input("Digite um número inteiro para ver a soma de todos os números pares até o qual escolheu:")))
print(ab, "\n")

# 6

m.tabuada(int(input("Digite um número inteiro para ver a sua tabuada de dez:")))
print("")

# 7

input("Aperte enter para ver uma contagem regressiva de todos of números ímpares menores que 100:")
m.impar_a_zero()

#----------------------MODULO------------------------
#import random as r
#import time as t

#def cinco_a_dez():
#    nums = r.randint(5,10)
#    return nums

#def tres_num():
#    nums1 = r.randint(1,100)
#    nums2 = r.randint(1,100)
#    nums3 = r.randint(1,100)
#    return nums1, nums2, nums3

#def dez_a_trinta():
#    nums = r.randint(10,30)
#    return nums

#def atirar():
#    for x in range(10,0,-1):
#        print(x)
#        t.sleep(0.3)
#    print("Fogo!")

#def soma_pares(fim):
#    nums2 = [nums for nums in range(2,fim,2)]
#    return sum(nums2)

#def tabuada(num):
#    for nums in range(1,11):
#        print(f"{num} * {nums} = {num*nums}")

#def impar_a_zero():
#    for x in range(99,0,-2):
#        print(x)
#        t.sleep(0.1)