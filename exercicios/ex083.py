expressão = str(input('Digite a expressão:')).strip().lower()
parenteses = list()
aberto = fechado = invalidou = 0
for item in expressão:  # para cada caracter na expressão faça
    if item == '(' or item == ')':
        parenteses.append(item)
cont = 0
# While para verificação se algum parenteses é fechado antes de abri-lo
while cont < len(parenteses):  # enquanto contador menor que o tamanho da expressão faça:
    if parenteses[cont] == '(':  # se for parenteses aberto
        aberto += 1
    else:  # se for parenteses fechado
        fechado += 1
    if fechado > aberto:  # se fechar algum parenteses antes de abri-lo, inválida a expressão!
        print('expressão inválida')
        invalidou = 1  # var invalidou para não invalidar 2 vezes
        break
    cont += 1
# verifica se não fechou todos parenteses
if aberto != fechado and invalidou != 1:  # se números de aberto e fechados diferentes, inválida.
    print('expressão inválida')
elif aberto == fechado:  # se nao fechou antes de abri-lo e o número de abertos e fechados são iguais, válida
    print('expressão válida')
