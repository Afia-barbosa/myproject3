#stock keepeing unit
# Código SKU

# Tipos de Produto:
# MON - Monitor
# TEC - Teclado
# MOU - Mouse

# Cor:
# PR - Preto
# AZ - Azul
# VM - Vermelho
# BR - Branco

# Material de Fabricação:
# PP = Polipropileno
# PE = Polietileno
# PO = Poliamida

# Geração:
# 1G - 1ª Geração
# 2G - 2ª Geração
# 3G - 3ª Geração

# Ano Cadastro:

# EXEMPLO:
# Mouse Branco de Poliamida 3ª Geração 2022 = MOU-BR-PO-3G/2022

# Criar um código que você pode cadastrar um produto, escolhendo as opções, e
# ao final ele traga o código, e que também possa digitar o código e ele trazer
# as informações

prod1 = int(input("Digite o tipo de Produto [1-Monitor], [2-Teclado], [3- Mouse]:"))
prod2 = int(input("Digite a cor [1-preto], [2-azul], [3-vermelho], [4-branco]:"))
prod3 = int(input("Digite o material de fabricação [1-Polipropileno],[2-Polietileno], [3-Poliamida]:"))
prod4 = int(input("Digite a Geração [1-1ª Geração],[2-2ª Geração], [3- 3ª Geração]:"))
prod5 = int(input("Digite o Ano de Cadastro:"))
if prod5 < 2020 or prod5 > 2025:
    print("Não encontramos seu produto:")
elif prod1 == 1:
    at = "MON"
elif prod1 == 2:
    at = "TEC"
else:
    at = "MOU"

if prod2 == 1:
    bt = "PR"
elif prod2 == 2:
    bt = "AZ"
elif prod2 == 3:
    bt = "VM"
else:
    bt = "BR"

if prod3 == 1:
    ct = "PP"
elif prod3 == 2:
    ct = "PE"
else:
    ct = "PO"

if prod4 == 1:
    dt = "1G"
elif prod4 == 2:
    dt = "2G"
else:
    dt = "3G"

print(at,bt,ct,dtsep="-",end="/")
print(prod5)
#MOU-BR-PO-3G/2022









