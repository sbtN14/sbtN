'''
SEGURIDAD INFORMATICA
Laboratorio 1
Sebastian Araya y Joaquin Gonzalez
'''

import requests

print(f'DESAFIO 1')

#  DESAFIO 1
abc = "abcdefghijklmnopqrstuvwxyz"                                  #STRINGS de todos los caracteres del abecedario

def rot(string, n):                                                 #Funcion CIFRADO ROT(N)
    ls = [*string]                                                  #Ls: Lista donde cada posicion es un caracter del MSG original
    for i in range(len(string)):                                    #For de i en el largo de la lista de caracteres
        ls[i]=abc[(abc.find(string[i])+n)%26]                       #El caracter i se convierte en el caracter con N desplazamientos adicionales
    return ''.join(ls)                                              #Retorna la lista de caracteres permutados

def cifrar(cadena, clave):                                          #Funcion CIFRADO VIGENERE que recive MSG ORIGINAL y CLAVE
    text_cifrar = ""                                                #setear texto a cifrado en vacio
    i = 0                                                           #setear i en 0
    for letra in cadena:                                            #For que se posiciona en cada letra del MSG ORIGINAL
        suma = abc.find(letra) + abc.find(clave[i % len(clave)])    #Suma la POS de la letra(msg) con la pos de la letra(pass), respecto abc
        modulo = int(suma) % len(abc)                               #obtiene la posicion de la letra correspondiente
        text_cifrar = text_cifrar + str(abc[modulo])                #juntar el texto ya cifrado con la letra a traves de la posicion en abc
        i = i + 1                                                   #Avanza de posicion el i para recorrer la CLAVE
    return text_cifrar                                              #Retorna el texto cifrado
 
def descifrar(cadena, clave):                                       #Funcion DECIFRADO VIGENERE que recive MSG CIFRADO y CLAVE
    text_cifrar = ""                                                #setear texto a decifrar en vacio
    i = 0                                                           #setear i en 0
    for letra in cadena:                                            #For que se posiciona en cada letra del MSG CIFRADO
        suma = abc.find(letra) - abc.find(clave[i % len(clave)])    #Resta la POS de la letra(msg) con la pos de la letra(pass), respecto abc
        modulo = int(suma) % len(abc)                               #obtiene la posicion de la letra correspondiente
        text_cifrar = text_cifrar + str(abc[modulo])                #juntar el texto ya decifrado con la letra a traves de la posicion en abc
        i = i + 1                                                   #Avanza de posicion el i para recorrer la CLAVE
    return text_cifrar                                              #Retorna el texto decifrado
 
def vigenere(string, proceso, clave):                               #MENU del cifrado vigenere, recibe msg, opcion y clave
    if proceso == 0:                                                #Si la opcion es 0
        return cifrar(string, clave)                                #CIFRA
    elif proceso == 1:                                              #Si la opcion es 0
        return(descifrar(string, clave))                            #DECIFRA                         
 
#ITERACIONES DEL DESAFIO 1

headers = {
    'Content-Type': 'text/plain',
}

data = '{"msg":"bncmwxuqdlzxecdkrzdmh"}'

response = requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=data)
print(response.content)

stringg = 'aprendiendoadescifrar'                                     #MSG Original
print(f'Mensaje Original -> {stringg}')                             #Muestra el MSG Original

first_rot = rot(stringg, 8)                              #APLICA CIFRADO ROT8
print(f'Rot 8 Cifrado -> {first_rot}')                              #Muestra el MSG CIFRADO EN ROT8

first_vig = vigenere(first_rot, 0, 'heropassword')                  #APLICA CIFRADO VIGENERE
print(f'Vigenere Cifrado -> {first_vig}')                           #Muestra el MSG CIFRADO EN VIGENERE

second_rot = rot(first_vig, 12)                           #APLICA CIFRADO ROT12
print(f'Rot 12 Cifrado -> {second_rot}')                            #Muestra el MSG CIFRADO EN ROT12

first_unrot = rot(second_rot, -12)                        #APLICA CIFRADO ROT-12
print(f'Rot 12 Descifrado -> {first_unrot}')                       #Muestra el MSG CIFRADO EN ROT-12

first_unvig = vigenere(first_unrot, 1, 'heropassword')              #APLICA DECIFRADO VIGENERE
print(f'Vigenere Descifrado -> {first_unvig}')                      #Muestra el MSG DECIFRADO EN VIGENERE

second_unrot = rot(first_unvig, -8)                                  #APLICA CIFRADO ROT-8
print(f'Rot 8 Descifrado -> {second_unrot}')                       #Muestra el MSG CIFRADO EN ROT-8



# DESAFIO 2
response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)

#print(response.content)                                             #Muestra el contenido de response para obtener la PALABRA
print(f'\nDESAFIO 2')

Palabra = 'DuaqQbOzYukrcqgEnwdqjl'                                  #PALABRA A DECIFRAR (obtenida de response)
print(f'Frase Cifrada -> {Palabra}')

word = [*Palabra]                                                   #Lista formada por los caracter de la palabra
bins = []                                                           #Lista que guarda si la letra es MAYUSC o MINUSC

for i in word:                                                      #For de in en la palabra
    if i.isupper():                                                 #SI es una letra MAYUSC
        bins.append(True)                                           #Guarda TRUE en la Lista bins
    else:                                                           #EN OTRO CASO 
        bins.append(False)                                          #Guarda FALSE en la Lista bins

rot1 = rot(Palabra.lower(), -12)

second_unvig = vigenere(rot1, 1, 'finispasswd')                     #DECIFRA EN VIGENERE
rot2 = rot(second_unvig, -8)
lss = [*rot2]                                                       #Lista formada de la palabra DECIFRADA

for i in range(len(word)):                                          #For i en el rano del laro de la lista Word
    if bins[i]:                                                     #SI bins en la POS i es True
        lss[i] = lss[i].upper()                                     #El caracter en la posicion i de lss sera pasado a MAYUSC

mensajefinal = ''.join(lss)                                         #Une una cadena de texto vacia con la lista lss

print(f'Mensaje Descifrado -> {mensajefinal}')                     #Muestra el texto decifrado del desafio 2