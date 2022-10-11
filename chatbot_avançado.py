from definições_avançado import estados, fatos
import discord
from discord.ext import commands
from random import choice
import random
from re import fullmatch
from os import getenv
from dotenv import load_dotenv
load_dotenv()

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
    if autor not in fatos:
        fatos[autor] = {
            'partida': 9,
            'status': {'Sanidade': 50,
            'Popularidade': 50,
            'Notas': 50,
            'Inteligência': 50
            },
            'cenarios': [8, 9],
            'vividos': 0,
            'recorde': 0,
            'estado_anterior_aleatorio': 9000
        }

    estado_do_jogador = estados[fatos[autor]['partida']]
    fato_do_jogador = fatos[autor]
    estado_anterior = fato_do_jogador['partida']
    status_sanidade = fato_do_jogador['status']['Sanidade']
    status_popularidade = fato_do_jogador['status']['Popularidade']
    status_notas = fato_do_jogador['status']['Notas']
    status_inteligencia = fato_do_jogador['status']['Inteligência']
    for key, value in estado_do_jogador['positivo_proximos_estados'].items():
        if fullmatch(key, msg.content):            
            await msg.channel.send(estado_do_jogador['frases_positivas'])
            senarios = fato_do_jogador['cenarios']
            appender_positivo = estado_do_jogador['append_positivo']
            remover_positivo = estado_do_jogador['remove_positivo']
            if appender_positivo != 8000:
                if appender_positivo not in senarios:
                    senarios.append(appender_positivo)
            if remover_positivo != 8000:
                if remover_positivo in senarios:
                    senarios.remove(remover_positivo)
            fatos[autor]['cenarios'] = senarios
            fatos[autor]['status']['Sanidade'] = status_sanidade + int(estado_do_jogador['positivos_sanidade'])
            fatos[autor]['status']['Popularidade'] = status_popularidade + int(estado_do_jogador['positivos_popularidade'])
            fatos[autor]['status']['Notas'] = status_notas + int(estado_do_jogador['positivos_notas'])
            fatos[autor]['status']['Inteligência'] = status_inteligencia + int(estado_do_jogador['positivos_inteligência'])
            fato_do_jogador = fatos[autor]
            if fato_do_jogador['status']['Sanidade'] <= 0:
                fatos[autor]['partida'] = 0
                fato_do_jogador = fatos[autor]               
            elif fato_do_jogador['status']['Sanidade'] >= 100:
                fatos[autor]['partida'] = 1
                fato_do_jogador = fatos[autor]              
            elif fato_do_jogador['status']['Popularidade'] <= 0:
                fatos[autor]['partida'] = 2
                fato_do_jogador = fatos[autor]               
            elif fato_do_jogador['status']['Popularidade'] >= 100:
                fatos[autor]['partida'] = 3
                fato_do_jogador = fatos[autor]               
            elif fato_do_jogador['status']['Notas'] <= 0:
                fatos[autor]['partida'] = 4
                fato_do_jogador = fatos[autor]                
            elif fato_do_jogador['status']['Notas'] >= 100:
                fatos[autor]['partida'] = 5
                fato_do_jogador = fatos[autor]                
            elif fato_do_jogador['status']['Inteligência'] <= 0:
                fatos[autor]['partida'] = 6
                fato_do_jogador = fatos[autor]               
            elif fato_do_jogador['status']['Inteligência'] >= 100:
                fatos[autor]['partida'] = 7
                fato_do_jogador = fatos[autor]
            if fato_do_jogador['partida'] in range(0, 8):
                fatos[autor]['status']['Sanidade'] = 50
                fatos[autor]['status']['Popularidade'] = 50
                fatos[autor]['status']['Notas'] = 50
                fatos[autor]['status']['Inteligência'] = 50
                fatos[autor]['vividos'] = fato_do_jogador['vividos'] - 1
                fato_do_jogador = fatos[autor]
                if fato_do_jogador['recorde'] < fato_do_jogador['vividos']:
                    fatos[autor]['recorde'] = fato_do_jogador['vividos']
                fatos[autor]['vividos'] = 0
            else:
                await msg.channel.send(fatos[autor]['status'])
                if value != 8000:
                    if fato_do_jogador['partida'] not in range(2048, 3001):
                        fatos[autor]['estado_anterior_aleatorio'] = fatos[autor]['partida']                    
                    fatos[autor]['partida'] = value
                    fato_do_jogador = fatos[autor]
                else:
                    if estado_anterior not in range(0, 8):
                        fatos[autor]['vividos'] = fato_do_jogador['vividos'] + 1
                    if estado_anterior not in range(2048, 3001):
                        fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                        fato_do_jogador = fatos[autor]
                    flip = fato_do_jogador['estado_anterior_aleatorio']
                    while fato_do_jogador['estado_anterior_aleatorio'] == flip:
                        flip = random.choice(senarios)
                    fatos[autor]['partida'] = flip
                    fato_do_jogador = fatos[autor]
            estado_do_jogador = estados[fatos[autor]['partida']]
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return    

    for key, value in estado_do_jogador['negativa_proximos_estados'].items():
        if fullmatch(key, msg.content):            
            await msg.channel.send(estado_do_jogador['frases_negativas'])
            senarios = fato_do_jogador['cenarios']
            appender_negativo = estado_do_jogador['append_negativo']
            remover_negativo = estado_do_jogador['remove_negativo']
            if appender_negativo != 8000:
                if appender_negativo not in senarios:
                    senarios.append(appender_negativo)
            if remover_negativo != 8000:
                if remover_negativo in senarios:
                    senarios.remove(remover_negativo)
            fatos[autor]['cenarios'] = senarios
            fatos[autor]['status']['Sanidade'] = status_sanidade + int(estado_do_jogador['negativos_sanidade'])
            fatos[autor]['status']['Popularidade'] = status_popularidade + int(estado_do_jogador['negativos_popularidade'])
            fatos[autor]['status']['Notas'] = status_notas + int(estado_do_jogador['negativos_notas'])
            fatos[autor]['status']['Inteligência'] = status_inteligencia + int(estado_do_jogador['negativos_inteligência'])
            if value != 8000:
                if fato_do_jogador['partida'] not in range(2048, 3001):
                    fatos[autor]['estado_anterior_aleatorio'] = fatos[autor]['partida']
                fatos[autor]['partida'] = value
            else:
                fatos[autor]['vividos'] = fatos[autor]['vividos'] + 1
                fatos[autor]['estado_anterior'] = fatos[autor]['partida']
                if fatos[autor]['estado_anterior'] in range(0, 8):
                    fatos[autor]['vividos'] = fatos[autor]['vividos'] - 1
                else:
                    if fatos[autor]['estado_anterior'] not in range(2048, 3001):
                        fatos[autor]['estado_anterior_aleatorio'] = fatos[autor]['partida']
                moeda = fatos[autor]['estado_anterior_aleatorio']
                while fatos[autor]['estado_anterior_aleatorio'] == moeda:
                    moeda = random.choice(senarios)
                fatos[autor]['partida'] = moeda         
            if fatos[autor]['status']['Sanidade'] <= 0:
                fatos[autor]['partida'] = 0                
            elif fatos[autor]['status']['Sanidade'] >= 100:
                fatos[autor]['partida'] = 1                
            elif fatos[autor]['status']['Popularidade'] <= 0:
                fatos[autor]['partida'] = 2                
            elif fatos[autor]['status']['Popularidade'] >= 100:
                fatos[autor]['partida'] = 3               
            elif fatos[autor]['status']['Notas'] <= 0:
                fatos[autor]['partida'] = 4                
            elif fatos[autor]['status']['Notas'] >= 100:
                fatos[autor]['partida'] = 5                
            elif fatos[autor]['status']['Inteligência'] <= 0:
                fatos[autor]['partida'] = 6                
            elif fatos[autor]['status']['Inteligência'] >= 100:
                fatos[autor]['partida'] = 7
            if fatos[autor]['partida'] in range(0, 8):
                fatos[autor]['status']['Sanidade'] = 50
                fatos[autor]['status']['Popularidade'] = 50
                fatos[autor]['status']['Notas'] = 50
                fatos[autor]['status']['Inteligência'] = 50
                fatos[autor]['vividos'] = fatos[autor]['vividos'] - 1
                if fatos[autor]['recorde'] < fatos[autor]['vividos']:
                    fatos[autor]['recorde'] = fatos[autor]['vividos']
                fatos[autor]['vividos'] = 0
            else:
                await msg.channel.send(fatos[autor]['status'])            
            estado_do_jogador = estados[fatos[autor]['partida']]
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return
    if fatos[autor]['partida'] >= 8 and msg.content.startswith('$socorro'):        
        await msg.channel.send(fatos[autor]['status'])
        await msg.channel.send(choice(estado_do_jogador['frases']))
        return
    if fatos[autor]['partida'] >= 8 and msg.content.startswith('$recorde'):
        await msg.channel.send(fatos[autor]['recorde'])
        return
    elif fatos[autor]['partida'] >= 8 and msg.content.startswith('$'):
        await msg.channel.send('Digite \$socorro para receber ajuda')
        await msg.channel.send('Digite \$recorde para receber seu recorde de cenarios sobreviviods')
        return

bot.run(getenv('DISCORD_TOKEN'))

