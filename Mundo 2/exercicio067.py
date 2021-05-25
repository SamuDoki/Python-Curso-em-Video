while True:
    número = int(input('Você quer a tabuada de que número? '))
    
    if número < 0:
        print('Numero inválido')
        break

    else:
        for c in range(1, 11):
            print(f'{número} x {c} = {c*número}')
