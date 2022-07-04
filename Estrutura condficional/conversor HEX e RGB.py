# # Conversão de número para Hexadecimal PYTHON
# W3SCHOOLS - FORMAT
# receber os valores de R, G e B, e ao final
# apresentar o Código Hexadecimal
# EX: R - 255
#     G - 255
#     B - 160
# RESPOSTA: #FFFFA0
# Não pode lançar valores para R, G ou B que estejam fora dos números
# 0 a 255


R = int(input('Digite um número para o R:'))
G = int(input('Digite um número para o G:'))
B = int(input('Digite um número para o B:'))
if R < 0 or R > 255 or G < 0 or G > 255 or B < 0 or B > 255:
    print('NÚMERO RGB INCORRETO')
else:
    print(f'#{R:02X}{G:02X}{B:02X}')