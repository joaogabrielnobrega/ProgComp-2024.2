#   João Gabriel Nóbrega Santos
#               20242014050013
#
#   Programa para descobrir quantos numeros decrescentes exitem entre 10 e 987631

#tudo em comentarios usando string de multiplas linhas foi usado para testes

#Variaveis contadoras
num = 10 
num_decrescentes = 0
porcentagem = 0

#Laço para descobrir quantos numeros decrescentes exitem entre 10 e 987631
while num <= 987631:
    #variavel que conterá se o numero é decrescente
    decrescente = True
    
    '''
    if num == 11:
        print(decrescente)
    '''
    #variavel intermediaria que pode ser modificada
    intermediario = num
    
    #laço para descobrir se um numero é decrescente
    while intermediario > 0 and decrescente:
        x = intermediario % 10
        intermediario //= 10
        '''
        if num == 875:
            print(x)
            print(intermediario)
        '''
        #condicional para atualizar a variavel decrescente quando o ultimo digito for maior que o proximo 
        if intermediario != 0 and x > intermediario % 10:
            decrescente = False
    '''
    if num == 875:
        print(decrescente)
    if num == 10:
        print(decrescente)
    '''
    #condicional para adicionar à contagem se o numero for decrescente
    if decrescente:
        num_decrescentes += 1
    
    #condicional para verificar progresso do programa
    if num % 9876 == 0:
        porcentagem += 1
        print(porcentagem, "% concluido")
    
    num += 1

#função para mostrar o resultado
print("Existem ", num_decrescentes, " numeros decrescentes entre 10 e 987631")