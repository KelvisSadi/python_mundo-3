lista = list()
for cont in range(5):  # laço de 5 vezes
    num = int(input('Digite um número:'))
    if cont == 0:  # se o laço estiver na primeira passagem faça
        print('Primeiro item adicionado...')
        print('-'*30)
        lista.append(num)
    contador = 0
    while contador < len(lista):  # enquanto contador for menor que o tamanho da lista faça
        if num < lista[contador]:  # se num for menor algum número dentroda lista faça: vai inserir ele nessa posição
            lista.insert(contador, num)
            print(f'Adicionado na posição {contador} da lista...')
            print('-' * 30)
            break
        elif cont != 0 and contador == len(lista) - 1:
            # se não estiver na primeira passagem e contador igual ao último indice da lista
            lista.append(num)
            print(f'Adicionado no final da lista ...')
            print('-' * 30)
            break
        contador += 1
print(f'Esses foram os valores digitados {lista}')

