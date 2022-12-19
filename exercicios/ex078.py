valores = list()
for cont in range(5):
    valores.append(int(input(f'Digite o {cont}º valor:')))
print('=-'*30)
maior = menor = 0
for contador, valor in enumerate(valores):
    if contador == 0:
        menor = valor
        maior = valor
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor
print(f'Estes são valores digitados: {valores}')
print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for pos, item in enumerate(valores):
    if item == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições:', end=' ')
for pos1, item2 in enumerate(valores):
    if item2 == menor:
        print(f'{pos1}...', end=' ')
