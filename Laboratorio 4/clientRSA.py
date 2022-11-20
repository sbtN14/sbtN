from Crypto.PublicKey import RSA # Importamos el módulo RSA
from Crypto.Cipher import PKCS1_OAEP
import socket


def cipherRSA(textToCipher, key):
    cipher_rsa = PKCS1_OAEP.new(key)
    encryptedData = cipher_rsa.encrypt(textToCipher.encode())
    return encryptedData

HOST = "127.0.0.1"                                               #Direccion IP del servidor
PORT = 65433                                                     #Puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crear socket
    s.connect((HOST, PORT))
    pub_key = RSA.importKey(s.recv(4096), passphrase=None) 
print(pub_key)


archivo = open("E:\Codes\Laboratorio 4\mensajeentrada.txt", "r") #Abre el archivo como lectura
msg = archivo.read()                                             #Lee la informacion y la asigna a la var
archivo.close()      
textoClaro = msg

textoCifrado = cipherRSA(textoClaro, pub_key)
print(f'ENCRIPTADO\n{textoCifrado}\n')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crear socket
    s.connect((HOST, PORT))
    s.send(bytes(textoCifrado))
print(pub_key)