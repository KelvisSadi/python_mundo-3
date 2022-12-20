valores = list()
valores_imp = list()
valores_par = list()
while True:
    num = int(input('Digite um número:'))
    valores.append(num)
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar adicionado números? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
for item in valores:
    if item % 2 == 0:
        valores_par.append(item)
    else:
        valores_imp.append(item)
print(f'Valores: {valores} \nValores pares: {valores_par} \nValores ímpares: {valores_imp}')
