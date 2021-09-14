# Diccionario con la codificación morse
morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
         'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..',   '0': '-----',
         '1': '.----',  '2': '..---',  '3': '...--',
         '4': '....-',  '5': '.....',  '6': '-....',
         '7': '--...',  '8': '---..',  '9': '----.' }
def codificar_palabra(palabra):
    # Creamos una cadena vacía para ir añadiendo las letras codificadas
    palabra_codificada = ''
    # Recorremos los caracteres de la palabra
    for i in palabra:
        # Accedemos al diccionario con la clave correspondiente al caracter y añadimos el valor (el código morse) a la palabra codificada
        palabra_codificada += morse[i.upper()] + ';' # Añadimos un punto y coma entre caracter y caracter.
    return palabra_codificada
    

def decodificar_palabra(palabra):
    # A partir del diccionario morse construimos otro diccionario invertido, es decir, cuyas claves sean los códigos morse y cuyos valores sean las letras asociadas.
    # Recorremos los pares del diccionario morse e invertimos las claves y los valores y devolvemos un diccionario mediante comprensión de diccionarios.
    morse_invertido = {value:key for key, value in morse.items()}
    # Creamos una cadena vacía para ir añadiendo las letras decodificadas.
    palabra_decodificada = ''
    # Dividimos el código morse por el punto y coma y recorremos la lista de códigos resultante.
    for i in palabra.split(';'):
        # Accedemos al diccionario invertido con la clave correspondiente al código morse y añadimos el valor (el caracter decodificado) a la palabra decodificada.
        palabra_decodificada += morse_invertido[i]
    return palabra_decodificada

def codificar_mensaje(mensaje):
    # Creamos una cadena con un espacio para ir añadiendo las palabras codificadas.
    mensaje_codificado = ' '
    # Dividimos el mensaje de entrada por el espacio y obtenemos una lista de palabras.
    mensaje = mensaje.split()
    # Aplicamos la función codificar_palabra a cada palabra de la lista y obtenemos una lista con las palabras codificadas.
    palabras_codificadas = list(map(codificar_palabra, mensaje))
    # Concatenamos todas las palabras de la lista en una cadena separadas por un espacio.
    return mensaje_codificado.join(palabras_codificadas)

def decodificar_mensaje(mensaje):
    # Creamos una cadena con un espacio para ir añadiendo las palabras decodificadas.
    mensaje_decodificado = ' '
    # Dividimos el mensaje de entrada por el espacio y obtenemos una lista de palabras codificadas.
    mensaje = mensaje.split()
    # Aplicamos la función decodificar_palabra a cada palabra de la lista y obtenemos una lista con las palabras decodificadas.
    palabras_decodificadas = list(map(decodificar_palabra,mensaje))
    # Concatenamos todas las palabras de la lista en una cadena separadas por un espacio.
    return mensaje_decodificado.join(palabras_decodificadas)