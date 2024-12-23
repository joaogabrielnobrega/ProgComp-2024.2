num = 10 
num_decrescentes = 0

while num <= 987631:
    decrescente = True
    intermediario = num
    while intermediario > 0 and decrescente:
        x = intermediario % 10
        intermediario //= 10
        if x > intermediario % 10:
            decrescente = False
    if decrescente:
        num_decrescentes += 1

print(num_decrescentes)