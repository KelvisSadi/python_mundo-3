print(f'{" Listas ":-^40}')
lanche = ["hamburguer", "suco", "pizza", "pudim"]

# lanche.insert(0, "cachorro-quente") | lanche.append("picole") = adicionando elementos
# lanche.pop(3) | del lanche[3] | lanche.remove("pizza") = apagando elementos
# lanche.pop() elimina o último elemento
if "pizza" in lanche:
    lanche.remove("pizza")
print(lanche)
valores = [8, 3, 6, 5, 4, 2, 77, 8, 8, 4]

print('-'*40)  # ordenando valores na forma reversiva
valores.sort(reverse=True)
print(valores)
print(f'quantidade de valores dentro da lista: {len(valores)}')

print('-'*40)  # indece 0 recebendo valor 2
valores[0] = 2
print(valores)

print('-'*40)  # adicionando valor 1000 no indice 1
valores.insert(1, 1000)
print(valores)

print('-'*40)  # removendo o indice 1
valores.pop(1)

print(valores)
valores2 = [5, 6, 5, 8, 4, 5]

print(valores2)
while 10 in valores2:  # enquanto tiver 5 em valores2
    valores2.remove(10)  # remova o 5, OBS: O {remove} remove o primeiro valor 5 que acha, por isso uso da repetição!

print('Testando cópiamento de lista')
a = list(range(1, 10, 2))
b = a
print(f'A = {a}')
print(f'B = {b}')
print('criando um ligação entre lista A e B com comando b = a')
b[2] = 9  # OBSERVAÇÃO! SEMPRE QUE IGUALAR UMA LISTA A OUTRA, CRIA UM LIGAÇÃO ENTRE ELAS E UMA MUDANÇA MUDA AS DUAAS!!!!
print(f'A = {a}')
print(f'B = {b}')
print('-'*40)
# PARA FAZER UMA CÓPIA DOS VALORES DE UMA LISTA USAR O FATIAMENTO EXEMPLO
c = a[:]
print(f'C = {c}')
print(f'A = {a}')
print('Somente copiando os valores da lista A pra C com comando c = a[:]')
a[0] = 9999
print(f'C = {c}')
print(f'A = {a}')
print('-'*40)
for posição, valor in enumerate(valores2):  # para cada X dentro de Y faça:
    print(f'Na poição {posição + 1} encontrei {valor} ...')
nomes_idade = list()
for entrada in range(3):
    nomes_idade.append(str(input('Digite seu nome:')))
    nomes_idade.append(int(input('Digite sua idade')))
print(nomes_idade)
for item in nomes_idade:
    if type(item) == str:
        print(f'Nome: {item:.<30}', end=' ')
    else:
        print(f'Idade: {item}')
