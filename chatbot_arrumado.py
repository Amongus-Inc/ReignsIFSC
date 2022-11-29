#versão onde ele não escolhe o mesmo cenario após a morte (de verdade dessa vez)
from definições_avançado import estados, canais_de_voz
import discord
from discord.ext import commands
from random import choice
import random
from re import fullmatch
from os import getenv
from os.path import exists
from dotenv import load_dotenv
import pymongo

load_dotenv()

usuario = getenv('MONGODB_USERNAME', default='')
senha = getenv('MONGODB_PASSWORD', default='')
cluster = getenv('MONGODB_CLUSTER', default='')
uri = ''.join(['mongodb+srv://', usuario, ':', senha, '@', cluster, '/?retryWrites=true&w=majority'])
mongo_client = pymongo.MongoClient(uri)
database = mongo_client.chatbot

partidas_db = database.partidas

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return

    autor = msg.author.id

    if msg.content.startswith('$'):
        pass
    else:
        return

    mensagem = msg.content.strip()[1:]

    if fullmatch('jogu tchubaron [rR]einiciar', mensagem):
        partidas_db.find_one_and_delete({'jogador': autor})
        await msg.channel.send('Jogo reiniciado (progresso do jogador apagado).')
        return

    if fullmatch('jogu tchubaron [sS]ai', mensagem):
        [await canais_de_voz[i].disconnect() for i in canais_de_voz.keys()]
        await msg.channel.send('Saindo do canal de voz')
        return

    if partidas_db.count_documents({'jogador': autor}) == 0:
        partidas_db.insert_one({'jogador': autor, 'partida': 2050, 'status': {'Sanidade': 50, 'Popularidade': 50, 'Notas': 50, 'Inteligência': 50}, 'cenarios': [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 'estado_anterior_aleatorio': 9000})
    
    partida = partidas_db.find_one({'jogador': autor})

    if msg.channel.type.name == 'private':
        if partida['partida'] == 2050:
            await msg.channel.send('Não é possível reproduzir áudio em canais privados. \n Por favor, esteja em um canal de voz para ter a imersão completa do jogo.')

    if msg.channel.type.name != 'private':
        if msg.author.voice:
            if msg.guild.me not in msg.author.voice.channel.members:
                canais_de_voz[autor] = await msg.author.voice.channel.connect()
        else:
            await msg.channel.send('Por favor, esteja em um canal de voz para ter a imersão completa do jogo.')
            return

    estado_do_jogador = estados[partida['partida']]
    senarios = partida['cenarios']
    anterior = 8000
    Sanidade = partida['status']['Sanidade']
    Popularidade = partida['status']['Popularidade']
    Notas = partida['status']['Notas']
    Inteligência = partida['status']['Inteligência']
    for key, value in estado_do_jogador['positivo_proximos_estados'].items():
        if fullmatch(key, msg.content):            
            await msg.channel.send(estado_do_jogador['frases_positivas'])                
            appender = estado_do_jogador['append_positivo']
            remover = estado_do_jogador['remove_positivo']
            if appender != 8000 and appender not in senarios and appender in estados:
                senarios.append(appender)
            if remover != 8000 and remover in senarios: #and remover_positivo in estados(?)
                senarios.remove(remover)
            if estado_do_jogador['positivos_sanidade'] != 0:
                Sanidade = partida['status']['Sanidade'] + int(estado_do_jogador['positivos_sanidade'])
            if estado_do_jogador['positivos_popularidade'] != 0:
                Popularidade = partida['status']['Popularidade'] + int(estado_do_jogador['positivos_popularidade'])
            if estado_do_jogador['positivos_notas'] != 0:
                Notas = partida['status']['Notas'] + int(estado_do_jogador['positivos_notas'])
            if estado_do_jogador['positivos_inteligência'] != 0:
                Inteligência = partida['status']['Inteligência'] + int(estado_do_jogador['positivos_inteligência'])
            if Sanidade <= 0:
                numero = 0           
            elif Sanidade >= 100:
                numero = 1          
            elif Popularidade <= 0:
                numero = 2           
            elif Popularidade >= 100:
                numero = 3        
            elif Notas <= 0:
                numero = 4         
            elif Notas >= 100:
                numero = 5       
            elif Inteligência <= 0:
                numero = 6  
            elif Inteligência >= 100:
                numero = 7
            if Inteligência in range(1, 100) and Notas in range(1, 100) and Popularidade in range(1, 100) and Sanidade in range(1, 100):
                if value == 2060:
                    Sanidade = 50
                    Popularidade = 50
                    Notas = 50
                    Inteligência = 50
                await msg.channel.send('[Sanidade: ' + str(Sanidade) + ', Popularidade: ' + str(Popularidade) + ', Notas: ' + str(Notas) + ', Inteligência: ' + str(Inteligência) + ']')
                if value != 8000:                   
                    numero = value
                else:
                    copia = senarios.copy()
                    if partida['estado_anterior_aleatorio'] in copia:
                        copia.remove(partida['estado_anterior_aleatorio'])
                    flip = random.choice(copia)
                    numero = flip
                    anterior = flip                                                                         
            if numero in range(0, 16):
                Sanidade = 50
                Popularidade = 50
                Notas = 50
                Inteligência = 50
            if anterior != 8000:
                if appender != 8000 or remover != 8000:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}, 'cenarios': senarios, 'estado_anterior_aleatorio': anterior}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
                else:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}, 'estado_anterior_aleatorio': anterior}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
            else:
                if appender != 8000 or remover != 8000:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}, 'cenarios': senarios}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
                else:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
            await msg.channel.send(choice(estados[numero]['frases']))
            if msg.channel.type.name != 'private':
                arquivo_de_som = str(numero) + '.mp3'
                if exists(arquivo_de_som):
                    som_opus = await discord.FFmpegOpusAudio.from_probe(arquivo_de_som)
                    canais_de_voz[autor].play(som_opus)
            return
    for key, value in estado_do_jogador['negativa_proximos_estados'].items():
        if fullmatch(key, msg.content):            
            await msg.channel.send(estado_do_jogador['frases_negativas'])
            appender = estado_do_jogador['append_negativo']
            remover = estado_do_jogador['remove_negativo']
            if appender != 8000 and appender not in senarios and appender in estados:
                senarios.append(appender)
            if remover != 8000 and remover in senarios: #and remover_negativo in estados(?)
                senarios.remove(remover)
            if estado_do_jogador['negativos_sanidade'] != 0:
                Sanidade = partida['status']['Sanidade'] + int(estado_do_jogador['negativos_sanidade'])
            if estado_do_jogador['negativos_popularidade'] != 0:
                Popularidade = partida['status']['Popularidade'] + int(estado_do_jogador['negativos_popularidade'])
            if estado_do_jogador['negativos_notas'] != 0:
                Notas = partida['status']['Notas'] + int(estado_do_jogador['negativos_notas'])
            if estado_do_jogador['negativos_inteligência'] != 0:
                Inteligência = partida['status']['Inteligência'] + int(estado_do_jogador['negativos_inteligência'])
            if Sanidade <= 0:
                numero = 0           
            elif Sanidade >= 100:
                numero = 1          
            elif Popularidade <= 0:
                numero = 2           
            elif Popularidade >= 100:
                numero = 3        
            elif Notas <= 0:
                numero = 4         
            elif Notas >= 100:
                numero = 5       
            elif Inteligência <= 0:
                numero = 6  
            elif Inteligência >= 100:
                numero = 7
            if Inteligência in range(1, 100) and Notas in range(1, 100) and Popularidade in range(1, 100) and Sanidade in range(1, 100):
                if value == 2060:
                    Sanidade = 50
                    Popularidade = 50
                    Notas = 50
                    Inteligência = 50
                await msg.channel.send('[Sanidade: ' + str(Sanidade) + ', Popularidade: ' + str(Popularidade) + ', Notas: ' + str(Notas) + ', Inteligência: ' + str(Inteligência) + ']')
                if value != 8000:                   
                    numero = value
                else:
                    copia = senarios.copy()
                    if partida['estado_anterior_aleatorio'] in copia:
                        copia.remove(partida['estado_anterior_aleatorio'])
                    flip = random.choice(copia)
                    numero = flip
                    anterior = flip                                                                         
            if numero in range(0, 16):
                Sanidade = 50
                Popularidade = 50
                Notas = 50
                Inteligência = 50
            if anterior != 8000:
                if appender != 8000 or remover != 8000:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}, 'cenarios': senarios, 'estado_anterior_aleatorio': anterior}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
                else:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}, 'estado_anterior_aleatorio': anterior}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
            else:
                if appender != 8000 or remover != 8000:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}, 'cenarios': senarios}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
                else:
                    partida = partidas_db.find_one_and_update(
                        {'jogador': autor},
                        {'$set': {'partida': numero, 'status': {'Sanidade': Sanidade, 'Popularidade': Popularidade, 'Notas': Notas, 'Inteligência': Inteligência}}},
                        return_document=pymongo.ReturnDocument.AFTER
                    )
            await msg.channel.send(choice(estados[numero]['frases']))
            if msg.channel.type.name != 'private':
                arquivo_de_som = str(numero) + '.mp3'
                if exists(arquivo_de_som):
                    som_opus = await discord.FFmpegOpusAudio.from_probe(arquivo_de_som)
                    canais_de_voz[autor].play(som_opus)
            return
    if partida['partida'] >= 16 and msg.content.startswith('$socorro'):        
        await msg.channel.send('[Sanidade: ' + str(Sanidade) + ', Popularidade: ' + str(Popularidade) + ', Notas: ' + str(Notas) + ', Inteligência: ' + str(Inteligência) + '] \n' + choice(estados[partida['partida']]['frases']))
        return
    elif partida['partida'] >= 16 and msg.content.startswith('$'):
        await msg.channel.send('Digite \$socorro para receber ajuda')
        return

bot.run(getenv('DISCORD_TOKEN'))

#if fato_do_jogador['cenarios'] != senarios:
#    fatos[autor]['cenarios'] = senarios

#copia = senarios[:]
#ou
#copia = senarios.copy()