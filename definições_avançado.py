# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['morte sanidade baixa estado0 suicidio'],
        'frases_positivas': 'recomeçando jogo',
        'frases_negativas': 'recomeçando jogo',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000           
    },
    1: {
        'frases': ['morte sanidade alta estado1'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    2: {
        'frases': ['morte popularidade baixa estado2'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    3: {
        'frases': ['morte popularidade alta estado3'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    4: {
        'frases': ['morte notas baixa estado4'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    5: {
        'frases': ['morte notas alta estado5'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    6: {
        'frases': ['morte inteligência baixa estado6'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    7: {
        'frases': ['morte inteligência alta estado7'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[oO] que': 8000},               #usar 8000 para o proximo cenario ser aleatorio
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000             
    },
    8: {
        'frases': ['Ricardito quer se lanche você dá? cenario8'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 25, 
        'positivos_popularidade': 25,
        'positivos_notas': 25,
        'positivos_inteligência': 25,
        'negativos_sanidade': 25, 
        'negativos_popularidade': 25,
        'negativos_notas': 25,
        'negativos_inteligência': 25,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },
    9: {
        'frases': ['Você quer participar da aula do Carlyle? cenario9'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 25, 
        'positivos_popularidade': 25,
        'positivos_notas': 25,
        'positivos_inteligência': 25,
        'negativos_sanidade': 25, 
        'negativos_popularidade': 25,
        'negativos_notas': 25,
        'negativos_inteligência': 25,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 8000
        },
        'append_positivo': 10,
        'append_negativo': 10,
        'remove_positivo': 9,
        'remove_negativo': 9
        
    },
    10: {
        'frases': ['Ficar intêligente? cenario10'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 25,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': -25,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },
    2048: {
        'frases': ['Você têm certeza? continuação1, estado2048'],
        'frases_positivas': 'isso não é muito legal',
        'frases_negativas': 'descisão certa, ganha respeito',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$[sS](i)+m': 8000},
        'negativa_proximos_estados': {
            '\$[nN][aã]+o': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
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
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
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
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
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
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    }
}

# Dicionário com os estados correntes de cada jogador.
fatos = {}

#reservar 0-15 para derrotas
#reservar 16-31 (quanto prescisar)
#cenarios mormais 32-1023
#cenarios historias 1024-2047
#cenarios de continuação 2048-3000