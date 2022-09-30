from definições import estados, partidas, status_dos_jogadores
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
    autor = msg.author.id
    if autor == bot.application_id:
        return
    if autor not in partidas:
        partidas[autor] = 8
        status_dos_jogadores[autor] = {
            'Sanidade': 50,
            'Popularidade': 50,
            'Notas': 50,
            'Inteligência': 50
        }
    estado_do_jogador = estados[partidas[autor]]
    status_sanidade = status_dos_jogadores[autor]['Sanidade']
    status_popularidade = status_dos_jogadores[autor]['Popularidade']
    status_notas = status_dos_jogadores[autor]['Notas']
    status_inteligencia = status_dos_jogadores[autor]['Inteligência']
    for key, value in estado_do_jogador['positivo_proximos_estados'].items():
        if fullmatch(key, msg.content):            
            await msg.channel.send(estado_do_jogador['frases_positivas'])
            status_dos_jogadores[autor]['Sanidade'] = status_sanidade + int(estado_do_jogador['positivos_sanidade'])
            status_dos_jogadores[autor]['Popularidade'] = status_popularidade + int(estado_do_jogador['positivos_popularidade'])
            status_dos_jogadores[autor]['Notas'] = status_notas + int(estado_do_jogador['positivos_notas'])
            status_dos_jogadores[autor]['Inteligência'] = status_inteligencia + int(estado_do_jogador['positivos_inteligência'])            
            if partidas[autor] == 0 or partidas[autor] == 1 or partidas[autor] == 2 or partidas[autor] == 3 or partidas[autor] == 4 or partidas[autor] == 5 or partidas[autor] == 6 or partidas[autor] == 7:
                status_dos_jogadores[autor]['Sanidade'] = 50
                status_dos_jogadores[autor]['Popularidade'] = 50
                status_dos_jogadores[autor]['Notas'] = 50
                status_dos_jogadores[autor]['Inteligência'] = 50
                if value != 8000:
                    partidas[autor] = value
                    estado_do_jogador = estados[partidas[autor]]
                else:
                    estado_anterior = partidas[autor]
                    moeda = estado_anterior
                    while estado_anterior == moeda:
                        moeda = random.randint(8, 9)
                    partidas[autor] = moeda
                    flip = random.randint(15, 16)#fazer ficar 1 à 25
                    if flip == 17:
                        partidas[autor] = random.randint(2048, 2051)
            elif status_dos_jogadores[autor]['Sanidade'] <= 0:
                partidas[autor] = 0                
            elif status_dos_jogadores[autor]['Sanidade'] >= 100:
                partidas[autor] = 1                
            elif status_dos_jogadores[autor]['Popularidade'] <= 0:
                partidas[autor] = 2                
            elif status_dos_jogadores[autor]['Popularidade'] >= 100:
                partidas[autor] = 3               
            elif status_dos_jogadores[autor]['Notas'] <= 0:
                partidas[autor] = 4                
            elif status_dos_jogadores[autor]['Notas'] >= 100:
                partidas[autor] = 5                
            elif status_dos_jogadores[autor]['Inteligência'] <= 0:
                partidas[autor] = 6                
            elif status_dos_jogadores[autor]['Inteligência'] >= 100:
                partidas[autor] = 7
            else:
                await msg.channel.send(status_dos_jogadores[autor])            
                if value != 8000:
                    partidas[autor] = value
                    estado_do_jogador = estados[partidas[autor]]
                else:
                    estado_anterior = partidas[autor]
                    moeda = estado_anterior
                    while estado_anterior == moeda:
                        moeda = random.randint(8, 9)
                    partidas[autor] = moeda
                    flip = random.randint(15, 16)#fazer ficar 1 à 25
                    if flip == 17:
                        partidas[autor] = random.randint(2048, 2051)
            estado_do_jogador = estados[partidas[autor]]
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return
    for key, value in estado_do_jogador['negativa_proximos_estados'].items():
        if fullmatch(key, msg.content):            
            await msg.channel.send(estado_do_jogador['frases_negativas'])
            status_dos_jogadores[autor]['Sanidade'] = status_sanidade + int(estado_do_jogador['negativos_sanidade'])
            status_dos_jogadores[autor]['Popularidade'] = status_popularidade + int(estado_do_jogador['negativos_popularidade'])
            status_dos_jogadores[autor]['Notas'] = status_notas + int(estado_do_jogador['negativos_notas'])
            status_dos_jogadores[autor]['Inteligência'] = status_inteligencia + int(estado_do_jogador['negativos_inteligência'])
            if partidas[autor] == 0 or partidas[autor] == 1 or partidas[autor] == 2 or partidas[autor] == 3 or partidas[autor] == 4 or partidas[autor] == 5 or partidas[autor] == 6 or partidas[autor] == 7:
                status_dos_jogadores[autor]['Sanidade'] = 50
                status_dos_jogadores[autor]['Popularidade'] = 50
                status_dos_jogadores[autor]['Notas'] = 50
                status_dos_jogadores[autor]['Inteligência'] = 50
                if value != 8000:
                    partidas[autor] = value
                    estado_do_jogador = estados[partidas[autor]]
                else:
                    estado_anterior = partidas[autor]
                    moeda = estado_anterior
                    while estado_anterior == moeda:
                        moeda = random.randint(8, 9)
                    partidas[autor] = moeda
                    flip = random.randint(15, 16)#fazer ficar 1 à 25
                    if flip == 17:
                        partidas[autor] = random.randint(2048, 2051)
            elif status_dos_jogadores[autor]['Sanidade'] <= 0:
                partidas[autor] = 0                
            elif status_dos_jogadores[autor]['Sanidade'] >= 100:
                partidas[autor] = 1                
            elif status_dos_jogadores[autor]['Popularidade'] <= 0:
                partidas[autor] = 2                
            elif status_dos_jogadores[autor]['Popularidade'] >= 100:
                partidas[autor] = 3                
            elif status_dos_jogadores[autor]['Notas'] <= 0:
                partidas[autor] = 4                
            elif status_dos_jogadores[autor]['Notas'] >= 100:
                partidas[autor] = 5               
            elif status_dos_jogadores[autor]['Inteligência'] <= 0:
                partidas[autor] = 6                
            elif status_dos_jogadores[autor]['Inteligência'] >= 100:
                partidas[autor] = 7
            else:
                await msg.channel.send(status_dos_jogadores[autor])            
                if value != 8000:
                    partidas[autor] = value
                    estado_do_jogador = estados[partidas[autor]]
                else:
                    estado_anterior = partidas[autor]
                    moeda = estado_anterior
                    while estado_anterior == moeda:
                        moeda = random.randint(8, 9)
                    partidas[autor] = moeda
                    flip = random.randint(15, 16)#fazer ficar 1 à 25
                    if flip == 17:
                        partidas[autor] = random.randint(2048, 2051)
            estado_do_jogador = estados[partidas[autor]]
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return
    if partidas[autor] >= 8 and msg.content.startswith('$socorro'):
        await msg.channel.send(choice(estado_do_jogador['frases']))
        await msg.channel.send(status_dos_jogadores[autor])
    elif partidas[autor] >= 8 and msg.content.startswith('$'):
        await msg.channel.send('Digite \$socorro para receber ajuda')


bot.run(getenv('DISCORD_TOKEN'))