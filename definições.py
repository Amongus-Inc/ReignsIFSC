# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['Ricardito quer parte do teu lanche, você dá\? estado0'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 20,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 7
        }             
    },
    1: {
        'frases': ['estado1'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
    },
    2: {
        'frases': ['estado2'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
    },
    3: {
        'frases': ['estado3'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }

    },
    7: {
        'frases': ['estado7'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
        
    },
    2048: {
        'frases': ['estado2048'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
    },
    2049: {
        'frases': ['estado2049'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
    },    
    2050: {
        'frases': ['estado2050'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
    },    
    2051: {
        'frases': ['estado2051'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': -30, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 30, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 2
        }
    }
}

# Dicionário com os estados correntes de cada jogador.
partidas = {}
status_dos_jogadores = {}

#reservar 0-15 para derrotas
#reservar 16-31 (quanto prescisar)
#cenarios mormais 32-1023
#cenarios de continuação 1024-2047
#cenarios historias 2048-3000
#fazer um dicionario com cada autor e uma lista dos cenarios que podem ser sorteados e também fazer o sistema de mortes
