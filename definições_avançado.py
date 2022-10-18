# Dicionário com as definições da máquina de estados do jogo.
# As opções dos jogadores são definidas como expressões regulares.
estados = {
    0: {
        'frases': ['Columbine.'],
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
        'frases': ['Você atingiu o nível máximo de sanidade e percebe que o ifsc não vale a pena e transcende para além de seu corpo físico.'],
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
    2: {
        'frases': ['Sua popularidade é tão baixa que você é isolado, entra em depressão e se mata.'],
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
    3: {
        'frases': ['Você é tão popular que começa a se relacionar com uma galera da pesada, cai na pilha errada, logo drogas, logo cadeia.'],
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
    4: {
        'frases': ['Repete de ano na primeira fase, eterno mono.'],
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
    5: {
        'frases': ['Suas notas são tão altas que começam a achar que você está colando e você é expulso.'],
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
    6: {
        'frases': ['Em um momento de burrice, você decide subir no telhado do ifsc durante um temporal com um fio desencapado para captar sinais AM, é acertado por um raio e morre.'],
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
    7: {
        'frases': ['No ápice de sua inteligencia, você constrói uma cadeira telefone tão avançada que ela se torna um foguete e te leva para o espaço.'],
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
    8: {
        'frases': ['Você se estica para tentar alcançar o objeto e escorrega, caindo no esgoto e se afoga.'],
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
            '\$[oO] que': 8000},
        'negativa_proximos_estados': {
            '\$[oO] que': 8000
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
    32: {
        'frases': ['Um buraco foi aberto para reformas no esgoto do ifsc, no fundo você vê algo brilhante. Quer pegar? \n 1=Sim \n 2=Não'],
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
            '\$1': 8},
        'negativa_proximos_estados': {
            '\$2': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },
    33: {
        'frases': ['Você está na aula de matemática do João. Tem uma prova de sociologia na próxima aula. Você..\n 1=Decide prestar atenção na aula \n 2=Decide estudar sociologia'],
        'frases_positivas': 'Você consegue aprender matemática, mas não consegue ir tão bem na prova.',
        'frases_negativas': 'Enquanto estuda sociologia, o professor da um socão no quadro e você leva um susto, mas pelo menos consegue tirar uma boa nota em sociologia no próximo período.',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': -13,
        'positivos_inteligência': 15,
        'negativos_sanidade': -15, 
        'negativos_popularidade': 0,
        'negativos_notas': 20,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 8000},
        'negativa_proximos_estados': {
            '\$2': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },10: {
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
        
    },10: {
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
        
    },10: {
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
        
    },10: {
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
        
    },10: {
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
        
    },10: {
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
        
    },10: {
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