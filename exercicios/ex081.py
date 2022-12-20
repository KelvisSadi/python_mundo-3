valores = list()
pos_ord = list()
pos = list()
pos_dig = list()
while True:
    n = int(input('Digite um número:'))
    valores.append(n)
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer adicionar mais números [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
valores_ord = sorted(valores, reverse=True)
for pos, item in enumerate(valores_ord):
    if item == 5:
        pos_ord.append(pos)
for pos2, item2 in enumerate(valores):
    if item2 == 5:
        pos_dig.append(pos2)
print('-'*30)
print(f'Ao total foram digitados {len(valores)}...')
print(f'Os valores na ordem de digitação são: {valores}')
print(f'Os valores em ordem decrescente são: {valores_ord}')
if 5 in valores:
    print(f'O número 5 está na lista e aparece {valores.count(5)} vezes')
    print(f'O número 5 na ordem de digitação aparece nas posições: {pos_dig} ')
    print(f'O número 5 na ordem descrescente aparece nas posições {pos_ord}')
else:
    print(f'O número 5 não está na lista!')


