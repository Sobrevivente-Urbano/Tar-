import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


cartas = {
    1: 'O Louco - Viagem, liberdade, inocencia',
    2: 'O Mago - Ação, Novidades, poder',
    3: 'A Sacerdotisa - Sabedoria, misterio, oculto',
    4: 'A Imperatriz - Comunicação, fertilidade, realizações',
    5: 'O Imperador - Proteção, segurança, estabilidade',
    6: 'O Hierofante - Aconselhamento, estudos, tradição',
    7: 'Os Amantes - Escolhas, relacionamentos, amor',
    8: 'O Carro - Controle, rumo, oportunidades',
    9: 'A Força - Sensualidade, coragem, autocontrole',
    10: 'O Eremita - Reclusão, paciência, estudos',
    11: 'A Roda da Fortuna - Viagem, mudança inesperada, destino', 
    12: 'A Justiça - Negociações legais, reconciliação, ser justo', 
    13: 'O Enforcado - Estagnação, sacrifício, deixar ir',
    14: 'A Morte - Transformação, mudança, fim de ciclo',
    15: 'A Temperança - Equilibrio, harmonia, moderação',
    16: 'O Diabo - Tentação, material, sexualidade',
    17: 'A Torre - Ruptura, perda, destruição',
    18: 'A Estrela - Esperança, inspiração, espiritualidade',
    19: 'A Lua - Ilusão, duvidas, fertilidade',
    20: 'O Sol - Alegria, realizações, gravidez',
    21: 'O Julgamento - Renovação, Renascimento, resgate',
    22: 'O Mundo - Viagem, sucesso, conclusão',
    23: 'Ás de Paus – Novos projetos',
    24: 'Dois de Paus – Inquietação',
    25: 'Três de Paus – Estabelecer força',
    26: 'Quatro de Paus – Harmonia',
    27: 'Cinco de Paus – Luta, Conflito',
    28: 'Seis de Paus – Vitoria',
    29: 'Sete de Paus – Obstaculos',
    30: 'Oito de Paus – Atividade',
    31: 'Nove de Paus – Recuperação',
    32: 'Dez de Paus – Fardo, Peso',
    33: 'Valete de Paus – Mensagem',
    34: 'Cavaleiro de Paus – Movimento',
    35:	'Rainha de Paus – Criação',
    36: 'Rei de Paus – Lider',
    37: 'As de Copas – Novos relacionamentos',
    38: 'Dois de Copas – Parceria',
    39: 'Tres de Copas – Celebração',
    40: 'Quatro de Copas – Insatisfação',
    41: 'Cinco de Copas – Arrependimento',
    42: 'Seis de Copas – Melancolia',
    43: 'Sete de Copas – Escolhas',
    44: 'Oito de Copas – Nova direção',
    45: 'Nove de Copas – Satisfação',
    46: 'Dez de Copas – Felicidade',
    47: 'Valete de Copas – Mensageiro',
    48: 'Cavaleiro de Copas – Movimento',
    49: 'Rainha de Copas – Influenciar',
    50: 'Rei de Copas – Autoridade',
    51: 'As de Espadas – Algo chegando',
    52: 'Dois de Espadas – Escolhas',
    53: 'Três de Espadas – Coração partido',
    54: 'Quatro de Espadas – Descansar',
    55: 'Cinco de Espadas – Derrota',
    56: 'Seis de Espadas – Progresso',
    57: 'Sete de Espadas – Traição',
    58: 'Oito de Espadas – Restrição',
    59: 'Nove de Espadas – Depressão',
    60: 'Dez de Espadas – Infortuno',
    61: 'Valete de Espadas – Joven',
    62: 'Cavaleiro de Espadas – Agressivo',
    63: 'Rainha de Espadas – Vingativa',
    64: 'Rei de Espadas – Homem lógico',
    65: 'As de Ouros – Potencial',
    66: 'Dois de Ouros – Dualidade',
    67: 'Tres de Ouros – Comunicação',
    68: 'Quatro de Ouros – Estabilidade',
    69: 'Cinco de Ouros – Adversidade',
    70: 'Seis de Ouros – Crescimento',
    71: 'Sete de Ouros – Fé',
    72: 'Oito de Ouros – Mudança',
    73: 'Nove de Ouros – Processo',
    74: 'Dez de Ouros – Conclusão',
    75: 'Valete de Ouros  – Mensagem',
    76: 'Cavaleiro de Ouros – Movimento',
    77: 'Rainha de Ouros – Influencia',
    78: 'Rei de Ouros – Autoridade'
}
print(bcolors.OKCYAN + '#############################')
print(bcolors.OKCYAN + '# Passado, Presente, Futuro # ')
print(bcolors.OKCYAN + '#############################')
passado_pres_fut = random.sample(range(1,78), 3)
print(bcolors.HEADER + "Passado: " + bcolors.FAIL + cartas[passado_pres_fut[0]])
print(bcolors.HEADER + "Presente: " + bcolors.FAIL + cartas[passado_pres_fut[1]])
print(bcolors.HEADER + "futuro: " + bcolors.FAIL + cartas[passado_pres_fut[2]])
print('')

