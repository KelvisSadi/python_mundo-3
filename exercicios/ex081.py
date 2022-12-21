valores = list()
pos_ord = list()
pos = list()
pos_dig = list()
while True:  # while infinito n1
    n = int(input('Digite um número:'))
    valores.append(n)
    continuar = ''
    while continuar != 'S' and continuar != 'N':  # while {continuar} diferente de {S} e continuar diferente de {N}
        continuar = str(input('Quer adicionar mais números [S/N]')).strip().upper()[0]
    if continuar == 'N':  # se {continuar} igual a {N}
        break  # break n1
valores_ord = sorted(valores, reverse=True)  # salva os valores de forma ordenada na var {valores_ord}
for pos, item in enumerate(valores_ord):  # laço para pegar cada pos, {valor} em enumerate{valores_ord}
    if item == 5:
        pos_ord.append(pos)
for pos, item in enumerate(valores):  # laço para pegar cada pos, {valor} em enurate{valores}
    if item == 5:
        pos_dig.append(pos)
print('-'*30)
print(f'Ao total foram digitados {len(valores)} valores ...')
print(f'Os valores na ordem de digitação são: {valores}')
print(f'Os valores em ordem decrescente são: {valores_ord}')
if 5 in valores:
    print(f'O número 5 está na lista e aparece {valores.count(5)} vezes')
    print(f'O número 5 na ordem de digitação aparece nas posições: {pos_dig} ')
    print(f'O número 5 na ordem descrescente aparece nas posições {pos_ord}')
else:
    print(f'O número 5 não está na lista!')


