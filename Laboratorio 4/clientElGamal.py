import random
from math import pow
import socket

#Maximo comun divisor
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Generating large random numbers
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)

    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key

# Exponenciación modular
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

# Encriptar con ElGamal
def encrypt(msg, q, h, g):
 
    en_msg = []
 
    k = gen_key(q)# Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p

HOST = "127.0.0.1"                                               #Direccion IP del servidor
PORT = 65433                                                     #Puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crear socket
    s.connect((HOST, 65433))
    q = s.recv(1024)
    g = s.recv(1024)
    h = s.recv(1024)
print(q,g,h)

archivo = open("E:\Codes\Laboratorio 4\mensajeentrada.txt", "r") #Abre el archivo como lectura
msg = archivo.read()                      #Lee la informacion y la asigna a la var
archivo.close()      
textoClaro = msg

q = int(q.decode())
g = int(g.decode())
h = int(h.decode())

textoCifrado, p = encrypt(msg, q, h, g)
textoCifrado = str(textoCifrado).encode('utf-8')

print(f'p ->{p} {type(p)}')
l = [textoCifrado, p]
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crear socket
    s.connect((HOST, 65434))
    s.send(bytes(textoCifrado))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     #Crear socket
    s.connect((HOST, 65435))
    s.send(bytes(str(p).encode()))
