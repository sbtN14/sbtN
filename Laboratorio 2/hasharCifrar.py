'''
LABORATORIO 2 SEGURIDAD INFORMATICA
SEBASTIAN ARAYA Y JOAQUIN GONZALEZ
13/09/2022
'''


import hashlib                                                      #Libreria para utilizar los hash
import Funciones as Cypher                                          #Importa el archivo con las funciones de cifrado


inputFile = open('E:\Codes\Lab2\mensajedeentrada.txt', 'r')         #Abrir el archivo de texto con el mensaje
word = inputFile.read()                                             #Leer lineas del archivo y pasarlas a la variable
inputFile.close()                                                   #Cerrar archivo de texto

print(f'Mensaje Original -> {word}')                                #Muestra el msg original
first_rot = Cypher.rot(word, 77)                                    #sobre el msg aplica un primer rot de 77, es decir 77%26 y lo guarda
pw = 'jjcc'                                                         #clave para vigenere

vig = Cypher.vigenere(first_rot, 0, pw)                             #sobre el primer rot aplica un Cifrado vigenere y lo guarda
segundo_rot = Cypher.rot(vig, 5)                                    #Aplica un rot de 5 sobre el texto cifrado en vigenere

h = hashlib.sha256(word.encode('utf-8')).hexdigest()                #aplica la tecnica de hash sha256 sobre la palabra original
print(f'Hash -> {h}')                                               #Muestra el msg original hasheado


message = open('E:\Codes\Lab2\mensajeseguro.txt', 'w')              #Abre el archivo de texto, si no existe, lo crea

message.write(segundo_rot + '\n')                                   #Escribe el mensaje con cifrados aplicados
message.write(h)                                                    #Escribe el mensaje original hasheado
message.close()                                                     #Cierra el archivo de texto