import random as r
import time as t

def cinco_a_dez():
    nums = r.randint(5,10)
    return nums

def tres_num():
    nums1 = r.randint(1,100)
    nums2 = r.randint(1,100)
    nums3 = r.randint(1,100)
    return nums1, nums2, nums3

def dez_a_trinta():
    nums = r.randint(10,30)
    return nums

def atirar():
    for x in range(10,0,-1):
        print(x)
        t.sleep(0.3)
    print("Fogo!")

def soma_pares(fim):
    nums2 = [nums for nums in range(2,fim,2)]
    return sum(nums2)

def tabuada(num):
    for nums in range(1,11):
        print(f"{num} * {nums} = {num*nums}")

def impar_a_zero():
    for x in range(99,0,-2):
        print(x)
        t.sleep(0.1)

