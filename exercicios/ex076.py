produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Comapasso',
            9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
produto = 0
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
while True:
    print(f'{produtos[produto]:.<40} R$ ', end='')  # alinhado a esquerda e preenchido com pontos em 40 caracteres
    produto += 1
    print(f'{produtos[produto]:>6.2f}')  # alinhado a direita em 6 espaços e mostrando apenas dois números após o ponto
    produto += 1
    if produto == len(produtos):
        break
print('-'*50)
print('Jeito Guanabara')
print('-'*50)
for pos in range(0, len(produtos)):  # como todos os nomes estão nas casas pares, se for par alinha a esquerda com ...
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end=' ')
    else:
        print(f'R$ {produtos[pos]:>6.2f}')