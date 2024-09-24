def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        print('Erro! Não dividirá por zero!')
        return None

def calc():
    print('===== NumberCrunch =====')

    while True:
        print('Selecione a operação:')
        print('1. SOMA')
        print('2. SUBTRAÇÃO')
        print('3. MULTIPLICAÇÃO')
        print('4. DIVISÃO')
        print('5. SAIR')

        opcao = input('Digite o numero da operação desejada: ')

        if opcao == '5':
            print('Obrigado por utilizar do nosso serviço da NumberCrunch!')
            break

        num1 = float(input('Primeiro numero: '))
        num2 = float(input('Segundo numero: '))

        if opcao == '1':
            result = soma(num1, num2)
        elif opcao == '2':
            result = subtracao(num1, num2)
        elif opcao == '3':
            result = multiplicacao(num1, num2)
        elif opcao == '4':
            result = divisao(num1, num2)
        else:
            print('Opção invalida.')
            continue

        if result is not None:
            print('Resultado: ', result)

calc()