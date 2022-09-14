'''
LABORATORIO 2 SEGURIDAD INFORMATICA
SEBASTIAN ARAYA Y JOAQUIN GONZALEZ
13/09/2022
'''

#Funciones de cifrado

abc = 'abcdefghijklmnopqrstuvwxyz'                                  #STRINGS de todos los caracteres del abecedario

def rot(string, n):                                                 #Funcion CIFRADO ROT(N)
    ls = [*string]                                                  #Ls: Lista donde cada posicion es un STRING del MSG original
    for i in range(len(string)):                                    #For de i en el largo de la lista de strings
        ls[i]=abc[(abc.find(string[i])+n)%26]                       #El String i se convierte en el caracter con N desplazamientos adicionales
    return ''.join(ls)                                              #Retorna el texto 


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

