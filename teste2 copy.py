import random

sanidade = 50
popularidade = 50
notas = 50
inteligência = 50

senarios = ['N1', 'N2', 'N3']
#senario com s, é porque eu quero

#if mensagem do discord for iniciar o bagulho começa
while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
        sorteio = random.choice(senarios)
        if sorteio == 'N1':
                print('Você quer participar da aula do Carlyle?')
                while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade - 10
                                popularidade = popularidade
                                notas = notas
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.append('S1')
                                break
                        elif resposta.startswith('nao'):
                                sanidade = sanidade + 20
                                popularidade = popularidade
                                notas = notas
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                break
                        else:
                                print('digita direito capeta')
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                
        elif sorteio == 'N2':
                print('Ricardito pede um pedaço do teu lanche, você dá?')
                while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade
                                popularidade = popularidade -20
                                notas = notas
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.append('S1')
                                break
                        elif resposta.startswith('nao'):
                                sanidade = sanidade
                                popularidade = popularidade + 20
                                notas = notas
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.remove('S1')
                                break
                        else:
                                print('digita direito capeta')
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
        elif sorteio == 'N3':
                print('Sei lá')
                while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas + 20
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.append('S1')
                                break
                        elif resposta.startswith('nao'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas + 20
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.remove('S1')
                                break
                        else:
                                print('digita direito capeta')
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
        elif sorteio == 'S1':
                print('Especial')
                while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas + 20
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.append('S1')
                                break
                        elif resposta.startswith('nao'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas + 20
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.remove('S1')
                                break
                        else:
                                print('digita direito capeta')
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))



print ('perdeu otario')
print (senarios)