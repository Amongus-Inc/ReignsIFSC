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
        'frases_positivas': '',
        'frases_negativas': 'você ignora o objeto brilhante e continua com seu dia',
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
        
    },34: {
        'frases': ['Durante uma prova, você vê um aluno colando. O que você faz? \n 1=Ignora e termina sua prova \n 2=Dedura para aumentar sua nota'],
        'frases_positivas': '',
        'frases_negativas': 'O professor zera a prova do aluno mas se recusa a te recompensar.',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -40,
        'negativos_notas': 0,
        'negativos_inteligência': -0,
        'positivo_proximos_estados': {
            '\$1': 8000},
        'negativa_proximos_estados': {
            '\$2': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },35: {
        'frases': ['Você está com sede, quer ir ao bebedouro? \n 1=Não \n 2=Sim'],
        'frases_positivas': 'Você não vai beber água e fica com sede na sala',
        'frases_negativas': 'Você dá sorte e bebe água geladinha',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 10, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
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
        
    },36: {
        'frases': ['Depois de chegar na sala e se sentar, diversas pessoas mais velhas entram se dizendo veteranos, estando lá para escolher um "mono-modelo". Você é escolhido. O que você faz? \n 1=Aceita e participa da brincadeira \n 2=Nega o título à todo custo'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 15,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -15,
        'negativos_notas': 0,
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
        
    },37: {
        'frases': ['Você sente vontade de ir ao banheiro. Você vai? \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Você dá azar e não tem papel para secar suas mãos. Você decide sacudir as mãos até que elas fiquem secas, e acaba parecendo um idiota.',
        'frases_negativas': 'Você não consegue segurar a vontade da natureza, e acaba acontecendo um acidente.',
        'positivos_sanidade': 0, 
        'positivos_popularidade': -20,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -10,
        'negativos_notas': 0,
        'negativos_inteligência': -0,
        'positivo_proximos_estados': {
            '\$1': 8000},
        'negativa_proximos_estados': {
            '\$2': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },38: {
        'frases': ['Você sente vontade de ir ao banheiro. Você vai? \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Você dá sorte e tem um restinho de papel para secar as mãos, somente o suficiente para elas ficarem sequinhas. O cara que estava esperando para secar as mãos percebe que não tem mais papel e fica puto com você.',
        'frases_negativas': 'Você segura até o final da aula. Bexigas de aço.',
        'positivos_sanidade': 0, 
        'positivos_popularidade': -5,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': -5, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
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
        
    },
    39: {
        'frases': ['Durante a prova de história, você percebe que o Ricardito está copiando da sua prova. Você... \n 1=...deixa ele copiar \n 2=...decide fazer algo sobre isso'],
        'frases_positivas': '',
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
            '\$1': 8000},
        'negativa_proximos_estados': {
            '\$2': 2048
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },
    40: {
        'frases': ['Você está com sede, quer ir ao bebedouro? \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Você fica com sede mas nada acontece.',
        'frases_negativas': 'Você dá azar e bebe de um bebedouro com água quente.',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
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
        
    },
    41: {
        'frases': ['A próxima aula é do Carlyle. Você decide... \n 1=Matar a aula e ir no Mini Kalzone com os casas \n 2=Ir na aula e (tentar) prestar atenção na aula'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 18, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': -13,
        'negativos_sanidade': -13, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 18,
        'positivo_proximos_estados': {
            '\$1': 8000},
        'negativa_proximos_estados': {
            '\$2': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },
    42: {
        'frases': ['É domingo de noite e você lembra que tem que entregar um relatório de biologia na segunda. Você... \n 1=...passa a noite acordado fazendo. \n 2=...tem uma boa noite de sono.'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': -11, 
        'positivos_popularidade': 0,
        'positivos_notas': 12,
        'positivos_inteligência': 0,
        'negativos_sanidade': 15, 
        'negativos_popularidade': 0,
        'negativos_notas': -12,
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
        
    },
    43: {
        'frases': ['Richard te pede um pedaço de seu lanche, você dá? \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Você fica com sede mas nada acontece.',
        'frases_negativas': 'Você dá azar e bebe de um bebedouro com água quente.',
        'positivos_sanidade': -7, 
        'positivos_popularidade': 10,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 10, 
        'negativos_popularidade': -7,
        'negativos_notas': 0,
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
        
    },
    44: {
        'frases': ['Você ta na aula do Volmir. Você... \n 1=...decide aprender OS SILOuGISMOS \n 2=...decide zoar o sotaque dele'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 8,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 9,
        'negativos_notas': 0,
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
        
    },
    45: {
        'frases': ['Alguém que você conhece mas não muito bem esbarra em você, o que você faz? \n 1=Finge que nada aconteceu \n 2=Cumprimenta a pessoa'],
        'frases_positivas': '',
        'frases_negativas': 'Você confunde ele com outra pessoa e ele só te ignora',
        'positivos_sanidade': 7, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': -7, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
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
        
    },
    46: {
        'frases': ['Você está no recreio e com fome. Você decide...\n 1=...comer as fruta la \n 2=Comprar um lanche na cantina'],
        'frases_positivas': 'A fruta tava podre',
        'frases_negativas': 'Você sacia sua fome mas também pagou bem caro por isso, burro.',
        'positivos_sanidade': -7, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 8, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': -5,
        'positivo_proximos_estados': {
            '\$1': 8000},
        'negativa_proximos_estados': {
            '\$2': 8000
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
        
    },
    47: {
        'frases': ['Te chamam pra jogar de goleiro o interclasse \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Boa decisão',
        'frases_negativas': 'Você entra no interclasse e franga gol',
        'positivos_sanidade': 9, 
        'positivos_popularidade': -7,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -7,
        'negativos_notas': 0,
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
        
    },
    48: {
        'frases': ['Você ta de boa no relaxa ai e tropeça num pufe. Você... \n 1=da um rolamento \n 2=cai no chão'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 9,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -9,
        'negativos_notas': 0,
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
        
    },
    49: {
        'frases': ['Mongol gigante te chama pro soco no karate do marquinhos. Você...\n 1=...desvia dos golpes \n 2=bate de frente com ele'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 9,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -9,
        'negativos_notas': 0,
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
        
    },
    2048: {
        'frases': ['O que? \n 1=Escreve as respostas erradas para ele copiar e no último segundo corrige. \n 2=Dedura ele.'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 11,
        'positivos_notas': 0,
        'positivos_inteligência': 13,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -20,
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