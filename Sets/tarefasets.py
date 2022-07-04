# 1.A empresa JONASREITER PRODUCTIONS vende cursos da área da educação.
# Após a mudança de sistema, o cadastro de clientes ficou embaralhado,
# onde acabou ficando em 2 arquivos .txt. Crie um programa que
# importe 2 arquivos .txt que contenham CNPJs.
# Ao final, diga quantos itens estão duplicados
# Total de duplicados: 422

# email = open('email.txt', 'r')
# nomes = open('nomes.txt', 'r')
# lista1 = nomes.read().splitlines()
# lista2 = email.read().splitlines()
from typing import Set
#
novos = open('clientes sistema novo.txt')
antigos = open('clientes sistema antigo.txt')
lista1 = antigos.read().splitlines()
lista2 = novos.read().splitlines()
lista3 = lista1 + lista2
duplicados = set()

unicos = 0
for i in lista3:
    if lista3.count(i) > 1:
        duplicados.add(i)
    else:
        unicos += 1


print(f'novos: {len(lista1)}')
print(f'antigos: {len(lista2)}')
print(f'total de cadastros: {len(lista1 + lista2)}')

print(f"Duplicados: {len(duplicados)}")
print(f"cadastro único: {len(set(lista1 + lista2))}")
print(f"Repetidos removidos: {len(lista3) - len(set(lista1 + lista2))}")
print(f"Itens a remover para não ter duplicados:









