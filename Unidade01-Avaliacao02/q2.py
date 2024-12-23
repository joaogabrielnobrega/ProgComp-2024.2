num = 10
palindromos = 0

while num <= 100000:
    msg = "Digite o numero que você deseja testar: \n"
    inverter = num
    invertido = ""

    while inverter > 0:
        x = inverter % 10   
        inverter //= 10 
        invertido = invertido + str(x) 
    invertido = int(invertido)

    if invertido == num:
        print(num)
        palindromos += 1
    num += 1

print("Existem", palindromos, "palindromos entre 10 e 100000")
#print(f"Existem {palindromos} palindromos entre 10 e 100000")