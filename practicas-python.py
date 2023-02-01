
"""

1) Realizar una función para normalizar un vector. La función recibe un vector de longitud indeterminada de
float, y debe devolver un nuevo vector normalizado, es decir el módulo del vector debe ser 1.
Ejemplo:
vector1 = [1, 1, 1] -> [0.577..., 0.577...8, 0.577...]
vector2 = [1, 3, 7, 9] -> [0.084..., 0.253..., 0.591..., 0.760...]

"""

# Programa

A = [1, 3, 7, 9]

def NormalizarVector(V):
    cuenta = 0
    B = []
    for x in V: 
        vector = x**2 
        cuenta += vector
    for x in V: 
        vector = x/cuenta**0.5
        B.append(round(vector, 3))
    return B 

print(NormalizarVector(A))

"""

2) Realizar una función para buscar si hay ganador en un juego de ta-te-ti. La función recibe una matriz de
3x3 con la situación actual del juego. Cada elemento de la matriz contiene “x”, “o” o “ ”(espacio), igual que
en el ejercicio 3. La función debe devolver un None si no hay ganador, o devolver “x” o “o” según si el
ganador es la “x” o la “o”.
Ejemplo:
tablero1 = [["x","o"," "],["o"," ","x"],["x"," ","o"]] -> None
tablero2 = [["x","o"," "],["x","o","x"],["x"," ","o"]] -> "x"

"""

# Programa

tablero1 = [["o","x"," "],
            ["o"," ","x"],
            ["o"," ","x"]]

tablero2 = [["x","o"," "],
            [" ","x","o"],
            ["o"," ","x"]]

tablero3 = [[" ","x","o"],
            [" ","o","x"],
            [" ","x","o"]]

def ComprobarGanador(T):
    for x in range (8):
        if T[0][0] == T[0][1] == T[0][2]:
            if T[0][0] != " ":
                return T[0][0]
        elif T[1][0] == T[1][1] == T[1][2]:
            if T[1][0] != " ":
                return T[1][0]
        elif T[2][0] == T[2][1] == T[2][2]:
            if T[2][0] != " ":
                return T[2][0]
        elif T[0][0] == T[1][0] == T[2][0]:
            if T[0][0] != " ":
                return T[0][0]
        elif T[0][1] == T[1][1] == T[2][1]:
            if T[0][1] != " ":
                return T[0][1]
        elif T[0][2] == T[1][2] == T[2][2]:
            if T[0][2] != " ":
                return T[0][2]
        elif T[0][0] == T[1][1] == T[2][2]:
            if T[1][1] != " ":
                return T[1][1]
        elif T[0][2] == T[1][1] == T[2][0]:
            if T[1][1] != " ":
                return T[1][1]
        else:
            return None
    
print(ComprobarGanador(tablero1))
print(ComprobarGanador(tablero2))
print(ComprobarGanador(tablero3))


"""

3) Construir una función para calcular la superficie de un polígono cualquiera, dados sus vértices utilizando la
fórmula del área de Gauss. La función recibe una lista de vértices, la cantidad de vértices es
indeterminada. Cada vértice es un vector de dos elementos con la posición (x, y). La función debe devolver
un float con la superficie del polígono.
Pueden encontrar el método en:

https://es.wikipedia.org/wiki/F%C3%B3rmula_del_%C3%A1rea_de_Gauss

Ejemplo:

p1 = [[0,0], [0,1], [1,1], [1,0]] -> 1.0
p2 = [[1,1], [1,4], [5,1]] -> 6.0

"""

# Programa

p1 = [[0,0],
      [0,1],
      [1,1],
      [1,0]]

p2 = [[1,1],
      [1,4],
      [5,1]]

def Gauss(G):
    G.append(G[0])
    S = []
    F = []
    for x in G:
        S.append(x[0])
        F.append(x[1])
    del S[-1], F[0]
    Cuenta1 = 0
    índiceF = 0
    for x in(S):
        B = x * F[índiceF]
        Cuenta1 += B 
        índiceF += 1
    S.append(G[-1][0])
    F.insert(0, G[0][1])
    del S[0], F[-1]
    Cuenta2 = 0
    índiceF = 0
    for x in(S):
        C = x * F[índiceF]
        Cuenta2 += C
        índiceF += 1
    Resultado = 1/2 * (Cuenta1 - Cuenta2)
    del G[-1]
    return abs(Resultado)

print(Gauss(p1))
print(Gauss(p2))

