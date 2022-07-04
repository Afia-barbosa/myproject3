# 0	Rio Grande do Sul
cpf = input('Digite seu CPF: ')
estado = cpf[10]

if estado == '0':
    print('Rio Grande do Sul')
elif estado == '1':
    print('Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul ou Tocantis')
elif estado == '2':
    print('Amazonas, Pará, Roraima, Amapá, Acre ou Rondônia')
elif estado == '3':
    print('Ceará, Maranhão ou Piauí')
elif estado == '4':
    print('Paraíba, Pernambuco, Alagoas ou Rio Grande do Norte')
elif estado == '5':
    print('Bahia ou Sergipe')
elif estado == '6':
    print('Minas Gerais')
elif estado == '7':
    print('Rio de Janeiro ou Espírito Santo')
elif estado == '8':
    print('São Paulo')
elif estado == '9':
    print('Paraná ou Santa Catarina')