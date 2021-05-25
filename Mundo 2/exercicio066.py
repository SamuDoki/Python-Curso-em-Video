número = 0
soma = 0
quantidade = 0

while número != 999:
    número = int(input('Digite um valor [Digite 999 para parar]: '))
    quantidade += 1
    soma += número


print(f'Você digitiu {quantidade - 1} números, e a soma de todos eles é igual a {soma - 999}')
