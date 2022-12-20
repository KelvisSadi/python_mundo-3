valores = list()
while True:  # while infinito
    num = int(input('Digite um valor:'))
    if num in valores:  # if {num} estiver em valores faça:
        print('Valor duplicado, NÃO adicionado!')
    else:  # se não faça
        valores.append(num)
        print('Valor ADICIONADO com sucesso...')
    print(f'{"---":^30}')
    continuar = ''
    while continuar != 'S' and continuar != 'N':  # enquanto continuar diferente de 'S' e 'N'OBS:acaba se for 'S' ou 'N'
        continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
        print(f'{"---":^30}')
    if continuar == 'N':  # se {continuar} igual a 'N'
        break
print(f'Você digitou os valores: {sorted(valores)}')  # pode usar também ex:sorted(valores, reverse=True)
print(f'{" Programa encerrado ":-^30}')
