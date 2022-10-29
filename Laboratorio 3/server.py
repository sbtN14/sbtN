# LABORATORIO 3
# SEGURIDAD INFORMATICA
# SEBASTIAN ARAYA
# JOAQUIN GONZALEZ
# FELIPE GONZALEZ

import pyDHE, socket                                             #Libreria  Diffie Hellman, Socket
from Crypto.Cipher import AES, DES, DES3                         #Libreria  AES, DES, 3DES

def AESdecrypt(key, data):                                       #Metodo para Descencriptar con AES
    nonce = data[:AES.block_size]
    tag = data[AES.block_size:AES.block_size * 2]
    ciphertext = data[AES.block_size * 2:]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)


HOST = "127.0.0.1"                                               #IP (LocalHost)
PORT = 65433                                                     #Puerto

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crea el socket
    s.bind((HOST, PORT))                                         #Establece el IP y el Puerto del servidor
    s.listen()                                                   #Deja al servidor listo para recibir informacion
    conn, addr = s.accept()                                      #Acepta la conexion
    with conn:                                                   #En la conexion
        print(f"Connected by {addr}")                            #Muestra mensaje de conexion exitosa
        while True:
            Kako = pyDHE.new(18)                                 #Realiza el Diffie Hellman 
            KakoF = Kako.negotiate(conn)                         #Envia el B publico y recibe A publico
            KakoF = int(str(KakoF)[0:16])                        #Selecciona los primeros 16 digitos -> 16 bytes
            print(f'Llave Publica ->{KakoF}')                    #Muestra la llave publica recibida
            break                                           

# DES
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xd:     #Crea el socket
    xd.bind((HOST, 65431))                                        #Establece el IP y el Puerto
    xd.listen()                                                   #Deja al servidor listo para recibir info
    conn, addr = xd.accept()                                      #Acepta la conexion
    with conn:                                                    #En la conexion
        print(f"Connected by {addr}")                             #Muestra mensaje de conexion exitosa
        while True:
            data = conn.recv(1024)                                #Recibe data
            if data:                                              #Si venia data
                msgEncrypt = data                                 #asigna la data
                break                                             #Cierra conexion
            
des = DES.new(str(KakoF)[0:8].encode(), DES.MODE_ECB)               #Crea instancia DES metodologia ECB
des = des.decrypt(msgEncrypt)                                       #Descencripta con DES
print(f'DES Decrypt ->{des}')
Archivo = open("E:\Codes\Laboratorio 3\mensajerecibidodes.txt", "w")#Abre el archivo para escribir
Archivo.write(des.decode('utf-8'))                                  #Escribe el texto claro
Archivo.close()                                                     #Cierra el archivo

# 3DES
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xd:   #Crea el socket
    xd.bind((HOST, 65433))                                      #Establece el IP y el Puerto
    xd.listen()                                                 #Deja al servidor listo para recibir info
    conn, addr = xd.accept()                                    #Acepta la conexion
    with conn:
        print(f"Connected by {addr}")                           #Muestra mensaje de conexion exitosa
        while True:                             
            data = conn.recv(1024)                              #Recibe data
            if data:                                            #Si hay data
                msgEncrypt = data                               #Asigna la data
                break                                           #Termina conexion

des3 = DES3.new(str(KakoF).encode(), DES3.MODE_ECB)                     #Crea instancia 3DES metodologia ECB
des3 = des3.decrypt(msgEncrypt)                                         #Descencripta con 3DES
print(f'3DES Decrypt ->{des3}')                                 
Archivo = open("E:\Codes\Laboratorio 3\mensajerecibido3des.txt", "w")   #Abre el archivo para escribir
Archivo.write(des3.decode('utf-8'))                                     #Escribe el texto claro
Archivo.close()                                                         #Cierra el archivo


# AES
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xdd:   #Crea el socket
    xdd.bind((HOST, 65431))                                      #Establece el IP y el Puerto
    xdd.listen()                                                 #Deja al servidor listo para recibir info
    conn, addr = xdd.accept()                                    #Acepta la conexion
    with conn:                                                   #En la conexion
        print(f"Connected by {addr}")                            #Muestra mensaje de conexion exitosa
        while True:                                             
            data = conn.recv(1024)                               #Asigna el msg encriptado a data y max de 1024b
            if data:                                             #Si viene data
                msgEncrypt = data                                #Asigna la data
                break                                            #Terminar conexion

Msg = AESdecrypt(str(KakoF).encode(),msgEncrypt)                    #Descencripta AES
print(f'AES Decrypt ->{Msg}')                                       #Muestra MSG
Archivo = open("E:\Codes\Laboratorio 3\mensajerecibidoaes.txt", "w")#Abre el archivo para escribir
Archivo.write(Msg.decode("utf-8"))                                  #Escribe el texto claro
Archivo.close()                                                     #Cerrar txt