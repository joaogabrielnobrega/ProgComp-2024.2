## Jogo termo(www.term.ooo) dueto com 7 tentativas mostrar as cores
#print("\033[;31;42mCaramba\033[0m")
#31: Vermelho
#32: Verde
#33: Amarelo
#34: Azul
#35: Magenta
#36: Ciano
#37: Branco
#0: Reseta para a cor padrão

'''
palavra1 = 
palavra2 =
tentativa = 1
verde = faz parte da palavra e esta na posição correta
amarelo = faz parte mas posição errada
preto = não faz parte da palavra

while tentativa <= 7:
    while letra < len(palavra1):
    while letra < len(palavra2):
'''

import random
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)

palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)
print(palavra1)
print(palavra2)
tentando_palavra1 = True
tentando_palavra2 = True
"""
a = "VIUVO"
print(f"\033[1;37;42m {a}", end="-")
print("")
print(f"arroz{palavra1[0]}")
"""

tentativa = 1
palavra_tentativa = input("Digite sua tentativa: ")
#if a in palavras:
#    print("")

#erro: quando a primeira letra da tentativa é igual ou existe na palavra todas as outras letras ficam amarelas
#achei o motivo, só precisei ler a linha 75 e 86, no lugar de (letra) estava (0)
while tentativa <= 7:
    #for ind in palavra
    letra = 0
    while tentando_palavra1 and letra < len(palavra1):
        if palavra_tentativa[letra] == palavra1[letra]:
            print(f"\033[1;37;42m{palavra_tentativa[letra]}\033[m", end="-")
        elif palavra_tentativa[letra] in palavra1:
            print(f"\033[1;37;43m{palavra_tentativa[letra]}\033[m", end="-")
        else: print(f"\033[1;37;41m{palavra_tentativa[letra]}\033[m", end="-")
        if letra == len(palavra1) - 1 and  palavra_tentativa == palavra1:
            tentando_palavra1 = False
        letra += 1
    letra = 0
    print("")
    while tentando_palavra2 and letra < len(palavra2):
        if palavra_tentativa[letra] == palavra2[letra]:
            print(f"\033[1;37;42m{palavra_tentativa[letra]}\033[m", end="-")
        elif palavra_tentativa[letra] in palavra2:
            print(f"\033[1;37;43m{palavra_tentativa[letra]}\033[m", end="-")
        else: print(f"\033[1;37;41m{palavra_tentativa[letra]}\033[m", end="-")
        if letra == len(palavra2) - 1 and palavra_tentativa == palavra2:
            tentando_palavra2 = False
        letra += 1
    print("")
    if tentando_palavra1 or tentando_palavra2:
        palavra_tentativa = input("Digite sua tentativa: ")
    else:
        tentativa += 10
    tentativa += 1