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
        'positivos_notas': 15,
        'positivos_inteligência': 10,
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
        'positivos_popularidade': -7,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -10,
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
        'frases_positivas': 'Você finge que não viu e ele copia sua prova inteira',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 14,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
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
        'frases': ['A próxima aula é do Carlyle. Você decide... \n 1=...matar a aula e ir no Mini Kalzone com os casas \n 2=...ir na aula e (tentar) prestar atenção na aula'],
        'frases_positivas': 'Você se diverte com seus casas no Mini Kalzone, até decidir pedir um sorvetão de morango e perceber que é horrível e que jogou fora seu dinheiro',
        'frases_negativas': 'A aula dele é terrível, mas você consegue acompanhar uma parte da matéria',
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
        'frases_positivas': 'Você passa quase a noite inteira escrevendo seu relatório e vai pra aula praticamente morto',
        'frases_negativas': 'Você dorme igual um neném, porém com a consciência pesada',
        'positivos_sanidade': -11, 
        'positivos_popularidade': 0,
        'positivos_notas': 15,
        'positivos_inteligência': 0,
        'negativos_sanidade': 15, 
        'negativos_popularidade': 0,
        'negativos_notas': -11,
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
        'frases': ['Richard te pede um "pedacinho" do seu lanche, você dá? \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Ele mente e pega uma grande parte do seu lanche. Você fica triste, porém faz amizade com ele. Ainda está em dúvida se isso é bom ou ruim.',
        'frases_negativas': 'Richard fica triste com você, mas pelo menos o lanche é todo seu',
        'positivos_sanidade': -7, 
        'positivos_popularidade': 10,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 10, 
        'negativos_popularidade': -5,
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
        'positivos_notas': 8,
        'positivos_inteligência': 8,
        'negativos_sanidade': 7, 
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
        'frases_positivas': 'Você pede desculpa e segue em frente',
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
        'frases_positivas': 'A fruta tava podre e você fica enjoado',
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
        'frases': ['Te chamam pra jogar de goleiro o interclasse. Você vai? \n 1=Não\n 2=Sim'],
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
        'frases_positivas': 'Você executa um rolamento perfeito e impressiona todas as outras 2 pessoas que estavam matando aula no relaxa aí',
        'frases_negativas': 'Você cai no chão e parece um idiota',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 9,
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
    49: {
        'frases': ['Mongol gigante te chama pro soco no karate do marquinhos. Você...\n 1=...desvia dos golpes \n 2=bate de frente com ele'],
        'frases_positivas': 'Você é ágil demais para o mongol, e ele erra todos os golpses, caindo no chão',
        'frases_negativas': 'Ele é muito maior que você e te derrota facilmente',
        'positivos_sanidade': 10, 
        'positivos_popularidade': 10,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': -10, 
        'negativos_popularidade': -10,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2049},
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
        'frases_positivas': 'Ele nem percebe que você fez isso e sai feliz da sala, achando que vai conseguir tirar uma boa nota',
        'frases_negativas': 'Você dedura ele e todos acham você um otário',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 15,
        'positivos_inteligência': 13,
        'negativos_sanidade': 0, 
        'negativos_popularidade': -20,
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
    2049: {
        'frases': ['O que você faz em seguida? \n 1=Correr \n 2=Aproveito o momento perfeito para retaliar'],
        'frases_positivas': 'Você corre da luta e perde o respeito de todos',
        'frases_negativas': 'Você utiliza do momento de fraqueza do mongol e finaliza ele no chão, ganhando a luta',
        'positivos_sanidade': 0, 
        'positivos_popularidade': -15,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 10, 
        'negativos_popularidade': 15,
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
    2050: {
        'frases': ['Quer fazer o tutorial? \n 1=Sim \n 2=Não'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2051},
        'negativa_proximos_estados': {
            '\$2': 2060
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2051: {
        'frases': ['Bem vindo ao Reigns IFSC! Esse tutorial lhe introduzirá as mecânicas básicas de escolhas e status que você terá de lidar durante o jogo. \n 1=Entendi \n 2=OK'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2052},
        'negativa_proximos_estados': {
            '\$2': 2052
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2052: {
        'frases': ['Nesse jogo, você possui 4 status: Sanidade, Popularidade, Notas e Inteligência. Você deve administrá-los, evitando que eles cheguem em 0 ou 100. Caso isso aconteça, você vai morrer. \n 1=Vou morrer!? \n 2=OK'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2053},
        'negativa_proximos_estados': {
            '\$2': 2053
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2053: {
        'frases': ['Todas suas escolhas tem consequências, podendo diminuir ou aumentar um ou mais status. Depende de você decidir qual a melhor opção. Este tutorial serve para você aprender as mecânicas básicas, portanto, não haverão consequências. Depois disso, cada escolha sua importa, e você estará por conta própria. \n 1=OK \n 2=Saquei'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2054},
        'negativa_proximos_estados': {
            '\$2': 2054
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2054: {
        'frases': ['Por algum motivo, você acha que é uma boa ideia entrar no IFSC, e decide se inscrever para realizar a prova. O teste é daqui a 7 dias. Você decide estudar durante essa semana? \n 1=Sim \n 2=Não'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 10,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': -10,
        'positivo_proximos_estados': {
            '\$1': 2055},
        'negativa_proximos_estados': {
            '\$2': 2055
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2055: {
        'frases': ['Uma semana se passa. A prova é amanhã. Você decide virar a noite jogando? \n 1=Sim \n 2=Não'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': -10, 
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
    },  
    2056: {
        'frases': ['Hoje é o dia da prova. Você chega no IFSC e encontra sua sala e mesa, e se senta para fazer a prova. Você se sente nervoso? \n 1=Sim \n 2=Não'],
        'frases_positivas': 'Você fica nervoso demais na hora da prova e corre para o banheiro. Todos em volta olham para você e te acham um esquisito.',
        'frases_negativas': 'Sua tranquilidade nesse momento de pressão te faz parecer um chad.',
        'positivos_sanidade': 0, 
        'positivos_popularidade': -10,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 10,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2057},
        'negativa_proximos_estados': {
            '\$2': 2058
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2057: {
        'frases': ['Depois de se acalmar, você volta para a sala. O inspetor entrega a prova para todos. Hora de mostrar do que você é capaz. Você lê a primeira questão: Complete corretamente a espaço vazio: Ele saiu cedo de casa, ____ o congestionamento o atrasou.\n 1=Mas \n 2=Mais'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 10,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': -10,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2059},
        'negativa_proximos_estados': {
            '\$2': 2059
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2058: {
        'frases': ['O inspetor entrega a prova. Hora de mostrar do que você é capaz. Você lê a primeira questão: Sem ___ nem menos, decidiu viajar para a Europa. \n 1=Mas \n 2=Mais'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': -10,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 10,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2059},
        'negativa_proximos_estados': {
            '\$2': 2059
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2059: {
        'frases': ['Parabéns! Você concluiu o tutorial e conseguiu entrar no IFSC. Mas não fique feliz, os problemas só começaram, afinal agora você precisa sofrer por 4 anos seguidos, e tudo fica pior a cada semestre que se passa. Boa sorte. \n 1=Beleza \n 2=OK'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': 0,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': 0, 
        'negativos_popularidade': 0,
        'negativos_notas': 0,
        'negativos_inteligência': 0,
        'positivo_proximos_estados': {
            '\$1': 2060},
        'negativa_proximos_estados': {
            '\$2': 2060
        },
        'append_positivo': 8000,
        'append_negativo': 8000,
        'remove_positivo': 8000,
        'remove_negativo': 8000
    },  
    2060: {
        'frases': ['Você chega ao IFSC, ansioso e, um pouco, nervoso para seu primeiro dia de aula. Ao subir as escadas, se vê cercado por uma multidão de pessoas que apenas gritam uma palavra "mono", você não sabe o que isso significa ou quais são suas intensões com essa ação. O que você faz? \n 1=Começa a chorar e corre \n 2=Tenta parecer calmo e os ignora'],
        'frases_positivas': '',
        'frases_negativas': '',
        'positivos_sanidade': 0, 
        'positivos_popularidade': -15,
        'positivos_notas': 0,
        'positivos_inteligência': 0,
        'negativos_sanidade': -15, 
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
        
}

# Dicionário com os estados correntes de cada jogador.
fatos = {}

#reservar 0-15 para derrotas
#reservar 16-31 (quanto prescisar)
#cenarios mormais 32-1023
#cenarios historias 1024-2047
#cenarios de continuação 2048-3000