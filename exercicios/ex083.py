expressão = str(input('Digite a expressão:')).strip().lower()
parenteses = list()
aberto = list()
fechado = list()
for item in expressão:  # para cada caracter na expressão faça
    if item == '(':
        aberto.append(item)
    elif item == ')':
        fechado.append(item)

if len(aberto) != len(fechado):  # se números de aberto e fechados diferentes, inválida.
    print('expressão inválida')
else:  # se nao fechou antes de abri-lo e o número de abertos e fechados são iguais, válida
    print('expressão válida')
# versão do guanabara toda vez que aparece um parenteses {aberto} ele joga na {lista}, e toda vez que aparecesse um
# parenteses {fechado} ele remove um {aberto} da {lista}, então para dar certo o (len) da {lista} tem que estar em zero
