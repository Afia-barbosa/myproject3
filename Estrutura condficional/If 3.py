"""
INFORME A QUANTIDADE DE LADOS, E AO FINAL, DIGA QUAL É A FIGURA GEOMÉTRICA
1 LADO, É PONTO
2 LADOS ... LINHA
3 LADOS ... TRIANGULO
4 LADOS ... QUADRADO
5 LADOS ... PENTÁGONO
6 LADOS ... HEXÁGONO

SE O NÚMERO FOR MAIOR QUE 6, TRAZER COMO RESPOSTA: VOCÊ ESTÁ CERTO DISSO?

"""

la =int(input("Digite o número de lados: "))
if la == 1:
    print("A figura geométrica é um ponto: ")
elif la == 2:
    print("A figura geométrica é uma linha: ")
elif la == 3:
    print("A figura geométrica é um TRIANGULO: ")
elif la == 4:
    print("A figura geométrica é um quadrado: ")
elif la == 5:
    print("A figura geométrica é um Pentágono: ")
elif la == 6:
    print("A figura geométrica é um HEXÁGONO: ")
else:
    print("Tem certeza disso? ")


