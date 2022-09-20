import random

#pesquisar sobre python dicionarios

ignorar_erros_ir_proximo_cenario = 1

sanidade = 50
popularidade = 50
notas = 50
inteligência = 50

senarios = ['N1', 'N2', 'N3']
#senario com s, é porque eu quero
#glosario 
#N = normal
#S = special
#H = historia (faça questão de ordenar esses cenarios na sua ordem que devem acontecer)
#adicione letras especificas para cenarios que serão adicionados a lista

#if mensagem do discord for iniciar o bagulho começa
while sanidade >= 0 and sanidade <= 100 and sanidade != 0 and sanidade != 100 and popularidade >= 0 and popularidade <= 100 and popularidade != 0 and popularidade != 100 and notas >= 0 and notas <= 100 and notas != 0 and notas != 100 and inteligência >= 0 and inteligência <= 100 and inteligência != 0 and inteligência != 100:
        print ('Novo cenário: ')
        sorteio = random.choice(senarios)
        if sorteio == 'N1':
                print('Você quer participar da aula do Carlyle?')
                while ignorar_erros_ir_proximo_cenario == 1:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade - 45
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
                                sanidade = sanidade + 450
                                popularidade = popularidade
                                notas = notas
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                if 'S1' in senarios:
                                        senarios.remove('S1')
                                break
                        else:
                                print('digita direito capeta')
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                
        elif sorteio == 'N2':
                print('Ricardito pede um pedaço do teu lanche, você dá?')
                while ignorar_erros_ir_proximo_cenario == 1:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade
                                popularidade = popularidade - 45
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
                                popularidade = popularidade + 450
                                notas = notas
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                if 'S1' in senarios:
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
                while ignorar_erros_ir_proximo_cenario == 1:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas - 45
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
                                notas = notas + 450
                                inteligência = inteligência
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                if 'S1' in senarios:
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
                while ignorar_erros_ir_proximo_cenario == 1:
                        resposta = input("Sua descisão: ")
                        if resposta.startswith('sim'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas
                                inteligência = inteligência - 45
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                senarios.append('S1')
                                break
                        elif resposta.startswith('nao'):
                                sanidade = sanidade
                                popularidade = popularidade
                                notas = notas
                                inteligência = inteligência + 450
                                print('Sanidade: ' + str(sanidade))
                                print('Popularidade: ' + str(popularidade))
                                print('Notas: ' + str(notas))
                                print('Inteligência: ' + str(inteligência))
                                if 'S1' in senarios:
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