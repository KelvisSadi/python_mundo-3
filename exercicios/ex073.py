times_brasileirão = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Athletico-PR', 'Fortaleza',
                     'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Cortiba', 'Cuiabá',
                     'Ceará', 'Atlético-GO', 'Avai', 'Juventude')
print(f'Primeiros cinco times do Brasileirão: {times_brasileirão[:5]}')
print('-'*30)
print(f'Últimos quatro times do Brasileirão: {times_brasileirão[-4:]}')
print('-'*30)
print(f'Times do Brasileirão em ordem alfabética: {sorted(times_brasileirão)}')
print('-'*30)
print(f'O Internacional está  na {times_brasileirão.index("Internacional") + 1}ª posição')
