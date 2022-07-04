6. Campeonato Brasileiro
Faça um código que receba o nome dos times do campeonato brasileiro série A de 2022.
Utilizando For, imprima uma lista com todas as possibilidades de jogos.


import random
print('\033[1;33m='*30)
print('\033[1;32mCAMPEONATO BRASILEIRO'.center(30))
print('\033[1;33m='*30)
print('Quantos times vão participar do Campeonato? ')
quant = int(input('Resposta: '))
time = []
time2 = time

for i in range(quant):
    novo_time = input(f'\033[0;34mDigite o {i+1} Time: ')
    time.append(novo_time)

for i in time:
    for j in time2:
        if i == j:
            continue
        valor1 = random.randint(0, 10)
        valor2 = random.randint(0, 10)
        print(f'\033[1;31m{i}[{valor1}] x [{valor2}]{j}')
        if valor1 == valor2:
            print('\033[0;30mEMPATE')
            print('\033[0;33m=' * 30)
        if valor1 > valor2:
            print(f'\033[0;32m{i} TIME VENCEDOR ')
            print('\033[0;33m=' * 30)
        if valor2 > valor1:
            print(f'\033[0;36m{j} TIME VENCEDOR')
            print('\033[0;33m=' * 30)























