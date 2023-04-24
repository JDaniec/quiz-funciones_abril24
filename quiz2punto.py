print("-----------------ultimo digito = 4--------------")
print("------------------------------------------------")
print("------------------------------------------------")

def verificar_ultimodigito(n):
    r = False
    if n % 10 == 4:
        r = True
        return r

n = int(input("Digite el numero a verificar: "))

if verificar_ultimodigito(n):
    print("El numero a verificar si tiene como ultimo digito 4: ")

else: 
    print("El numero a verificar no tiene como ultimo digito 4")

    