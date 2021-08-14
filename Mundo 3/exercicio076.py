lista = ('Lápis', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90
        )

print('--- LISTAGEM DE PREÇOS ---')
    
for check in range(0, len(lista)):
    if check % 2 == 0:
        print(f'{lista[check]}{"." * (35 - len(lista[check]))}', end='')  #primeiro termo é as palavras // Segundo termo é multiplicar os pontos por 35 - quantas letras tem a palavra, para balancear
    
    else:
        print(float(lista[check]))
