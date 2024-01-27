import socket

ip= input("Ingrese la direccion IP a escannear: ")

for puerto in range (1,65535):
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("Puerto abierto: " +str(puerto))
        sock.close()

    else:
        print("Puerto cerrado: " +str(puerto))        