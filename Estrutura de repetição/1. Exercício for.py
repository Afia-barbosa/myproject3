#questão1.

# 1. Faça um programa, utilizando for, que permita o usuário fazer três contas de subtração.

print("questão 1")
print("="*30)

for i in range(1,4):
    print(f"conta {i}")
    num1 = int(input("Digite o número: "))
    num2 = int(input("Digite o número: "))
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")




