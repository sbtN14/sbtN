# LABORATORIO 4
# SEBASTIAN ARAYA
# JOAQUIN GONZALEZ

import random
from math import pow
import socket

HOST = "127.0.0.1"                                               #Direccion IP del servidor
PORT = 65433     

#Clave privada aleatoria
a = random.randint(2, 10)

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

# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c
 
#Funcion desencripta 
def decrypt(en_msg, p, key, q):
 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
         
    return dr_msg

 
q = random.randint(pow(10, 10), pow(10, 25))
g = random.randint(2, q)
key = gen_key(q)# Private key for receiver
h = power(g, key, q)
print("generador aleatorio usado: ", g)
print("K (g^a) usado: ", h)

#Public = [q,g,h]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, 65433))                                       #Establece el IP y el Puerto
    s.listen()                                                  #Deja al servidor listo para recibir info
    conn, addr = s.accept()                                     #Acepta la conexion
    with conn:                                                   #En la conexion
        print(f"Connected by {addr}")                            #Muestra mensaje de conexion exitosa
        while True:                                             
            conn.send(bytes(str(q).encode()))
            conn.send(bytes(str(g).encode()))
            conn.send(bytes(str(h).encode()))
            break            

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, 65434))                                       #Establece el IP y el Puerto
    s.listen()                                                  #Deja al servidor listo para recibir info
    conn, addr = s.accept()                                     #Acepta la conexion
    with conn:                                                   #En la conexion
        print(f"Connected by {addr}")                                         #Muestra mensaje de conexion exitosa
        while True:    
            textoCifrado = conn.recv(1024)    
            print('hola')                           
            break        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, 65435))                                       #Establece el IP y el Puerto
    s.listen()                                                  #Deja al servidor listo para recibir info
    conn, addr = s.accept()                                     #Acepta la conexion
    with conn:                                                   #En la conexion
        print(f"Connected by {addr}")                                         #Muestra mensaje de conexion exitosa
        while True:          
            p = conn.recv(1024)          
            print('chao')                   
            break        

print(f'Texto ->{textoCifrado}')

textoCifrado = textoCifrado.decode()
textoCifrado = textoCifrado.replace('[', '')
textoCifrado = textoCifrado.replace(']', '')
textoCifrado = textoCifrado.split()
texto2 = []

for i in textoCifrado:
    i = i.replace("'","")
    i = i.replace(",","")
    i = int(i)
    texto2.append(i)
print(f'Texto 2 ->{texto2}')

p = int(p.decode())

dr_msg = decrypt(texto2, p, key, q)
dmsg = ''.join(dr_msg)
print("Decrypted Message :", dmsg)
recibido = open("E:\Codes\Laboratorio 4\mensajerecibido.txt", "w") #Abre el archivo como lectura
recibido.write(dmsg.decode())                                             #Lee la informacion y la asigna a la var
recibido.close()    