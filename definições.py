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
            '[sS](i)+m': 0},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0                 #0 = igual a cenario duplo ou maior/1 = aleatorio
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0

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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
        
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
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
            '[sS](i)+m': 7},
        'negativa_proximos_estados': {
            '[nN][aã]+o': 2
        },
        '2_estapas': 0
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
