def somar(numero1, numero2):
    print(f'Realizando soma de {numero1} + {numero2}')
    return numero1 + numero2

def subtrair(numero1, numero2):
    print(f'Realizando subtracao de {numero1} - {numero2}')
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    print(f'Realizando multiplicacao de {numero1} * {numero2}')
    return numero1 * numero2

def divisao(numero1, numero2):
    print(f'Realizando divisao de {numero1} / {numero2}')
    return numero1 / numero2

if __name__ == '__main__':
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))

    operador = input('Qual operacao matematica voce deseja fazer? (+, -, /, *)')

    resultado = 0

    if operador == '+':
        resultado = somar(n1, n2)

    elif operador == '-':
        resultado = subtrair(n1, n2)

    elif operador == '*':
        resultado = multiplicacao(n1, n2)

    elif operador == '/':
        resultado = divisao(n1, n2)

    else:
        print('Operador incorreto.')

    print(f'O resultado da operacao e: {resultado}')