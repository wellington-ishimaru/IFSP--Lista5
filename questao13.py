print('******* Desenha retangulo ******\n')

def retangulo(l, a):
    if l > 20:
        l = 20
    if a > 20:
        a = 20
    print('+' + '--'*l + '+')
    c = 0
    while c < a:
        z = '|'
        print(f'{z}'+ '  '*l + f'{z}')
        c += 1
    print('+' + '--'*l + '+' )


largura = int(input('Informe a largura: '))
altura = int(input('Informe a altura: '))
retangulo(largura, altura)