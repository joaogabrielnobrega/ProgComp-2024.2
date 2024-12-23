#Programa para descobrir os pares de primos seguidos

num = 1
div = 2
ndiv = 0
primo = False

while div < (num ** 0,5):
    if verifica_primo % div == 0:
        ndiv += 1
    div += 1
if ndiv > 0:
    primo = True

if primo:
    verifica_primo = num + 2
    while div < (verifica_primo ** 0,5):
    if verifica_primo % div == 0:
        ndiv += 1
    div += 1
    if ndiv > 0:
        par_primo = True
        