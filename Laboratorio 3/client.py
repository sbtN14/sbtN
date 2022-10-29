# LABORATORIO 3
# SEGURIDAD INFORMATICA
# SEBASTIAN ARAYA
# JOAQUIN GONZALEZ
# FELIPE GONZALEZ

import pyDHE, socket                                             #Libreria  Diffie Hellman, Socket
from Crypto.Cipher import AES, DES, DES3                         #Libreria  AES, DES, 3DES

def AESncrypt(k, data):                                          #Metodo para encriptar en AES
    cipher = AES.new(k, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + tag + ciphertext


HOST = "127.0.0.1"                                               #Direccion IP del servidor
PORT = 65433                                                     #Puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crear socket
    s.connect((HOST, PORT))                                      #Solicitar conexion 
    print("\n=== Datos de sincronizacion de llaves enviados ===")
    Smidax = pyDHE.new(18)                                       #Realiza el Diffie Hellman 
    SmidaxF = Smidax.negotiate(s)                                #Envia el A publico y recibe B publico
    SmidaxF = int(str(SmidaxF)[0:16])                            #Selecciona los primeros 16 digitos -> 16 bytes
    print(f'Llave Publica ->{SmidaxF}')                          #Muestra la llave publica recibida
    s.sendall(b"Mensaje Enviado")

Archivo = open("E:\Codes\Laboratorio 3\mensajeentrada.txt", "r") #Abre el archivo como lectura
Msg = Archivo.read()                                             #Lee la informacion y la asigna a la var
Archivo.close()                                                  #Cierra el archivo
Msg = Msg.encode()                                               #Lo pasa a bytes


#DES
desEncrypt = DES.new(str(SmidaxF)[0:8].encode(), DES.MODE_ECB)   #Crea instancia DES metodologia ECB
msgdes = desEncrypt.encrypt(Msg)                                 #Encripta con DES

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xd:    #Crea el socket
    xd.connect((HOST, 65431))                                    #Solicitar conexion
    xd.sendall(msgdes)                                           #Manda el msg encriptado
    data = xd.recv(1024)                                         #Asigna data


#3DES
des3Encrypt = DES3.new(str(SmidaxF).encode(), DES3.MODE_ECB)     #Crea instancia 3DES metodologia ECB
msg3des = des3Encrypt.encrypt(Msg)                               #Encripta con 3DES

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xd:    #Crea el socket
    xd.connect((HOST, 65433))                                    #Solicitar conexion
    xd.sendall(msg3des)                                           #Manda el msg encriptado
    data = xd.recv(1024)                                         #Asigna data


#AES
msgEncrypt = AESncrypt(str(SmidaxF).encode(), Msg)               #Encripta el mensaje en AES
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as xdd:   #Crea socket
    xdd.connect((HOST, 65431))                                   #Solicitar conexion    
    xdd.sendall(msgEncrypt)                                      #Manda el mensaje encriptado al server
    data = xdd.recv(1024)                                        #Instancia el tamaño de la data enviada