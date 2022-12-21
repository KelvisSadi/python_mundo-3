valores = list()
valores_imp = list()
valores_par = list()
while True:  # while infinito n1
    num = int(input('Digite um número:'))
    valores.append(num)
    continuar = ''
    while continuar != 'S' and continuar != 'N':  # while {S} e {N} diferente de {continuar}
        continuar = str(input('Deseja continuar adicionado números? [S/N]')).strip().upper()[0]
    if continuar == 'N':  # se {continuar} igual {N}
        break  # break n1
for item in valores:  # laço para cada item em valores
    if item % 2 == 0:  # se o resto da divisão de item por 2 for igual a zero, quer dizer que é PAR
        valores_par.append(item)
    else:  # se não, só pode ser ímpar
        valores_imp.append(item)
print(f'Valores: {valores} \nValores pares: {valores_par} \nValores ímpares: {valores_imp}')
