#Solicitar as 3 medidas de 1 triângulo
#Após isso, verificar se as medidas realmente
#formam um triângulo, e digam, caso seja um
#triângulo possível, qual tipo de triângulo é
#Equilátero, Isóceles, Escaleno

#Critério para saber se é um triângulo
#Um dos lados nunca pode ser maior que a soma
#dos outros 2 lados

#Equilátero: todos os lados são iguais
#Isóceles: 2 lados iguais e 1 diferente
#Escaleno: 3 lados diferentes

l1 = int(input("medida um: "))
l2 = int(input("medida dois: "))
l3 = int(input("medida três: "))

if l1 > l2 + l3 or l2 > l1 + l3 or l3 > l1 + l2:
    print("Medida inválida")
else:
    if l1 == l2 and l3 == l1:
        print("TRIÂNGULO EQUILÁTERO: ")
    elif l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2:
        print("TRIÂNGULO ISÓCELES:")
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print("TRIÂNGULO ESCALENO:")





