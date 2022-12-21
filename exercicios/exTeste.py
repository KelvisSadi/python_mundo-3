cadastrados = ['jose', 'joao', 'maria', 'claudio', 'jessica', 'veronica']
logados = ['kelvis', 'mathues', 'pedro', 'maria']
for usuario in logados:
    if usuario in cadastrados:
        print(f'O usuario {usuario} está cadastrado!')
    else:
        print(f'O usuario {usuario} não está cadastrado!')
# deveras interessante
