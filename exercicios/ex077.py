palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
contador = 0
vogais = ('a', 'e', 'i', 'o', 'u')
contador_vogais = 0
while True:  # while n1
    print(f'Na palavra {palavras[contador]} temos: ', end='')
    while True:  # while n2
        qtd_vogal = palavras[contador].count(vogais[contador_vogais])  # conta quantos vagais 'x' tem na palavra
        if qtd_vogal > 0:  # se tiver mais que zero faça
            print(vogais[contador_vogais] * qtd_vogal, end='')  # printa vogal[x] * qtd que ela aparece na palavra
        contador_vogais += 1  # contador_vogais recebe mais um e agora vai verificar a proxima vogal na mesma frase
        if contador_vogais == len(vogais):  # se todas as vogais forem verificadas termina o while
            break  # break n2
    print('\n')
    contador += 1  # contador recebe mais um, assim mudando a palavra
    contador_vogais = 0  # contador recebe zero para verificar cada vogal na proxima palavra
    if contador == len(palavras):
        break  # break n1
