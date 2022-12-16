numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número inteiro entre 0 e 20:'))
    if num < 0 or num > 20:
        print('Tente novamente.', end=' ')
    else:
        print(f'Você digitou o número {numeros[num]}')
        continuar = ''
        while continuar != 'S':
            continuar = str(input('Quer continuar [S/N]')).upper().strip()[0]
            if continuar == 'N':
                break
    if continuar == 'N':
        break