"""

1) Construir una función calcule la distancia entre 2 puntos en el plano. La función tiene 4 argumentos (x1,
y1, x2, y2) que son las coordenadas de los puntos. Los tipos de datos de entrada y salida son punto
flotante (float). Opcional, la función recibe 2 vectores (de 2 elementos) en lugar de 4 valores.

"""

# Programa

# Función para 4 valores

def distancia2p(x1, y1, x2, y2):
    from math import sqrt
    return float(sqrt((x2-x1)**2+(y2-y1)**2))

# Programa

x1=float(input("Ingrese el valor de x1: "))
y1=float(input("Ingrese el valor de y1: "))
x2=float(input("Ingrese el valor de x2: "))
y2=float(input("Ingrese el valor de y2: "))

print("Distancia: ", distancia2p(x1, y1, x2, y2))

# Función para 2 vectores de 2 valores

def distancia2p(p1, p2):
    from math import sqrt
    return float(sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))

# Programa

p1=[]

x1=float(input("Ingrese el valor de x1: "))
p1.append(x1)
y1=float(input("Ingrese el valor de y1: "))
p1.append(y1)

p2=[]

x2=float(input("Ingrese el valor de x2: "))
p2.append(x2)
y2=float(input("Ingrese el valor de y2: "))
p2.append(y2)

print("Distancia: ", distancia2p(p1, p2))

"""

Realizar una función que, dadas las 3 dimensiones en centímetros de una caja, devuelva el volumen total
en litros. Realizar otra función que, dadas las 3 dimensiones en centímetros de una caja, devuelva la
superficie total de la caja en cm2. Entrada: las 3 dimensiones en centímetros. Salida: el volumen (en litros)
y la superficie total (en cm2). Opcional, Realizar una sola función que reciba las dimensiones de la caja y
devuelva tanto el volumen, como la superficie de la caja, simultáneamente.

"""

#                                  Funcion

def volumen_superficie(l1, l2, l3):
    return [2*l1*l2+2*l1*l3+2*l2*l3, (l1*l2*l3)/1000]

#                                 Programa

l1=float(input("Lado 1: "))
l2=float(input("Lado 2: "))
l3=float(input("Lado 3: "))

print("Superficie: ", volumen_superficie(l1, l2, l3)[0], "cm²")
print("Volumen: ", volumen_superficie(l1, l2, l3)[1], "litros")


"""

El método más fácil para encriptar un mensaje consiste en el de desplazamiento, cada carácter se desplaza
una cantidad fija llamada clave. Por ejemplo si la clave es 1, la palabra HOLA sería IPMB. Realizar 2
funciones, una para encriptar y otra para desencriptar. A la función se le pasa el texto y la clave (un
entero), y debe devolver un texto. Una pista, la función ord() convierte un carácter en un su código ASCII y
la función chr() convierte el código ASCII en carácter. Tener en cuenta que el texto resultante debe estar
compuesto por las letras del abecedario. Pueden ignorar las diferencias entre mayúsculas y minúsculas, y
pueden ignorar de convertir los signos de puntuación. Opcional, pueden hacer el encriptado más
complejo. Opcional, pueden hacer una sola función que encripte y desencripte, a la misma se le pasa el
texto, la clave (igual que entes) y la operación que se desea realizar (encriptar o desencriptar).

"""

#                               Funcion simple
# (Deja igual cualquier caracter que no sea una letra simple del abecedario)

def encrip_desencrip(texto, clave, operacion):
    texto = texto.lower()
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    texto_encriptado= ""

    if operacion==1:
        for letra in texto:
            if letra in abecedario:
                indice_actual = abecedario.index(letra)
                indice_encriptado = indice_actual + clave
                if indice_encriptado > 26:
                    indice_encriptado -= 27
                texto_encriptado += abecedario[indice_encriptado]
            else:
                texto_encriptado += letra
        return texto_encriptado
    elif operacion==2:
        for letra in texto:
            if letra in abecedario:
                indice_actual = abecedario.index(letra)
                indice_encriptado = indice_actual - clave
                if indice_encriptado < 0:
                    indice_encriptado += 27
                texto_encriptado += abecedario[indice_encriptado]
            else:
                texto_encriptado += letra
        return texto_encriptado

#                               Programa

texto = input("Ingrese un texto: ")
clave = int(input("Ingrese una clave: "))
print("\nElija una opción", "\n\n1. Encriptar", "\n2. Desencriptar")
x = int(input())
if x in [1, 2]:
    print("Resultado: ", encrip_desencrip(texto, clave, x))


