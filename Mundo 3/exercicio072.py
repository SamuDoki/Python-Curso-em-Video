from num2words import num2words

num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

escolha = int(input('Qual número você quer? De 1 a 20 '))
while escolha not in num:
   escolha = int(input('Escolha um número de 1 a 20. ')) 


text = num2words(escolha, lang= 'pt_BR') #Vai escrever por extenso (em português) o número que o usuário deseja 

print(f'Você escreveu o número {text}')
