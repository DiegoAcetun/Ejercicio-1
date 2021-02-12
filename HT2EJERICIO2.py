nombre = input(" ingrese su nombre ")
nombre = nombre.upper()

sexo = input (" Ingrese su sexo ")
sexo = sexo.upper()

letra_nombre = nombre[0]
print(letra_nombre)

if sexo == "MUJER":  
    if letra_nombre == 'A' or letra_nombre == 'B' or letra_nombre == 'C' or letra_nombre == 'D' or letra_nombre == 'E' or letra_nombre == 'F' or letra_nombre == 'G' or letra_nombre == 'H' or letra_nombre == 'I' or letra_nombre == 'J' or letra_nombre == 'K' or letra_nombre == 'L' or letra_nombre == 'M':
        print("Le corresponde el grupo A")

    elif letra_nombre == 'N' or letra_nombre == 'O' or letra_nombre == 'P' or letra_nombre == 'Q' or letra_nombre == 'R' or letra_nombre == 'S' or letra_nombre == 'T' or letra_nombre == 'U' or letra_nombre == 'V' or letra_nombre == 'W' or letra_nombre == 'X' or letra_nombre == 'Y' or letra_nombre == 'Z':
        print("Le corresponde el grupo B")

elif  sexo == "HOMBRE":  
    if letra_nombre == 'N' or letra_nombre == 'O' or letra_nombre == 'P' or letra_nombre == 'Q' or letra_nombre == 'R' or letra_nombre == 'S' or letra_nombre == 'T' or letra_nombre == 'U' or letra_nombre == 'V' or letra_nombre == 'W' or letra_nombre == 'X' or letra_nombre == 'Y' or letra_nombre == 'Z':
        print("Le corresponde el grupo A")

    elif  letra_nombre == 'A' or letra_nombre == 'B' or letra_nombre == 'C' or letra_nombre == 'D' or letra_nombre == 'E' or letra_nombre == 'F' or letra_nombre == 'G' or letra_nombre == 'H' or letra_nombre == 'I' or letra_nombre == 'J' or letra_nombre == 'K' or letra_nombre == 'L' or letra_nombre == 'M':
        print("Le corresponde el grupo B")


   