#                       Des/Encriptado más complejo 
# (se maneja con toda la lista ASCII menos espacios (hecho así a propósito))

def encrip_desencrip(texto, clave, operacion):
    txt_final= []
    if operacion == 1:
        for letra in texto:
            asci = ord(letra)
            if asci == 32:
                final = chr(asci)
                txt_final.append(final)
            else:
                asci += clave
                if asci > 255:
                    asci -= 255
                final = chr(asci)
                txt_final.append(final)
                StrT = "".join(txt_final)
        return StrT
    if operacion == 2:
        for letra in texto:
            asci = ord(letra)
            if asci == 32:
                final = chr(asci)
                txt_final.append(final)
            else:
                asci -= clave
                if asci < 0:
                    asci += 255
                final = chr(asci)
                txt_final.append(final)
                StrT = "".join(txt_final)
        return StrT

#                               Programa
    
texto = input("Ingrese un texto: ")
clave = int(input("Ingrese una clave: "))
print("\nElija una opción", "\n\n1. Encriptar", "\n2. Desencriptar")
x = int(input())
if x in [1, 2]:
    print("Resultado: ", encrip_desencrip(texto, clave, x))

"""

Construir una función que reciba el primer nombre, el segundo nombre y apellido de una persona y
devuelva un string con Apellido, Primer nombre inicial del segundo nombre punto. Tener en cuenta que el
segundo nombre es opcional en ese caso no devuelve la inicial del segundo nombre. Opcional, convertir a
mayúscula la inicial de cada nombre y apellido.

"""

#                                  Funcion

def convertirNombre (nombre, apellido, segundo=0):
    if segundo==0:
        nombre=nombre.capitalize()
        apellido=apellido.capitalize()
        return apellido +", " + nombre
    else:
        nombre=nombre.capitalize()
        segundo=segundo.capitalize()
        apellido=apellido.capitalize()
        return apellido +", " + nombre + " " + segundo[0]+"."

#                                Programa

#Sin segundo nombre
    
n=input("Nombre: ")
a=input("Apellido: ")
         
print(convertirNombre(n,a))

#Con segundo nombre

n=input("Nombre: ")
s=input("Segundo nombre: ")
a=input("Apellido: ")

print(convertirNombre(n,a,s))

"""

Realizar una función para calcular la cantidad de rollos de empapelado que se necesita para empapelar
una habitación. La función recibe las dimensiones de la habitación en metros (largo, ancho y alto), el ancho
del rollo en cm y el largo del rollo en metros, debe devolver un entero con la cantidad de rollos requerida.
Tengan en cuenta que, la habitación es rectangular y la altura es pareja en toda ella. Al empapelar las tiras
se colocan verticalmente, cada tira debe entrar entera en toda la altura de la pared (si lo que sobra en el
rollo es menos que la altura de la habitación, se debe desechar), se puede hacer que una tira cubra una
esquina (la tira se comparte por 2 paredes). Nota: no tener en cuenta las aberturas como ventanas o
puertas. Opcional, si no se especifican las dimensiones el rollo se debe calcular con rollos de 52cm de
ancho y 10 m de largo.

"""

#                                  Funcion
        
