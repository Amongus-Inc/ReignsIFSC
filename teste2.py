import random

sanidade = 50
popularidade = 50
notas = 50
inteligência = 50


print('Você quer participar da aula do Carlyle?')

resposta = input("Sua descisão: ")
# se lembrar de fazer o bagulho pra ele reconhecer letra maiuscula
while sanidade > 0:
    if resposta.startswith('sim'):
        sanidade = sanidade -7
    elif resposta.startswith('nao'):
        sanidade = sanidade +18
    else:
        print('digita direito capeta')
        #resolver isso depois



print('Sanidade: ' + str(sanidade))
print('Popularidade: ' + str(popularidade))
print('Notas: ' + str(notas))
print('Inteligência: ' + str(inteligência))
