a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
c = int(input('Digite um número:'))
d = int(input('Digite um número:'))
tupla = (a, b, c, d)
print('A tupla não contem nenhum número 9')if 9 not in tupla else print(f'O número nove apareceu {tupla.count(9)} vezes')
print('A tupla não contém nenhum número 3')if 3 not in tupla else print(f'O primeiro número 3 apareceu na posição {tupla.index(3) + 1}')
print('Os números pares são: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')

