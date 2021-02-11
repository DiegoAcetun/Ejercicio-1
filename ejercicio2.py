numero = int(input(" ingrese el numero "))
i=1
contador = 0

for i in range (i, numero+1):
    if numero % i == 0:
        contador = contador + 1

   
    

if contador == 2:
    print("es primo")
else:
    print("no es primo")