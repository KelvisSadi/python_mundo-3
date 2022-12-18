palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
print('-'*40)
print('Contando vogais em Tupla')
print('-'*40)
for palavra in palavras:  # para cada palavra em palvras faça:
    print(f'{palavra}:', end=' ')  # printa a palavra atual no for
    for vogal in vogais:  # para cada vogal em vogais faça:
        qtd = palavra.count(vogal)  # conta a quantidade da vogal atual dentro da palavra
        if vogal in palavra:  # se tem a vogal atual na palavra faça:
            print(f'{vogal * qtd}', end='')  # printa a vogal * a qtd de vez que tem ela
    print('')
    qtd = 0  # zera a qtd para a verificação da próxima palavra
print('-'*40)
print('Jeito Guanabara')
print('-'*40)
for p in palavras:
    print(f'\nNa palavra {p} temos:', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')

