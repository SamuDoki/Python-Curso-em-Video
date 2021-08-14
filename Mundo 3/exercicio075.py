tupla = (int(input('Digite um número: ')), 
        int(input('Digite o segundo número: ')), 
        int(input('Digite o terceiro número: ')), 
        int(input('Digite o quarto número: ')))

print(f'O número 9 apareceu {tupla.count(9)}') 
if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3) + 1}')

else:
    print('O número 3 não apareceu')

print('Esses foram os números pares digitados: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')