print(bcolors.OKCYAN + '############')
print(bcolors.OKCYAN + '# Problema # ')
print(bcolors.OKCYAN + '############')

cinco_cartas = random.sample(range(1,78), 5)
print(bcolors.HEADER + "Situação atual do problema: " + bcolors.FAIL + cartas[cinco_cartas[0]])
print(bcolors.HEADER + "Influência do passado em relação ao problema: " + bcolors.FAIL + cartas[cinco_cartas[1]])
print(bcolors.HEADER + "Tendências para um futuro próximo: " + bcolors.FAIL + cartas[cinco_cartas[2]])
print(bcolors.HEADER + "O que está oculto sob aparência: " + bcolors.FAIL + cartas[cinco_cartas[3]])
print(bcolors.HEADER + "Uma possível solução para o problema: " + bcolors.FAIL + cartas[cinco_cartas[4]])
print('')

print(bcolors.OKCYAN + '###########')
print(bcolors.OKCYAN + '# Mandala # ')
print(bcolors.OKCYAN + '###########')

mandala = random.sample(range(1,78), 13)
print(bcolors.HEADER + "Intenções ou projetos: " + bcolors.FAIL + cartas[mandala[0]])
print(bcolors.HEADER + "Finanças, ganhos e despesas: " + bcolors.FAIL + cartas[mandala[1]])
print(bcolors.HEADER + "Amigos, irmãos, pequenas viagens: " + bcolors.FAIL + cartas[mandala[2]])
print(bcolors.HEADER + "Família, origem: " + bcolors.FAIL + cartas[mandala[3]])
print(bcolors.HEADER + "Prazeres, aventuras, filhos, arte: " + bcolors.FAIL + cartas[mandala[4]])
print(bcolors.HEADER + "Profissão, trabalho, saúde: " + bcolors.FAIL + cartas[mandala[5]])
print(bcolors.HEADER + "Associações, contratos, casamentos: " + bcolors.FAIL + cartas[mandala[6]])
print(bcolors.HEADER + "Lado oculto, mudanças, transmutação: " + bcolors.FAIL + cartas[mandala[7]])
print(bcolors.HEADER + "Justiça, viagens longas, religião: " + bcolors.FAIL + cartas[mandala[8]])
print(bcolors.HEADER + "Reputação, status, méritos: " + bcolors.FAIL + cartas[mandala[9]])
print(bcolors.HEADER + "Relações com a sociedade, projetos: " + bcolors.FAIL + cartas[mandala[10]])
print(bcolors.HEADER + "Inimigos ocultos, heranças cármicas: " + bcolors.FAIL + cartas[mandala[11]])
print(bcolors.HEADER + "O momento: " + bcolors.FAIL +cartas[mandala[12]])
print('')

#sortei_arcanos = random.sample(range(1,78), 6)

#sorteados = []

#for caracter in sortei_arcanos:
#   sorteados.append(cartas[caracter])
#   print(cartas[caracter])











