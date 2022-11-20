# LABORATORIO 4
# SEBASTIAN ARAYA
# JOAQUIN GONZALEZ

from Crypto.PublicKey import RSA, ElGamal # Importamos el módulo RSA
from Crypto.Cipher import PKCS1_OAEP
import socket  


def decipherRSA(encryptedData, key):
    decipher_rsa = PKCS1_OAEP.new(key)
    decryptedData = decipher_rsa.decrypt(encryptedData)
    return decryptedData


bit_size = 2048
keysRSA = RSA.generate(bit_size)


HOST = "127.0.0.1"                                               #IP (LocalHost)
PORT = 65433                                                     #Puerto

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crea el socket
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'CONEXION ESTABLECIDA\n')
        while True:
            conn.send(keysRSA.publickey().exportKey(format='PEM', passphrase=None, pkcs=1)) 
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crea el socket
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'CONEXION ESTABLECIDA\n')
        while True:
            textoCifrado = conn.recv(2048)
            break

dec_data = decipherRSA(textoCifrado, keysRSA)
print(dec_data)

recibido = open("E:\Codes\Laboratorio 4\mensajerecibido.txt", "w") #Abre el archivo como lectura
recibido.write(dec_data.decode())                                             #Lee la informacion y la asigna a la var
recibido.close()     


