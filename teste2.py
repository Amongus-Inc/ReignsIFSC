import random

sanidade = 50
popularidade = 50
notas = 50
inteligência = 50

senarios = ['N1', 'N2', 'N3']
#senario com s, é porque eu quero

#if mensagem do discord for iniciar o bagulho começa
sorteio = random.choice(senarios)


print('Você quer participar da aula do Carlyle?')

while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
    resposta = input("Sua descisão: ")
    if resposta.startswith('sim'):
            sanidade = sanidade
            popularidade = popularidade
            notas = notas
            inteligência = inteligência
            print('Sanidade: ' + str(sanidade))
            print('Popularidade: ' + str(popularidade))
            print('Notas: ' + str(notas))
            print('Inteligência: ' + str(inteligência))
            senarios.append('S1')
    elif resposta.startswith('nao'):
            sanidade = sanidade
            popularidade = popularidade + 10
            notas = notas
            inteligência = inteligência
            print('Sanidade: ' + str(sanidade))
            print('Popularidade: ' + str(popularidade))
            print('Notas: ' + str(notas))
            print('Inteligência: ' + str(inteligência))
    else:
        print('digita direito capeta')
        print('Sanidade: ' + str(sanidade))
        print('Popularidade: ' + str(popularidade))
        print('Notas: ' + str(notas))
        print('Inteligência: ' + str(inteligência))



print ('perdeu otario')
print (senarios)