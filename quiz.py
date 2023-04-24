print("------------------multiplicar-------------")
print("------------------------------------------")
print("------------------------------------------")


def generar_tabla(n):
    for i in range(1,11):
       print(n, "*"  ,i,  "="  ,n*i) 


n = int(input("Digite el numero: "))
print("La tabla del " + str(n))
generar_tabla(n)

