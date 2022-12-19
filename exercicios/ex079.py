valores = list()
while True:
    num = int(input('Digite um valor:'))
    if num in valores:
        print('Valor duplicado, NÃO adicionado!')
    else:
        valores.append(num)
        print('Valor ADICIONADO com sucesso...')
    print(f'{"---":^30}')
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja Continuar [S/N]')).strip().upper()[0]
        print(f'{"---":^30}')
    if continuar == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
print(f'{" Programa encerrado ":-^30}')