def cantRollos (largo, ancho, alto, anchoR, largoR):
    import math
    largototalpared = (largo+ancho)*2
    anchoR = anchoR*0.01
    return math.ceil(largototalpared/(anchoR*(largoR//alto)))

#                                  Programa

#Paredes

l1=float(input("Largo de la habitación (metros): "))
l2=float(input("Ancho de la habitación (metros): "))
a=float(input("Altura de la habitación (metros): "))

#Rollo

x=float(input("Ancho del rollo (centimetros): "))
y=float(input("Largo del rollo (metros): "))

print("Rollos necesarios: ", cantRollos(l1, l2, a, x, y))

"""

Para una aplicación se necesita validar la fecha ingresada por el usuario. El usuario ingresa un entero
para el día, un entero para el mes y un entero para el año (año completo, 4 dígitos). No hay que validar
si los datos ingresados son eneros o no, solo si la fecha es válida. Salida: imprimir “Fecha valida” o
“Fecha invalida”.
NOTA: Está prohibido utilizar la librería estándar datetime.
dia=int(input(“Ingrese el día:”))
mes=int(input(“Ingrese el mes:”))
anio=int(input(“Ingrese el año:”))
#utilizo la variable anio para evitar la ñ en la variable
...continuar el programa.

"""

# Programa

dia=int(input("Ingrese el día: "))
mes=int(input("Ingrese el mes: "))
anio=int(input("Ingrese el año: "))

if (dia>=1 and dia<=31) and (mes>=1 and mes<=12) and (anio>0):

    bisiesto = False
    if (anio % 4 == 0 and anio % 100 !=0) or anio % 400 == 0:
        bisiesto = True

    if dia == 31:
        if mes in [2,4,6,9,11]:
            print("Fecha inválida")
        else: 
            print("Fecha válida")
    if dia == 30:
        if mes==2:
            print("Fecha inválida")
        else:
            print("Fecha válida")
    if dia == 29:
        if mes==2 and bisiesto==True:
            print("Fecha válida")
        elif mes==2 and bisiesto==False:
            print("Fecha inválida")
        elif mes!=2:
            print("Fecha válida")
    if dia <29:
        print("Fecha válida")
else:
    print("Ingrese datos reales.")

"""

En un juego se mide el tiempo que tardó en completarlo en segundos (entero), para el trabajo, se
ingresa por teclado. Se pide que se muestre el tiempo en el formato HH:MM:SS, utilizando 2 cifras
para la hora (HH), 2 cifras para los minutos (MM) y 2 cifras para los segundos (SS).
NOTA: Está prohibido utilizar la librería estándar datetime.
segundos=int(input(“Ingrese el tiempo en segundos:”))
...continuar el programa.
Nota: En las especificaciones del problema falta indicar que debe hace el programa en ciertos casos.
Identificar los casos no especificados. Decidir como debe actuar el programa en esos casos. Informen
sus decisiones y ajusten el programa para implementar sus decisiones.

"""

#Programa

segundos = int(input("Ingrese la cantidad de segundos: "))
 
if segundos<=0:
    print("Los segundos deben ser mayores a 0.")
else:
    minutos = segundos//60
    segundos_resto=segundos%60
    horas = minutos//60
    minutos_resto = minutos%60
    dias = horas//24
    horas_resto = horas%24
    if horas>23:
        print("Dias=", dias, "\nTiempo adicional= ",
              (str(horas_resto).zfill(2)),":",
              (str(minutos_resto).zfill(2)),":",
              (str(segundos_resto).zfill(2)))
    else:
        print((str(horas_resto).zfill(2)),":",
              (str(minutos_resto).zfill(2)),":",
              (str(segundos_resto).zfill(2)))

"""

En una fábrica, una balanza automática pesa tandas de galletitas. Para el ejercicio, los valores se
ingresan por teclado. Las galletitas se acumulan, cuando el peso acumulado es igual o superior al peso
que debe tener el paquete, se informa por pantalla para cambiar el paquete. El peso del paquete debe
ser un parámetro en el programa y puede cambiarse en cada ejecución.

"""

# Programa

peso=0
paquete=int(input("Ingrese la capacidad del paquete (gramos): "))
galleta=int(input("Ingrese el peso de la tanda (gramos): "))
if paquete and galleta >0:
    while galleta<paquete:
        peso += galleta
        paquete -= galleta
        print("\nPeso total: ", peso, "gramos.",
          "\nCapacidad restante del paquete: ", paquete, "gramos.")
        galleta=int(input("\nIngrese el peso de la sig. tanda (gramos): "))
    peso += galleta
    print("\nCapacidad máxima alcanzada.","\nPeso total: ", peso,
          "\n\nCambie el paquete.")
else:
    print("\nAmbos valores deben ser mayores a 0.")

"""

En una fábrica de panificados se tiene un silo para almacenar la harina. La capacidad del silo debe ser
un parámetro del programa y se puede cambiar en cada ejecución. Un operario le ingresa la cantidad
de harina requerida para la preparación (ingreso por teclado). El programa debe informar si la
cantidad de harina del silo suficiente para realizar la preparación. Si la cantidad es suficiente lo informa
y actualiza la cantidad harina restante en el silo. Si no es suficiente, lo informa y cancela la
preparación.

"""

# Programa


silo=int(input("Ingrese la capacidad del silo (gramos): "))
harina=int(input("Ingrese la cantidad de harina necesaria (gramos): "))

if harina and silo !=0:
    while harina<=silo:
        silo -= harina
        print("\nLa cantidad de harina es suficiente para la preparación.",
          "\nCantidad de harina restante en silo: ", silo, "gramos.")
        harina=int(input("\nIngrese la cantidad de harina necesaria (gramos): "))
    print("\nHarina insuficiente.", "\nPreparación cancelada.")
else:
    print("\nLos valores no pueden ser 0.")




