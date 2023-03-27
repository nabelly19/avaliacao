print('Bem vindo a calculadora Bosch')

print('\nOperações:\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação')

op = int(input('\nQual operação você deseja fazer? '))
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

if op == 1:
    print('\nR:', valor1 + valor2)

elif op == 2:
    print('\nR:', valor1 - valor2)

elif op == 3:
    print('\nR:', valor1 / valor2)

elif op == 4:
    print('\nR:', valor1 * valor2)

else:
    print('Algo deu errado')