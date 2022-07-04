# Criar um algoritmo quantos números
# você desejar (laço infinito), e ao final dele mostre:
# A lista em ordem crescente
# A lista em ordem decrescente
# A soma de todos os itens
# A média de todos os números

# numeros = []
# media = 0
# while True:
#     num = int(input('Digite um número:'))
#     numeros.append(num)
#     media += 1
#     escolha = input('Você deseja adicionar mais números?\n1-Não\n2-Sim\n')
#     if escolha == '1':
#         soma = sum(numeros)
#         numeros.sort()
#         print(f'{numeros}')
#         numeros.sort(reverse=True)
#         print(f'{numeros}')
#         print(f'Soma: {soma}')
#         print(f'Média: {soma/media}')
#         break

# Crie um algoritmo que receba quantos nomes(apenas nome) desejar, e ao final:
# A lista em ordem crescente
# A lista em ordem decrescente
# O total de nomes cadastrados
# Quantos ‘Carlos’ existem na lista

nome = []
total = 0
n = int(input("Digite a quantidade de nomes que deseja cadastrar: "))
for i in range(n):
    a = input('Digite o nome que você deseja cadastrar: \n')
    nome.append(a)
nome.sort()
print(f'{nome}')
nome.sort(reverse=True)
print(f'{nome}')
total = len(nome)
print(f'Total de nomes: {total}')
q = nome.count("carlos")
print(f'Total de Carlos: {q}')

# Crie um algoritmo que receba valores aleatórios (de qualquer tipo), e ao final:
# A lista em ordem inversa ao que foi lançado
# quantos dados são de cada tipo: int, str, float, bool






