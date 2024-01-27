import string
import random

longitud= int(input('ingrese el tamaño de la contraseña: '))

caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena= "".join(random.choice(caracteres) for i in range (longitud))

print ("La contraseña generada es: " , contrasena)