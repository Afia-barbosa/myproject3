#Faça um programa, utilizando for,
# que peça ao usuário um número e mostre a sua tabuada,
# enquanto o usuário quiser.

print('TABUADAS!')

while True:
    print()
    print('Deseja ver uma tabuada [S ou N]')
    opcao = input(f'Resposta: ').upper()
    print()
    if opcao == 'S':

        tabuada = int(input('Tabuada de: '))
        for i in range(1,11):
            print(f'{tabuada:^4} x {i:^4} = {tabuada*i:^4}')
    elif opcao == 'N':
        break
    else:
        continue