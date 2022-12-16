produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Comapasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
produto = 0
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
while True:
    print(f'{produtos[produto]:.<40} R$ ', end='')
    produto += 1
    print(f'{produtos[produto]:>6.2f}')
    produto += 1
    if produto == len(produtos):
        break
print('-'*50)