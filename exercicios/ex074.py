from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {num}')
num_ordenado = sorted(num)
print(f'O maior valor sorteado foi {num_ordenado[-1]}')
print(f'O menor valor sorteado foi {num_ordenado[0]}')
