# Price
# calcular a parcelar

valor = float(input('Digite o valor a financiar: '))
nper = int(input('Digite a quantidade de parcelas: '))
taxa = float(input('Digite a taxa de juros: '))/100
opcao = int(input('Deseja qual tipo [1]Price [2]SAC '))

while True:
    if opcao == 1:
        # Price
        prestacao = valor * (((1+taxa)**nper*taxa)/((1+taxa)**nper-1))
        print('Nº     Amortização      Juros        Saldo devedor')
        for i in range(nper):
            juros = taxa * valor
            amort = prestacao - juros
            valor -= amort
            print(i+1, end=' ')
            print(f'R$ {prestacao:.2f}', end=' ')
            print(f'R$ {amort:.2f}', end=' ')
            print(f'R$ {juros:.2f}', end=' ')
            print(f'R$ {valor:.2f}')
            break
    elif opcao == 2:
        #SAC
        amort = valor /nper
        print('Nº           Amortização Juros        Saldo devedor')
        for i in range(nper):
            juros = taxa * valor
            prestacao = amort + juros
            valor -= amort
            print(i+1, end=' ')
            print(f'R$ {prestacao:.2f}', end=' ')
            print(f'R$ {amort:.2f}', end=' ')
            print(f'R$ {juros:.2f}', end=' ')
            print(f'R$ {valor:.2f}')
            break
    else:
        print('Digite apenas 1 ou 2')