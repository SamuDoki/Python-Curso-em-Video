palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalho', 'mercado', 'programador', 'futuro')


for palavra_na_lista in palavras:

    print(f'\nNa palavra {palavra_na_lista} temos as vogais ', end='')
    
    for letras in palavra_na_lista:
        
        if letras in 'AEIOU':
            print(letras, end=' ')        
