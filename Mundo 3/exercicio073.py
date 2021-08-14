tabela = ('Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense',
            'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC',
            'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 
            'Goiás', 'Chapecoense', 'Botafogo')

print(f'Os cinco primeiros colocados são {tabela[:5]}\n')
print(f'Os cinco últimos colocados são {tabela[-5:]}\n')
print(f'Times organizados alfabeticamente: {sorted(tabela)}\n')
print(f'A Chapecoense está na {tabela.index("Chapecoense")}° posição')
