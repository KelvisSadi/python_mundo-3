lanches = ('hamburguer', 'suco', 'pizza', 'doce', 'a', 'b', 'c')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
c = sorted(c)
print(c.index(1))

print('-' * 15)
print(lanches[-1::-1])
print('-'*15)
print(len(lanches))
print(sorted(lanches))

print('-'*15)
for lanche in lanches:  # Modo simples de mostrar a tupla
    print(lanche)

# As tuplas são imutáveis

print('-'*15)
for cont in range(0, len(lanches)):  # Bom para mostrar a posição tambem
    print(lanches[cont], cont)

print('-'*15)
for pos, comida in enumerate(lanches):  # Segundo modo de mostrar a posição tambem
    print(comida, pos)

print('-'*15)
c = -1
while c > -5:
    print(lanches[c])
    c -= 1
