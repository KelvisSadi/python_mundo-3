valores = list()
maior = menor = 0
for cont in range(5):  # laço no range de 5 vezes
    valores.append(int(input(f'Digite o {cont}º valor:')))
    if cont == 0:  # se primeira vez
        menor = valores[cont]
        maior = valores[cont]
    if valores[cont] < menor:  # se {valor} for menor que {menor}
        menor = valores[cont]
    if valores[cont] > maior:  # se {valor} for maior que {maior}
        maior = valores[cont]
print('=-'*30)
print(f'Estes são valores digitados: {valores}')
print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for pos, item in enumerate(valores):  # laço de cada {pos} e {item} em enumerado(valores)
    if item == maior:  # se {item} for igual a {maior} faça
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições:', end=' ')
for pos, item in enumerate(valores):  # laço de casa {pos} e {item} em enumerado(valores)
    if item == menor:  # se {item} igual a {menor} faça
        print(f'{pos}...', end=' ')
