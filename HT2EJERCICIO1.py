contra = input(" Ingrese la contraseña ")
contra = contra.upper()

palabra = input(" Cual es la contraseña? ")
palabra = palabra.upper()


if palabra == contra:
    print("Contraseña correcta")

else:
    print("Contraseña incorrecta")