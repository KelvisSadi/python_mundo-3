tupla = (int(input('Digite o 1º número:')), int(input('Digite o 2º número:')),
         int(input('Digite o 3º número:')), int(input('Digite o 4º número:')))
print(f'A tupla contém: {tupla}')
print('A tupla não contem número 9')if 9 not in tupla else print(f'O número nove apareceu {tupla.count(9)} vezes')
print('A tupla não contém número 3')if 3 not in tupla else print(f'O primeiro número 3 apareceu na posição {tupla.index(3) + 1}')
print('Os números pares são: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')

