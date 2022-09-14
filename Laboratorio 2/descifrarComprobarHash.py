'''
LABORATORIO 2 SEGURIDAD INFORMATICA
SEBASTIAN ARAYA Y JOAQUIN GONZALEZ
13/09/2022
'''

import hashlib                                                      #Libreria para utilizar los hash
import Funciones as Cypher                                          #Importa el archivo con las funciones de cifrado

pw = 'jjcc'                                                         #clave para vigenere

op = open('mensajeseguro.txt', 'r')                   #Abre el archivo de texto en modo lectura
reading = op.readlines()                                            #Guarda en una variable su contenido
op.close()                                                          #Cierdda el archivo de texto

seguro = reading[0][:-1]                                            #Obtiene el texto que contiene el mensaje cifrado
hashed = reading[1]                                                 #Obtiene el texto que contiene el hash del mensaje original

first_unrot = Cypher.rot(seguro, -5)                                #Se le aplica decifrado rot al mensaje cifrado y se guarda
unvig = Cypher.vigenere(first_unrot, 1, pw)                         #Se le aplica decifrado vigenere a lo obtenido anteriormente y se guarda
segundo_unrot = Cypher.rot(unvig, -77)                              #Se le aplica decifrado rot a lo obtenido anteriormente y se guarda

print(f'Mensaje Descifrado -> {segundo_unrot}')                     #Se muestra el resultado del proceso de decifrado de mensaje

h2 = hashlib.sha256(segundo_unrot.encode('utf-8')).hexdigest()      #Se hashea el resultado anterior con la tecnica sha256
print(f'Hash descifrado -> {h2}')                                   #Muestra el mensaje decifrado, ya hasheado

if hashed == h2:                                                    #Compara el hash del mensaje original, con el trabajado recientemente
    print(f'Los hash y mensajes coinciden, el mensaje es integro.') 
else:
    print(f'Los hash y mensajes no coinciden, el mensaje fue modificado.')

