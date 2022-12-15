numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número inteiro entre 0 e 20:'))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20:'))
print(numeros[num])