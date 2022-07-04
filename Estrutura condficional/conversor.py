"""
Criar um algoritmo que traga a seguinte possibilidade

-----------------------------------------
          Selecione uma opção
-----------------------------------------
1 - Converter de Celsius para Kelvin
2 - Converter de Celsius para Fahrenheit
3 - Converter de Kelvin para Celsius
4 - Converter de Kelvin para Fahrenheit
5 - Converter de Fahrenheit para Celsius
6 - Converter de Fahrenheit para Kelvin

Ex:
Opção: 1
Digite a temperatura em Celsius: 30
Temperatura em Kelvin: 303.15 K

"""

print('===============================')
print('Selecione uma Opção')
print('==============================')
print('1-Converter de Celsius para Kelvin')
print('2-Converter de Kelvin para Celsius')
print('3-Converter de Kelvin para Fahrenheit')
print('4-Converter de Fahrenheit para Celsius')
print('5-Converter de Fahrenheit para Kelvin')
op=int(input('Digite sua escolha: '))
if op==1:
    c=float(input('Digite a temperatura em Celsius: '))
    k= c+273.15
    print(k)
elif op==2:
    k = float(input('Digite a temperatura em Kelvin: '))
    c= k-273.15
    print(c)
elif op==3:
    k=float(input('Digite a temperatura em Kelvin: '))
    f= (k-273.15)*1.8+32
    print(f)
elif op == 4:
    f=float(input('Digite a temperatura em Fahrenheit: '))
    c= (f-32)/1.8
    print(c)
elif op==5:
    f=float(input('Digite a temperatura em Fahrenheit: '))
    k= (f-32)*5/9-273
    print(k)