# 1.Crie um algoritmo que, dado um número informado pelo usuário,
# imprima a tabuada dele de 1 a 10. Use o formato de apresentação
# (considerando que o usuário informou o número 5):
#     5 x 1 = 5
#     5 x 2 = 10
#     5 x 3 = 15

# Questão 1

# 2.Faça um programa que calcule o fatorial de um número.
# Esse programa deve receber como entrada um número inteiro positivo
# e imprimir na tela o fatorial dele.
# questão 2

#
# 3.Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
#  Dada a massa inicial, em gramas, fazer um programa em que calcule o tempo necessário para que essa massa se torne menor que 0,5 grama.
#   O programa deve escrever a massa inicial, a massa final e o tempo calculado em horas, minutos e segundos.
#Questão


# 4.Desenvolver um programa que leia um número não determinado de valores,
# calcule e escreva a média aritmética deles, a quantidade de valores positivos,
# a quantidade de valores negativos, o percentual de valores negativos e positivos,
# qual o valor máximo, e qual o valor mínimo.

# num = 0
# qt_negativos = 0
# qt_positivos = 0
# maximo = 0
# minimo = 0
# cont = 0
# total = 0
#
# while True:
#     num = int(input("Digite o número desejado, ou 0 para parar"))
#     if num == 0:
#         break
#
#     total += num
#     cont += 1
#
#     if num < 0:
#         qt_negativos += 1
#     else:
#         qt_positivos += 1
#
#     if num > maximo or cont == 1:
#         maximo = num
#     if num < minimo or cont == 1:
#         minimo = num
#
# print(f"Total lançado: {total}")
# print(f"Quantidade lançamentos: {cont}")
# print(f"média : {total / cont}")
# print(f"positvos: {qt_positivos}")
# print(f"negativos: {qt_negativos}")
# print(f"% positivos: {qt_positivos / cont:.2%}")
# print(f"% negativos: {qt_negativos / cont:.2%}")
# print(f"maximo: {maximo}")
# print(f"minimo: {minimo}")



# 7.Escrever um algoritmo que gera
# e escreve os números ímpares entre 100 e 200.

# 8.  	Crie um programa que receba um número indeterminado de anos. Ao final, apresente quantos anos são pares,
# quantos são ímpares, quantos são bissextos, quantos são futuros (2023, 2024), e quantos são passado (2000, 2010)
# 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052
# par = 0
# imp = 0
# bis = 0
# futuro = 0
# passado = 0
#
# while True:
#     ano = int(input("Digite um ano: "))
#     if ano / 2 == 0:
#         par += 1
#     else:
#         imp += 1
#
#     if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#         bis += 1
#
#     if ano > 2022:
#         futuro += 1
#     elif ano < 2022:
#         passado += 1
#
#     print('Deseja continuar?')
#     resp = input('Resposta [s] ou [n]: ')
#     if resp == "n":
#         break
#
# print(f"anos pares {par}: ")
# print(f"anos impares {imp}: ")
# print(f"quantos anos bisseextos {bis}: ")
# print(f"quantos anos futuros {futuro}: ")
# print(f"quantos anos passado {passado}: ")
#








