from random import choice
import random
from definições_avançado2 import estados, fatos



if 5 in estados:
    print('deu certo')



fatos = {
            'partida': 2050,
            'status': {'Sanidade': 50,
            'Popularidade': 50,
            'Notas': 50,
            'Inteligência': 50
            },
            'cenarios': [28, 29],
            'estado_anterior_aleatorio': 28
        }


valores = []

#for cont in range (0, 5):
#    valores.append(int(input('Digite um valor: ')))

#print(valores)
fato_do_jogador = fatos
senarios = fato_do_jogador['cenarios']

for cont in range (0, 5):
    copia = senarios[:]
    copia.remove(fato_do_jogador['estado_anterior_aleatorio'])
    flip = random.choice(copia)
    fato_do_jogador['estado_anterior_aleatorio'] = flip
    print('Resultado do flip: ' + str(flip))


print('Senarios: ' + str(senarios))
print('Copia: ' + str(copia))