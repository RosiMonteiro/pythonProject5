print('Bem-vindo à Escolha do Caminho!')

print ('''lista dos caminhos
1 = caminhoA
2 = caminhoB
3 = caminhoC''')

caminho = int(input('Escoha um dos caminhos:'))

if caminho == 3:
    print('3 é um caminho cheio de perigo, escolha outro caminho.')

elif caminho == 2:
    print('b é um caminho de obstaculos! Escolha outro caminho.')
else:
    print('1 é um caminho seguro! siga em frente.')