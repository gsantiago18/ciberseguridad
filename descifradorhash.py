import hashlib

hash_file = "96d8b00f71986049ea08ecc2654eccd6bb7d8022cc74460e07c942f259746897"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

with open(dic_file, "r") as file:
    diccionario = [line.strip() for line in file]

    for password in diccionario:
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:
            print('La contraseña original es: ' + password)
            break
        else:
            print('La contraseña no se encuentra en el diccionario' )