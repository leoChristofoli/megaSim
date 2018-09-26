import random
import time

numeros = input('Numeros separados por ",": ')

def validate(numeros):
    numeros = numeros.split(',')
    if len(numeros) != 6:
        return False
    return True


def sorteio():
    numeros = [x for x in range(1,61)]
    sorteados = []
    for i in range(6):
        numero = random.choice(numeros)
        numeros.remove(numero)
        sorteados.append(numero)
    return sorteados


def tentar_a_sorte(numeros):
    i = 0
    numeros = [int(x) for x in numeros.split(',')]

    while True:
        sorteados = set(sorteio())
        numeros = set(numeros)
        resultado = list(numeros - sorteados)
        i += 1
        print("sorteio # {0} | chute: {1} - resultado: {2} - sua sorte: {3} - acertos {4} \n                   \r".format(i, numeros, sorteados, resultado, (6 - len(resultado)) ), end='')
        if len(resultado) == 0:
            print("Parabéns! Você precisou de {0} tentativa(s) para ficar milionário".format(i))
            break

if validate(numeros):
    tentar_a_sorte(numeros)