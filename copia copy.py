from os import getenv
from dotenv import load_dotenv
import discord
from discord.ext import commands
from random import choice
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')



# Dicionário com as definições da máquina de estados do jogo.
estados = {
    0: {
        'frases': ['Ricardito quer parte do teu lanche, você dá?'],
        'frases_positivas': ['isso não é muito legal'],
        'frases_negativas': ['descisão certa, ganha respeito'],
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'nagativos_notas': 0,
        'negativos_inteligência': 0,
        'proximos_estados': {
            'sim': 1,
            'nao': 2
        }
    },
    1: {
        'frases': ['Olá!', 'Tudo bem, como vai?'],
        'proximos_estados': {
            'sim': 2,
            'não': 3
        }
    },
    2: {
        'frases': ['Era uma vez...', 'E lá de volta outra vez...'],
        'proximos_estados': {
            'não': 3
        }
    },
    3: {
        'frases': ['Fim do jogo!', 'Parabéns!'],
        'proximos_estados': {}
    }
}

# Dicionário com os estados correntes de cada jogador.
estados_dos_jogadores = {}
status_dos_jogadores = {}

@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    # Verificar se a mensagem não tem o próprio bot como autor.
    if msg.author.id == msg.channel.me.id:
        return

    # Verificar se o jogador ainda não começou a partida,
    # o que significa que precisa colocá-lo no estado zero (0).
    if msg.author.id not in estados_dos_jogadores:
        estados_dos_jogadores[msg.author.id] = 0
        status_dos_jogadores[msg.author.id] = {
            'sanidade': 50,
            'popularidade': 50,
            'notas': 50,
            'inteligência': 50
        }


    # Em ordem de operação:
    # 0) Obter o ID do jogador:
    #    msg.author.id
    # 1) Obter o estado atual do jogador:
    #    estados_dos_jogadores[msg.author.id]
    # 2) Obter a definição completa desse estado:
    #    estados[estados_dos_jogadores[msg.author.id]]
    # 3) Filtrar desse estado apenas a lista de próximos estados:
    #    estados[estados_dos_jogadores[msg.author.id]]['proximos_estados']
    # 4) Filtrar dessa lista as chaves (frases) quem levam a próximos estados:
    #    estados[estados_dos_jogadores[msg.author.id]]['proximos_estados'].keys()
    # 5) Verificar se a frase do usuário está na lista de chaves (frases) do estado:
    if msg.content in estados[estados_dos_jogadores[msg.author.id]]['proximos_estados'].keys():
        await msg.channel.send(choice(estados[estados_dos_jogadores[msg.author.id]]['frases_positivas']))
        
        await msg.channel.send(estados_dos_jogadores)
        await msg.channel.send(status_dos_jogadores)
        
        
        
        
        sanidade = sanidade + str(estados[estados_dos_jogadores[msg.author.id]]['positivos_sanidade'])
        popularidade = popularidade + str(estados[estados_dos_jogadores['estado'][msg.author.id]]['positivos_popularidade'])
        notas = notas + str(estados[estados_dos_jogadores[msg.author.id]]['positivos_notas'])
        inteligência = inteligência + str(estados[estados_dos_jogadores[msg.author.id]]['positivos_inteligência'])
        
        
        
        await msg.channel.send('Sanidade: ' + str(estados_dos_jogadores[msg.author.id]))
        await msg.channel.send('Popularidade: ' + estados_dos_jogadores[msg.author.id])
        await msg.channel.send('Notas: ' + str(notas))
        await msg.channel.send('Inteligência: ' + str(inteligência))



        sanidade = sanidade + str(estados[estados_dos_jogadores[msg.author.id]]['positivos_sanidade'])
        popularidade = popularidade + str(estados[estados_dos_jogadores['estado'][msg.author.id]]['positivos_popularidade'])
        notas = notas + str(estados[estados_dos_jogadores[msg.author.id]]['positivos_notas'])
        inteligência = inteligência + str(estados[estados_dos_jogadores[msg.author.id]]['positivos_inteligência'])
        await msg.channel.send('Sanidade: ' + str(sanidade))
        await msg.channel.send('Popularidade: ' + str(popularidade))
        await msg.channel.send('Notas: ' + str(notas))
        await msg.channel.send('Inteligência: ' + str(inteligência))





        # 6) Atualizar o estado do jogador, fazendo-o avançar no jogo:
        estados_dos_jogadores[msg.author.id] = estados[estados_dos_jogadores[msg.author.id]]['proximos_estados'][msg.content]
        #
        # 7) Enviar para o jogador a mensagem do estado (já atualizado)
        #
        # Em ordem de operação:
        # 7.0) Obter o ID do jogador:
        #    msg.author.id
        # 7.1) Obter o estado atual do jogador:
        #    estados_dos_jogadores[msg.author.id]
        # 7.2) Obter a definição completa desse estado:
        #    estados[estados_dos_jogadores[msg.author.id]]
        # 7.3) Filtrar desse estado apenas a lista de frases:
        #    estados[estados_dos_jogadores[msg.author.id]]['frases']
        # 7.4) Sortear uma frase dessa lista:
        #   choice(estados[estados_dos_jogadores[msg.author.id]]['frases'])
        await msg.channel.send(choice(estados[estados_dos_jogadores[msg.author.id]]['frases']))
    #
    # Caso contrário, avisar que a mensagem não avança no jogo
    else:
        #
        # Se o jogador está no primeiro estado...
        if estados_dos_jogadores[msg.author.id] == 0:
            #
            # ...ajudar com uma dica:
            await msg.channel.send(choice(estados[estados_dos_jogadores[msg.author.id]]['frases']))
        else:
            #
            # Nos estados seguintes, a resposta padrão de HAL:
            await msg.channel.send('I\'m sorry, I\'m afraid I can\'t do that.')
            #teste com o display_name

bot.run(getenv('DISCORD_TOKEN'))