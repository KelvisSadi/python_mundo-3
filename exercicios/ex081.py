valores = list()
contador = 0
pos = list()
while True:
    n = int(input('Digite um número:'))
    valores.append(n)
    if n == 5:
        pos.append(contador)
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer adicionar mais números [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
    contador += 1
valores_ord = sorted(valores, reverse=True)
pos_ord = list()
for cont in range(len(valores_ord)):
    if valores_ord[cont] == 5:
        pos_ord.append(cont)

print('-'*30)
print(f'Ao total foram digitados {len(valores)}...')
print(f'Os valores na ordem de digitação são: {valores}')
print(f'Os valores em ordem decrescente são: {valores_ord}')
if 5 in valores:
    print(f'O número 5 está na lista e aparece {valores.count(5)} vezes')
    print(f'O número 5 na ordem de digitação aparece nas posições: {pos} ')
    print(f'O número 5 na ordem descrescente aparece nas posições {pos_ord}')
else:
    print(f'O número 5 não está na lista!')


