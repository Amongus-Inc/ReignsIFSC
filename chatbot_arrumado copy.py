#versão onde ele não escolhe o mesmo cenario após a morte
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
    if msg.content.startswith('$'):
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
                'estado_anterior_aleatorio': 9000
            }
        
        fato_do_jogador = fatos[autor]
        estado_do_jogador = estados[fato_do_jogador['partida']]
        estado_anterior = fato_do_jogador['partida']
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
                if fato_do_jogador['cenarios'] != senarios:
                    fatos[autor]['cenarios'] = senarios
                if estado_do_jogador['positivos_sanidade'] != 0:
                    fatos[autor]['status']['Sanidade'] = fato_do_jogador['status']['Sanidade'] + int(estado_do_jogador['positivos_sanidade'])
                if estado_do_jogador['positivos_popularidade'] != 0:
                    fatos[autor]['status']['Popularidade'] = fato_do_jogador['status']['Popularidade'] + int(estado_do_jogador['positivos_popularidade'])
                if estado_do_jogador['positivos_notas'] != 0:
                    fatos[autor]['status']['Notas'] = fato_do_jogador['status']['Notas'] + int(estado_do_jogador['positivos_notas'])
                if estado_do_jogador['positivos_inteligência'] != 0:
                    fatos[autor]['status']['Inteligência'] = fato_do_jogador['status']['Inteligência'] + int(estado_do_jogador['positivos_inteligência'])
                fato_do_jogador = fatos[autor]
                if fato_do_jogador['status']['Sanidade'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 0
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Sanidade'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 1
                    fato_do_jogador = fatos[autor]              
                elif fato_do_jogador['status']['Popularidade'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 2
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Popularidade'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 3
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Notas'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 4
                    fato_do_jogador = fatos[autor]                
                elif fato_do_jogador['status']['Notas'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 5
                    fato_do_jogador = fatos[autor]                
                elif fato_do_jogador['status']['Inteligência'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 6
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Inteligência'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 7
                    fato_do_jogador = fatos[autor]
                if fato_do_jogador['status']['Inteligência'] in range(1, 100) and fato_do_jogador['status']['Notas'] in range(1, 100) and fato_do_jogador['status']['Popularidade'] in range(1, 100) and fato_do_jogador['status']['Sanidade'] in range(1, 100):
                    await msg.channel.send(fatos[autor]['status'])
                    if value != 8000:
                        if fato_do_jogador['partida'] not in range(2048, 3001):
                            fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']                    
                        fatos[autor]['partida'] = value
                        fato_do_jogador = fatos[autor]
                    else:
                        if estado_anterior not in range(2048, 3001) and estado_anterior not in range(0, 8):
                            fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                            fato_do_jogador = fatos[autor]
                        flip = fato_do_jogador['estado_anterior_aleatorio']
                        while fato_do_jogador['estado_anterior_aleatorio'] == flip:
                            flip = random.choice(senarios)
                        fatos[autor]['partida'] = flip
                        fato_do_jogador = fatos[autor]                                                                            
                if fato_do_jogador['partida'] in range(0, 8):
                    fatos[autor]['status']['Sanidade'] = 50
                    fatos[autor]['status']['Popularidade'] = 50
                    fatos[autor]['status']['Notas'] = 50
                    fatos[autor]['status']['Inteligência'] = 50
                    fato_do_jogador = fatos[autor]
                estado_do_jogador = estados[fato_do_jogador['partida']]
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
                if fato_do_jogador['cenarios'] != senarios:
                    fatos[autor]['cenarios'] = senarios
                if estado_do_jogador['negativos_sanidade'] != 0:
                    fatos[autor]['status']['Sanidade'] = fato_do_jogador['status']['Sanidade'] + int(estado_do_jogador['negativos_sanidade'])
                if estado_do_jogador['negativos_popularidade'] != 0:
                    fatos[autor]['status']['Popularidade'] = fato_do_jogador['status']['Popularidade'] + int(estado_do_jogador['negativos_popularidade'])
                if estado_do_jogador['negativos_notas'] != 0:
                    fatos[autor]['status']['Notas'] = fato_do_jogador['status']['Notas'] + int(estado_do_jogador['negativos_notas'])
                if estado_do_jogador['negativos_inteligência'] != 0:
                    fatos[autor]['status']['Inteligência'] = fato_do_jogador['status']['Inteligência'] + int(estado_do_jogador['negativos_inteligência'])
                fato_do_jogador = fatos[autor]
                if fato_do_jogador['status']['Sanidade'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 0
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Sanidade'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 1
                    fato_do_jogador = fatos[autor]              
                elif fato_do_jogador['status']['Popularidade'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 2
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Popularidade'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 3
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Notas'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 4
                    fato_do_jogador = fatos[autor]                
                elif fato_do_jogador['status']['Notas'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 5
                    fato_do_jogador = fatos[autor]                
                elif fato_do_jogador['status']['Inteligência'] <= 0:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 6
                    fato_do_jogador = fatos[autor]               
                elif fato_do_jogador['status']['Inteligência'] >= 100:
                    fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                    fatos[autor]['partida'] = 7
                    fato_do_jogador = fatos[autor]
                if fato_do_jogador['status']['Inteligência'] in range(1, 100) and fato_do_jogador['status']['Notas'] in range(1, 100) and fato_do_jogador['status']['Popularidade'] in range(1, 100) and fato_do_jogador['status']['Sanidade'] in range(1, 100):
                    await msg.channel.send(fatos[autor]['status'])
                    if value != 8000:
                        if fato_do_jogador['partida'] not in range(2048, 3001):
                            fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']                    
                        fatos[autor]['partida'] = value
                        fato_do_jogador = fatos[autor]
                    else:
                        if estado_anterior not in range(2048, 3001) and estado_anterior not in range(0, 8):
                            fatos[autor]['estado_anterior_aleatorio'] = fato_do_jogador['partida']
                            fato_do_jogador = fatos[autor]
                        flip = fato_do_jogador['estado_anterior_aleatorio']
                        while fato_do_jogador['estado_anterior_aleatorio'] == flip:
                            flip = random.choice(senarios)
                        fatos[autor]['partida'] = flip
                        fato_do_jogador = fatos[autor]                                                                            
                if fato_do_jogador['partida'] in range(0, 8):
                    fatos[autor]['status']['Sanidade'] = 50
                    fatos[autor]['status']['Popularidade'] = 50
                    fatos[autor]['status']['Notas'] = 50
                    fatos[autor]['status']['Inteligência'] = 50
                    fato_do_jogador = fatos[autor]
                estado_do_jogador = estados[fato_do_jogador['partida']]
                await msg.channel.send(choice(estado_do_jogador['frases']))
                return
        if fato_do_jogador['partida'] >= 8 and msg.content.startswith('$socorro'):        
            await msg.channel.send(fato_do_jogador['status'])
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return
        elif fato_do_jogador['partida'] >= 8 and msg.content.startswith('$'):
            await msg.channel.send('Digite \$socorro para receber ajuda')
            return

bot.run(getenv('DISCORD_TOKEN'))

