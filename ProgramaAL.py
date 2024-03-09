# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:01:51 2023

@author: Sebastian Adan Cahuin Huaman
"""
#%%
#  SEMANAS 01 _ 02 
#  Comparación de los lenguajes de programación JAVA, PYTHON y C 
#%% Operaciones Básicas:
# 1. Realiza la suma, resta, multiplicación y división de 

#  PEDIMOS AL USUARIO PARA QUE INGRESE DOS NUMEROS
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# REALIZAMOS LAS OPERACIONES 
suma = num1 + num2   # SUMA
resta = num1 - num2   #RESTA
multiplicacion = num1 * num2  #MULTIPLICACION

if num2 != 0: # ASEGURAMOS QUE EL SEGUNDO NUM SEA DIFERENTE DE SERO
    division = num1 / num2 # DIVIDIMOS AMBOS NUMEROS
else:
    division = "No es posible dividir por cero." # SI EL SEGUNO VALOR ES CERO NOS DEVUELVE ESTE TEXTO

# IMPRIMIMOS LOS RESULTADOS
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#%%  Verificación de Número Par o Impar:
# 2.Solicita un número al usuario y determina si es par o impar.

# PEDIMOS AL USUARION QUE INGRESE UN NUMERO
numero = int(input("Ingresa un número: "))

# DETERMINAMOS SI ES PAR O IMPAR
if numero % 2 == 0:
    print(f"{numero} es un número par.") #IMPRIME QUE ES UN PAR
else:
    print(f"{numero} es un número impar.") #IMPRIME QUE ES UN IMPAR
    
#%% Área de un Triángulo: 
# 3. Pide la base y la altura de un triángulo al usuario y calcula su área. 

# PEDIMOS AL USUARION QUE NOS DE VALIRES PARA LA ALTURA Y BASE  DEL TRIANGULO
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# IMPLEMENTAMOS LA FORMULA PARA HALLAR EL AREA DEL TRIANGULO
area_triangulo = (base * altura) / 2

# IMPRIMIMOS EL RESULTADO
print(f"El área del triángulo con base {base} y altura {altura} es: {area_triangulo:.2f}")
    

#%% Calculadora de Factorial: 
# 4. Crea una función que calcule la factorial de un número. 

def factorial(n):
    if n == 0 or n == 1: #verificamos si el valor de n es igual a 0 o 1.
        return 1
    else:
        return n * factorial(n-1)# calculamos el factorial de n multiplicándolo por el factorial de n-1

# PEDIMOS UN NUMERO AL USUARIO
numero = int(input("Ingresa un número: "))

# CALCULAMOS EL FACTORIAL Y MOSTRAMOS EL RESULTADO
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

#%% Número Primo: 
# 5. Verifica si un número ingresado por el usuario es primo o no.

def es_primo(numero):
    if numero < 2:#Comprueba si el número es menor que 2
        return False #Si el número es menor que 2, devuelve False
    for i in range(2, int(numero**0.5) + 1):#Inicia un bucle for que itera sobre los valores de i desde 2 hasta la raíz cuadrada entera de numero más 1.
        if numero % i == 0:# En cada iteración, verifica si el número es divisible por i
            return False
    return True

# SOLICITAMMOS INGRESAR UN NUMERO
numero_usuario = int(input("Ingresa un número: "))

# VERIFICAMOS SI EL NUMERO ES PRIMO Y NOS IMPRIME EL RESULTADO
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")


#%% Inversión de Cadena:
# 6. Toma una cadena de texto y muestra su inversión. 

def invertir_cadena(cadena):
    cadena_invertida = cadena[::-1]# Utilizamos la notación de rebanado para crear una versión invertida de la cadena
    return cadena_invertida

# PEDIMOS AL USUARIO QUE INGRESE UNA CADENA
cadena_original = input("Ingresa una cadena de texto: ")

# OBTENEMOS LA CADENA INVERTIDA Y NOS MUESTRA EL RESULTADO
resultado = invertir_cadena(cadena_original)
print(f"La cadena invertida es: {resultado}")

#%% Suma de Números Pares: 
# 7.Calcula la suma de los números pares en un
# rango especificado por el usuario.

# PEDIMOS AL USUARIO QUE INGRESE 2 NUMERO CON UN RANGO
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))

# INICIAMOS LA SUMA Y GUARDAMOS EL VALOR EN UN VARIABLE
suma_pares = 0

# CALCULAMOS LA SUMA DE LOS NUMEROS PARES EN EL RANGO ESCRITO
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero

#IMPRIMIMOS EL RESULTADO
print(f"La suma de los números pares en el rango [{inicio}, {fin}] es: {suma_pares}")


#%% Lista de Cuadrados:
# 8.  Crea una lista de los cuadrados de los primeros 10 números naturales.

# CREAMOS LA LISTA DE LOS 10 PRIMEROS NUMERO CALCULANDO SUS CUADRADOS
cuadrados = [n**2 for n in range(1, 11)]

# IMPRIMIMOS LOS RESULTADOS
print("Lista de cuadrados de los primeros 10 números naturales:")
print(cuadrados)


#%% Contador de Vocales: 
# 9. Cuenta el número de vocales en una cadena de texto. 

# SOLCITAMOS AL USUARIO QUE INGRESE UN TEXTO
cadena = input("Ingresa una cadena de texto: ")

# INICIAMOS EL CONTADOR DE LAS VOCALES
contador_vocales = 0

# DEFINIMOS LAS VOCALES MAYUSCULAS O MINUSCULAS
vocales = "aeiouAEIOU"

# CONTAMOS EL NUMERO DE VOCALES EN LA CADENA
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

# IMPRIMIMOS EL RESULTADO
print(f"El número de vocales en la cadena es: {contador_vocales}")



#%% Números de la Serie Fibonacci:
# 10.Genera los primeros 10 números de la serie Fibonac

#CREMOS LA FUNCION PARA GENERAR LOS PRIMEROS N NUMERO DE FIBONACCI
def fibonacci(n):
    fib_series = [0, 1]  # Inicializamos la serie con los primeros dos números
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# OBTENEMOS LOS 10 PRIMEROS NUMEROS

primeros_10_fibonacci = fibonacci(10)

# MOSTRANMOS EL RESLTADO IMPRIMIENDONOS LA RESPUESTA

print("Primeros 10 números de la serie Fibonacci:")
print(primeros_10_fibonacci)

#%% Ordenamiento de Lista: 
#11.Ordena una lista de números ingresados por el usuario de menor a mayor.

# PEDIMOS AL USUARIO QUE INGRESE NUMEROS
entrada_usuario = input("Ingresa una lista de números: ")

# CONVERTIMOS LOS NUMEROS INGRESADOS EN UNA LISTA
numeros = [float(numero) for numero in entrada_usuario.split()]

# ORDENAMOS LOS NUMERO DE LA LINSTA DE MENOR A MAYOR
numeros_ordenados = sorted(numeros)

# IMPRIMIMOS LA RESPUESTA
print("Lista ordenada de menor a mayor:", numeros_ordenados)

#%% Palíndromo: 
# 12. Verifica si una palabra ingresada por el usuario es un palíndromo. 


def es_palindromo(palabra):
    palabra = palabra.lower()  # Convierte la cadena de entrada a minúsculas
    palabra_invertida = palabra[::-1]   # Crea una versión invertida de la cadena
    
    return palabra == palabra_invertida

# SOLICITAMOS AL USUARIO QUE INGRESE UNA PALABRA
palabra_usuario = input("Ingresa una palabra: ")

# VEREFICAMOS SI LA PALABRA ES UN PALINDROMO Y MOSTRAMOS EL RESULTADO
if es_palindromo(palabra_usuario):
    print(f"{palabra_usuario} es un palíndromo.")
else:
    print(f"{palabra_usuario} no es un palíndromo.")
    
    
#%% Generador de Tablas de Multiplicar: 
# 13. Crea un programa que genere la tabla de multiplicar 
#     de un número ingresado por el usuario.

# PEDIMOS AL USUARIO QUE INGRESE UN NUMERO
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11): #Esto inicia un bucle
    resultado = numero * i #: En cada iteración del bucle, calcula el resultado de la multiplicación del número dado
    print(f"{numero} x {i} = {resultado}")




#%% Cálculo del Área de un Círculo: 
# 14. Pide el radio de un círculo al usuario y calcula su área. 

import math

# PIDE UN RADIO AL USUARIO
radio = float(input("Ingresa el radio del círculo: "))

# CALCULAMOS EL AREA DEL CIRCULO CON LA FORMULA
area_circulo = math.pi * radio**2

# IMPRIME EL RESULTADO
print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")


#%% Suma de Dígitos: 
# 15.  Toma un número entero y calcula la suma de sus dígitos.

# PEDIMOS AL USUARION QUE INGRESE UN NUMERO ENTERO
numero = int(input("Ingresa un número entero: "))

# CALCULAMOS LA SUMA DE LOS DIGITOS
suma_digitos = sum(int(digito) for digito in str(abs(numero)))

# IMPRIME EL RESULTADO
print("La suma de los dígitos es:", suma_digitos)


#%%
# SEMANA 03 _ 04
# Recursividad – Arreglos y Matrices 
#%% Ejercicio 1:
# Escribe una función recursiva que imprima los números pares del 1 al 100. 

def imprimir_pares(n):
    if n <= 100:#Verifica si n es menor o igual a 100
        if n % 2 == 0: # verificamos si n es par utilizando el operador de módulo % 
            print(n)
        imprimir_pares(n + 2) #Esto se hace para pasar al siguiente número par

imprimir_pares(2)


#%% Ejercicio 2:
# Escribe una función recursiva que imprima la suma de los números del 1 al n. 

def suma_hasta_n(n):#DEFINIMOS LA FUNCION
    if n == 1: #Se comprueba si n es igual a 1
        return #Si n es igual a 1, se devuelve 1,
    else:
        return n + suma_hasta_n(n - 1) # Si n no es igual a 1, entonces se devuelve la suma de n y el resultado de llamar recursivamente a la función suma_hasta_n con n - 1

resultado = suma_hasta_n(20)
print(f"La suma de los números del 1 al 20 es: {resultado}")

#%% Ejercicio 3: 
#Escribe una función recursiva que imprima la pirámide de números del 1 al n. 

def imprimir_piramide(n, current_row=1, current_num=1):
    if current_row > n:
        return
    
    if current_num > current_row:
#AVANZA A LA SIGUINENTE FILA
        print()  
        imprimir_piramide(n, current_row + 1, 1)
    else:
#IMPRIME EL NUMERO Y LLAMA A LA FUNCION PARA EL SIGUINETE NUMERO DE LA MISMA FILA
        print(current_num, end=" ")
        imprimir_piramide(n, current_row, current_num + 1)

# LLAMAMOS A LA FUNCION CON UN EJEMPLO 4
imprimir_piramide(4)

#%% Ejercicio 4
# Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.

def imprimir_piramide_invertida(n, current_row=1, current_num=1):#define una función llamada imprimir_piramide_invertida
    if current_row > n:#Comprueba si current_row es mayor que n
        return
    
    if current_num > current_row: # comprobación de si current_row es mayor que n
        # Avanza a la siguiente fila
        print()  
        imprimir_piramide_invertida(n, current_row + 1, 1)
    else:
        # Imprime el número invertido y llama a la función para el siguiente número en la misma fila
        print(n - current_num + 1, end=" ")
        imprimir_piramide_invertida(n, current_row, current_num + 1)

# Llamamos a la función con un ejemplo (por ejemplo, n=4)
imprimir_piramide_invertida(4)


#%% Ejercicio 5:
# Escribe una función recursiva que imprima la tabla de multiplicar del n.

def tabla_multiplicar(n, multiplicador=1): #define una función llamada tabla_multiplicar que toma dos argumentos: n y multiplicador
    if multiplicador > 10:#verifica si el multiplicador actual es mayor que 10
        return
    else: #Se realiza el cálculo de una sola entrada de la tabla de multiplicar, se calcula el resultado multiplicando n
        resultado = n * multiplicador
        print(f"{n} x {multiplicador} = {resultado}")
        tabla_multiplicar(n, multiplicador + 1)

#TOMAMOS COMO ARGUMENTO EL NUMERO 5
tabla_multiplicar(5)



#%%Ejercicio 6:
# Crea una matriz de números reales

#CREAMOS UNA MATRIZ 3 X 3
matriz = [
    [1, 5, 1],
    [9, 5, 6],
    [2, 8, 3]
]

# IMPRIMIMOS LA MATRIZ
for ejercicio in matriz:#En cada iteración del bucle, la variable ejercicio toma el valor de cada elemento de la lista matriz
    print(ejercicio)
#%% Ejercicio 7:
#Crea una matriz de números complejos.

matriz_compleja = [ #CREAMOS UNA VARIBLE LLAMADA MARIZ_COMPLEJA
    [complex(1, 2), complex(3, 4)],# ESTAS DOS SON UNAS SUBLISTAS QUE CONTIENEN
    [complex(5, 6), complex(7, 8)] #NUMEROS COMPLEJOS
]
#ITERAMOS SOBRE CADA ELEMENTO DE LA LISTA
for fila in matriz_compleja:
    print(fila)

#%%Ejercicio 8:
#Crea una matriz de matrices.

# creamos una matriz de matrices (3x3)
matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
]

for matriz in matrices: # iteramos sobre cada elemento de la lista matrices
    for fila in matriz: # itera sobre cada elemento de la matriz actual
        print(fila)
    print() # Imprimimos la matriz de matrices
    
#%%Ejercicio 9:
#Accede al elemento central de una matriz.

#CREAMOS LA MATRIZ 3X3
matriz_impar = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# OBTENEMOS EL NUMERO DE FILAS Y COLUMNAS
num_filas = len(matriz_impar)
num_columnas = len(matriz_impar[0])

#ACCEDEMOS AL VALOR CENTRAL
elemento_central = matriz_impar[num_filas // 2][num_columnas // 2]
#IMPRIMIMOS EL VALOR CENTRAL
print("Elemento central:", elemento_central)
#%%Ejercicio 10:
#Suma dos matrices de diferentes tamaños.

def sumar_matrices(matriz_grande, matriz_pequena):# DEFINIMOS LA FUNCION CON SUSU ARGUMENTOS
#OBTENEMOS LAS DIMENSIONES DE AMBAS MATRICES
    filas_grande, columnas_grande = len(matriz_grande), len(matriz_grande[0])
    filas_pequena, columnas_pequena = len(matriz_pequena), len(matriz_pequena[0])
#VERIFICAMOS SI LA MATRIZ PEQUEÑA ES SUBMATRIZ DE LA MATRIZ GRANDE
    if filas_pequena > filas_grande or columnas_pequena > columnas_grande:
        print("No se puede sumar. La matriz pequeña no es submatriz de la matriz grande.")
        return None
    
#CREAMOS UNA NUEVA MATRIZ PARA ALMACENAR LA SUMA
    resultado = []
    for i in range(filas_grande):
        fila_resultado = []
        for j in range(columnas_grande):
            if i < filas_pequena and j < columnas_pequena:
                fila_resultado.append(matriz_grande[i][j] + matriz_pequena[i][j])
            else:
                fila_resultado.append(matriz_grande[i][j])
        resultado.append(fila_resultado)

    return resultado

#DEFINIMOS LA MATRIZ GRANDE
matriz_grande = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#DEFINIMOS LA MATRIZ PEQUEÑA
matriz_pequena = [
    [10, 20],
    [30, 40]
]
#LLAMAMOS A LA FUNCION Y LAS MATRICES
resultado_suma = sumar_matrices(matriz_grande, matriz_pequena)

if resultado_suma is not None:
    for fila in resultado_suma:
        print(fila)
#%% Ejercicio 11:
# Multiplica una matriz por un número. 

def multiplicar_matriz_por_escalar(matriz, escalar):#DEFINIMOS LA FUNCION CON SUS PARAMETROS
    resultado = []#INICIAMOS CON UNA LISTA VACIA

    for fila in matriz:#ITERAMOS SOBRE CADA FILA DE LA MATRIZ
    # multiplicamos cada elemento de la fila por el escalar
        fila_resultado = [elemento * escalar for elemento in fila]
        resultado.append(fila_resultado)#construye la nueva matriz con todas las filas multiplicadas por el escalar

    return resultado
#DEFINIMOS LA MATRIZ
matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#DEFINIMO EL ESCALAR PAR AMULTIPLICAR L MATRIZ
escalar = 2
#LLAMAMOS A LA FUNCION, A LA MATRIZ Y AL ESCALAR Y LA GUARDAMOS EN UN RESULTADO
matriz_resultado = multiplicar_matriz_por_escalar(matriz_original, escalar)
#Itera sobre cada fila de la matriz resultado y las imprime
for fila in matriz_resultado:
    print(fila)

#%%Ejercicio 12:
#Calcula la media de los elementos de una matriz. 

def calcular_media_matriz(matriz):#DEFINIMOS LA FUNCION CON SU PARAMETRO MATRIZ
#INICIALIZAMOS 2 VARIBLES DESDE 0
    total_elementos = 0
    suma_elementos = 0
#El bucle externo itera sobre cada fila de la matriz, y el bucle interno itera sobre cada elemento de la fila actual
    for fila in matriz:
        for elemento in fila:
            suma_elementos += elemento
            total_elementos += 1
# se verifica si el total de elementos es igual a 0
    if total_elementos == 0:
        print("La matriz está vacía. No se puede calcular la media.")
        return None
    else: #Si la matriz no está vacía, se calcula la media dividiendo la suma total de elementos
        media = suma_elementos / total_elementos
        return media

#DEFINIMOS LA MATRIZ
matriz_ejemplo = [
    [4, 6, 3],
    [4, 1, 9],
    [3, 8, 2]
]
#LLAMAMOS A LAFUNCION A LA MATRIZ COMO ARGUMENTO
media_matriz = calcular_media_matriz(matriz_ejemplo)
#Si el resultado de calcular_media_matriz no esta vacia, se imprime la media de los elementos de la matriz.
if media_matriz is not None:
    print(f"La media de los elementos de la matriz es: {media_matriz}")


# %% 
#Semana 3 y 4 la ultima parte"""
# %% 
"""Ejercicio 1:
Crea una matriz de números aleatorios de tamaño 100x100."""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

# Creamos una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

# Mostramos la matriz generada
print("Matriz de números aleatorios de tamaño 100x100:")  # Imprimimos un mensaje indicando la naturaleza de la matriz
print(matriz_aleatoria)  # Imprimimos la matriz de números aleatorios
# %% 

"""Ejercicio 2: Calcula la media, la mediana y la desviación estándar 
de los elementos de una matriz."""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

# Creamos una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

# Calculamos la media de los elementos de la matriz
media = np.mean(matriz_aleatoria)

# Calculamos la mediana de los elementos de la matriz
mediana = np.median(matriz_aleatoria)

# Calculamos la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz_aleatoria)

# Mostramos los resultados
print("Media de los elementos de la matriz:", media)  # Mostramos la media de los elementos de la matriz
print("Mediana de los elementos de la matriz:", mediana)  # Mostramos la mediana de los elementos de la matriz
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)  # Mostramos la desviación estándar de los elementos de la matriz

# %% 

"""Ejercicio 3:
Escribe una función que encuentre el elemento máximo de una matriz."""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def encontrar_maximo(matriz):
    # Función para encontrar el elemento máximo de una matriz
    maximo = np.max(matriz)  # Utilizamos la función np.max() de NumPy para encontrar el elemento máximo
    return maximo  # Devolvemos el elemento máximo encontrado

# Creamos una matriz de ejemplo de tamaño 3x3 utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz_ejemplo = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

# Llamamos a la función para encontrar el máximo de la matriz de ejemplo
maximo_encontrado = encontrar_maximo(matriz_ejemplo)

# Mostramos el máximo encontrado
print("El elemento máximo de la matriz es:", maximo_encontrado)

# %% 

"""Ejercicio 4:
Escribe una función que encuentre la submatriz de mayor suma de una matriz"""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def encontrar_submatriz_maxima(matriz):
    # Función para encontrar la submatriz de mayor suma dentro de una matriz dada
    max_suma = float('-inf')  # Inicializamos la máxima suma con un valor negativo infinito
    submatriz_maxima = None  # Inicializamos la submatriz de mayor suma como vacía

    # Recorremos todas las submatrices posibles dentro de la matriz
    for i in range(len(matriz)):  # Iteramos sobre las filas de la matriz
        for j in range(len(matriz[0])):  # Iteramos sobre las columnas de la matriz
            for k in range(i, len(matriz)):  # Definimos el límite superior de las filas de la submatriz
                for l in range(j, len(matriz[0])):  # Definimos el límite superior de las columnas de la submatriz
                    # Calculamos la suma de la submatriz actual
                    suma_actual = np.sum(matriz[i:k+1, j:l+1])

                    # Si la suma actual es mayor que la máxima suma registrada hasta ahora
                    if suma_actual > max_suma:
                        max_suma = suma_actual  # Actualizamos la máxima suma
                        submatriz_maxima = matriz[i:k+1, j:l+1]  # Actualizamos la submatriz de mayor suma

    return submatriz_maxima  # Devolvemos la submatriz de mayor suma encontrada

# Creamos una matriz de ejemplo de tamaño 4x4 utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz_ejemplo = np.array([[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]])

# Llamamos a la función para encontrar la submatriz de mayor suma
submatriz_maxima_encontrada = encontrar_submatriz_maxima(matriz_ejemplo)

# Mostramos la submatriz de mayor suma encontrada
print("La submatriz de mayor suma es:")
print(submatriz_maxima_encontrada)

# %% 

"""Ejercicio 5:
Escribe una función que encuentre la matriz de covarianza de dos matrices"""

import numpy as np  # Importamos la librería NumPy y la renombramos como np

def matriz_covarianza(matriz1, matriz2):
    # Función para calcular la matriz de covarianza entre dos matrices dadas
    covarianza = np.cov(matriz1, matriz2)  # Calculamos la matriz de covarianza utilizando np.cov()
    return covarianza  # Devolvemos la matriz de covarianza calculada

# Creamos dos matrices de ejemplo utilizando np.array que 
#Es una función de la librería NumPy que crea matrices multidimensionales Y 
#Permite convertir listas bidimensionales en matrices NumPy.
matriz1 = np.array([[1, 2, 3],  # Creamos la matriz1 con 2 filas y 3 columnas
                     [4, 5, 6]])

matriz2 = np.array([[7, 8, 9],  # Creamos la matriz2 con 2 filas y 3 columnas
                     [10, 11, 12]])

# Llamamos a la función para encontrar la matriz de covarianza de las dos matrices
matriz_cov = matriz_covarianza(matriz1, matriz2)

# Mostramos la matriz de covarianza encontrada
print("Matriz de covarianza de las dos matrices:")
print(matriz_cov)


# %% 
"""semana 5"""
# %%  
"""1. Escriba una función que reciba un conjunto de números y devuelva un conjunto con 
los números primos."""

def es_primo(numero):
    # Verifica si el número es menor o igual a 1
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Itera sobre los números desde 2 hasta la raíz cuadrada del número + 1
    for i in range(2, int(numero ** 0.5) + 1):
        # Si el número es divisible por cualquier número en este rango, no es primo
        if numero % i == 0:
            return False

    return True  # Si el número no es divisible por ningún número, es primo


def numeros_primos(conjunto):
    primos = set()  # Inicializa un conjunto para almacenar los números primos

    # Itera sobre cada número en el conjunto dado
    for num in conjunto:
        # Verifica si el número es primo utilizando la función es_primo()
        if es_primo(num):
            # Si el número es primo, agrégalo al conjunto de números primos
            primos.add(num)

    return primos  # Devuelve el conjunto de números primos


# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}

# Imprime el conjunto original
print("Conjunto original:", conjunto_de_numeros)

# Llama a la función numeros_primos para obtener el conjunto de números primos dentro del conjunto dado
numeros_primos_en_conjunto = numeros_primos(conjunto_de_numeros)

# Imprime el conjunto de números primos
print("Conjunto de números primos:", numeros_primos_en_conjunto)




# %%  
"""2. Escriba una función que reciba un conjunto de palabras y devuelva 
un conjunto con las palabras que comienzan con una letra determinada."""

def palabras_con_letra_inicial(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra inicial y devuelve las palabras que comienzan con esa letra
    palabras_con_letra = set()  # Inicializamos un conjunto para almacenar las palabras que comienzan con la letra dada
    
    # Iteramos sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Comprobamos si la palabra comienza con la letra dada, ignorando mayúsculas y minúsculas
        if palabra.lower().startswith(letra.lower()):
            palabras_con_letra.add(palabra)  # Agregamos la palabra al conjunto si cumple la condición
    
    return palabras_con_letra  # Devolvemos el conjunto de palabras que comienzan con la letra especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_inicial = "P"

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_con_letra_inicial para obtener las palabras que comienzan con la letra dada
palabras_con_letra_dada = palabras_con_letra_inicial(conjunto_de_palabras, letra_inicial)

# Imprimimos las palabras que comienzan con la letra dada
print("Palabras que comienzan con la letra '{}':".format(letra_inicial), palabras_con_letra_dada)

# %%  
"""3. Escriba una función que reciba un conjunto de números y devuelva 
un conjunto con los números que son divisibles por un número determinado."""

def numeros_divisibles(conjunto_numeros, divisor):
    # Función que recibe un conjunto de números y un divisor, y devuelve los números divisibles por el divisor
    numeros_divisibles = set()  # Inicializamos un conjunto para almacenar los números divisibles
    
    # Iteramos sobre cada número en el conjunto dado
    for numero in conjunto_numeros:
        # Verificamos si el número es divisible por el divisor
        if numero % divisor == 0:
            numeros_divisibles.add(numero)  # Agregamos el número al conjunto si es divisible por el divisor
    
    return numeros_divisibles  # Devolvemos el conjunto de números divisibles por el divisor

# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3

# Imprimimos el conjunto de números original
print("Conjunto de números original:", conjunto_de_numeros)

# Llamamos a la función numeros_divisibles para obtener los números divisibles por el divisor dado
numeros_divisibles_por_divisor = numeros_divisibles(conjunto_de_numeros, divisor)

# Imprimimos los números divisibles por el divisor
print("Números divisibles por {}: ".format(divisor), numeros_divisibles_por_divisor)

# %%  
"""4. Escriba una función que reciba dos conjuntos de números y devuelva 
un conjunto con los números que están en ambos conjuntos."""

def numeros_en_comun(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en ambos conjuntos
    numeros_comunes = conjunto1.intersection(conjunto2)
    # La función intersection() devuelve un conjunto que contiene los elementos que están presentes en ambos conjuntos
    
    return numeros_comunes
    # Devolvemos el conjunto que contiene los números comunes a ambos conjuntos

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_comun para encontrar los números que están en ambos conjuntos
numeros_comunes = numeros_en_comun(conjunto1, conjunto2)

# Imprimimos los números en común
print("Números en común:", numeros_comunes)

# %%  
"""5. Escriba una función que reciba dos conjuntos de números y 
devuelva un conjunto con los números que están en el primer conjunto 
pero no en el segundo."""

def numeros_en_primero_no_en_segundo(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en el primer conjunto pero no en el segundo
    numeros_diferentes = conjunto1.difference(conjunto2)
    # La función difference() devuelve un conjunto que contiene los elementos que están en el primer conjunto pero no en el segundo
    return numeros_diferentes
    # Devolvemos el conjunto que contiene los números que están en el primer conjunto pero no en el segundo

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_primero_no_en_segundo para encontrar los números que están en el primero pero no en el segundo conjunto
numeros_diferentes = numeros_en_primero_no_en_segundo(conjunto1, conjunto2)

# Imprimimos los números que están en el primero pero no en el segundo conjunto
print("Números en el primero pero no en el segundo:", numeros_diferentes)

# %%  
"""6. Escriba una función que reciba dos conjuntos de números y 
devuelva un conjunto con los números que están en el segundo conjunto
 pero no en el primero."""

def numeros_en_segundo_no_en_primero(conjunto1, conjunto2):
    # Función que recibe dos conjuntos de números y devuelve los números que están en el segundo conjunto pero no en el primero
    numeros_diferentes = conjunto2.difference(conjunto1)
    # La función difference() devuelve un conjunto que contiene los elementos que están en el segundo conjunto pero no en el primero
    return numeros_diferentes
    # Devolvemos el conjunto que contiene los números que están en el segundo conjunto pero no en el primero

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Imprimimos los conjuntos originales
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Llamamos a la función numeros_en_segundo_no_en_primero para encontrar los números que están en el segundo pero no en el primer conjunto
numeros_diferentes = numeros_en_segundo_no_en_primero(conjunto1, conjunto2)

# Imprimimos los números que están en el segundo pero no en el primer conjunto
print("Números en el segundo pero no en el primero:", numeros_diferentes)

# %%  
"""7. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son anagramas"""

def encontrar_anagramas(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve un conjunto con las palabras que son anagramas

    anagramas = set()  # Inicializamos un conjunto para almacenar los anagramas encontrados
    conteo_palabras = {}  # Creamos un diccionario para almacenar el conteo de letras en cada palabra

    # Iteramos sobre cada palabra en el conjunto dado
    for palabra in conjunto_palabras:
        # Convertimos la palabra a una tupla de letras ordenadas alfabéticamente
        letras_ordenadas = tuple(sorted(palabra))

        # Agregamos la tupla de letras ordenadas al diccionario y aumentamos su conteo
        conteo_palabras[letras_ordenadas] = conteo_palabras.get(letras_ordenadas, 0) + 1

    # Iteramos sobre los elementos del diccionario
    for letras_ordenadas, conteo in conteo_palabras.items():
        # Si hay más de una palabra con las mismas letras ordenadas, son anagramas
        if conteo > 1:
            # Iteramos sobre las palabras con las letras ordenadas dadas
            for palabra in conjunto_palabras:
                # Si la palabra tiene las letras ordenadas correspondientes, la agregamos al conjunto de anagramas
                if tuple(sorted(palabra)) == letras_ordenadas:
                    anagramas.add(palabra)

    return anagramas

# Ejemplo de uso:
conjunto_de_palabras = {"roma", "amor", "casa", "saca", "perro", "arroz"}

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras:", conjunto_de_palabras)

# Llamamos a la función encontrar_anagramas() y mostramos los resultados
print("Anagramas encontrados:", encontrar_anagramas(conjunto_de_palabras))

# %%  
"""8. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son palíndromos."""

def palabras_palindromos(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve las palabras que son palíndromos
    palindromos = set()  # Inicializamos un conjunto para almacenar los palíndromos
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if palabra == palabra[::-1]:   # Comprobamos si la palabra es igual a su reverso
            palindromos.add(palabra)    # Si la palabra es igual a su reverso, la añadimos al conjunto de palíndromos
            
    return palindromos  # Devolvemos el conjunto de palabras que son palíndromos

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python"}

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_palindromos() y mostramos los palíndromos encontrados
print("Palíndromos en el conjunto:", palabras_palindromos(conjunto_de_palabras))


# %%  
"""9. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que tienen una longitud determinada."""

def palabras_longitud(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras y una longitud, y devuelve las palabras con la longitud especificada
    palabras_con_longitud = set()  # Inicializamos un conjunto para almacenar las palabras con la longitud especificada
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if len(palabra) == longitud:   # Comprobamos si la longitud de la palabra es igual a la longitud especificada
            palabras_con_longitud.add(palabra)  # Si la longitud de la palabra es la requerida, la añadimos al conjunto
            
    return palabras_con_longitud  # Devolvemos el conjunto de palabras con la longitud especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
longitud_deseada = 5

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_longitud() y mostramos las palabras con la longitud deseada
print("Palabras con longitud {}: ".format(longitud_deseada), palabras_longitud(conjunto_de_palabras, longitud_deseada))

# %% 
"""10. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que contienen una letra determinada."""

def palabras_con_letra(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra, y devuelve las palabras que contienen la letra especificada
    palabras_con_la_letra = set()  # Inicializamos un conjunto para almacenar las palabras con la letra especificada
    
    for palabra in conjunto_palabras:  # Iteramos sobre cada palabra en el conjunto dado
        if letra in palabra:   # Comprobamos si la letra está presente en la palabra
            palabras_con_la_letra.add(palabra)  # Si la letra está presente, añadimos la palabra al conjunto
    
    return palabras_con_la_letra  # Devolvemos el conjunto de palabras que contienen la letra especificada

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_deseada = 'a'

# Imprimimos el conjunto de palabras original
print("Conjunto de palabras original:", conjunto_de_palabras)

# Llamamos a la función palabras_con_letra() y mostramos las palabras que contienen la letra deseada
print("Palabras que contienen la letra '{}': ".format(letra_deseada), palabras_con_letra(conjunto_de_palabras, letra_deseada))
 
# %%  
"""11. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están ordenados de menor a mayor"""

def numeros_ordenados_menor_a_mayor(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de menor a mayor
    numeros_ordenados = sorted(conjunto_numeros)  # Ordenamos el conjunto de números
    return set(numeros_ordenados)  # Devolvemos el conjunto ordenado de menor a mayor

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados = numeros_ordenados_menor_a_mayor(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados de menor a mayor:", numeros_ordenados)  # Mostramos el resultado ordenado

# %%  
"""12. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están ordenados de mayor a menor"""

def numeros_ordenados_mayor_a_menor(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de mayor a menor
    numeros_ordenados = sorted(conjunto_numeros, reverse=True)  # Ordenamos el conjunto de números en orden descendente
    return set(numeros_ordenados)  # Devolvemos el conjunto ordenado de mayor a menor

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados = numeros_ordenados_mayor_a_menor(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados de mayor a menor:", numeros_ordenados)  # Mostramos el resultado ordenado

# %%  
"""13. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están duplicados."""

def numeros_duplicados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números duplicados
    numeros_duplicados = set()  # Inicializamos un conjunto para almacenar los números duplicados
    numeros_vistos = set()  # Inicializamos un conjunto para almacenar los números que ya hemos visto

    for numero in conjunto_numeros:  # Iteramos sobre cada número en el conjunto dado
        if numero in numeros_vistos:  # Verificamos si ya hemos visto este número antes
            numeros_duplicados.add(numero)  # Si el número ya ha sido visto, lo agregamos al conjunto de duplicados
        else:
            numeros_vistos.add(numero)  # Si el número no ha sido visto antes, lo agregamos al conjunto de vistos

    return numeros_duplicados  # Devolvemos el conjunto de números duplicados

# Ejemplo de uso:
conjunto_de_numeros = {1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_duplicados_encontrados = numeros_duplicados(conjunto_de_numeros)  # Llamamos a la función
print("Números duplicados:", numeros_duplicados_encontrados)  # Mostramos los números duplicados encontrados

# %%  
"""14. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que no están duplicados."""

def numeros_no_duplicados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números que no están duplicados
    numeros_no_duplicados = set()  # Inicializamos un conjunto para almacenar los números que no están duplicados
    numeros_vistos = set()  # Inicializamos un conjunto para almacenar los números que ya hemos visto
    duplicados = set()  # Inicializamos un conjunto para almacenar los números duplicados

    for numero in conjunto_numeros:  # Iteramos sobre cada número en el conjunto dado
        if numero in numeros_vistos:  # Verificamos si ya hemos visto este número antes
            duplicados.add(numero)  # Si el número ya ha sido visto, lo agregamos al conjunto de duplicados
        else:
            numeros_vistos.add(numero)  # Si el número no ha sido visto antes, lo agregamos al conjunto de vistos

    numeros_no_duplicados = conjunto_numeros - duplicados  # Obtenemos los números que no están duplicados

    return numeros_no_duplicados  # Devolvemos el conjunto de números que no están duplicados

# Ejemplo de uso:
conjunto_de_numeros = {1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_no_duplicados_encontrados = numeros_no_duplicados(conjunto_de_numeros)  # Llamamos a la función
print("Números no duplicados:", numeros_no_duplicados_encontrados)  # Mostramos los números no duplicados encontrados

# %%  
"""15. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que son primos y están ordenados 
de menor a mayor"""

def es_primo(numero):
    # Función que verifica si un número es primo
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobamos si el número es divisible por algún número entre 2 y su raíz cuadrada
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible, el número no es primo

    return True  # Si no se encontraron divisores, el número es primo

def numeros_primos_ordenados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números primos ordenados de menor a mayor
    primos_ordenados = sorted({num for num in conjunto_numeros if es_primo(num)})  # Filtramos los números primos y los ordenamos
    return primos_ordenados  # Devolvemos el conjunto de números primos ordenados

# Ejemplo de uso:
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_primos = numeros_primos_ordenados(conjunto_de_numeros)  # Llamamos a la función
print("Números primos ordenados:", numeros_primos)  # Mostramos los números primos ordenados encontrados

# %%  
"""16. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que sonpalíndromos y están 
ordenadas de menor a mayor."""

def es_palindromo(palabra):
    # Función que verifica si una palabra es un palíndromo
    return palabra == palabra[::-1]

def palabras_palindromos_ordenadas(conjunto_palabras):
    # Función que recibe un conjunto de palabras y devuelve los palíndromos ordenados de menor a mayor
    palindromos_ordenados = sorted({palabra for palabra in conjunto_palabras if es_palindromo(palabra)})
    return palindromos_ordenados

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python"}
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palindromos_ordenados = palabras_palindromos_ordenadas(conjunto_de_palabras)  # Llamamos a la función
print("Palíndromos ordenados:", palindromos_ordenados)  # Mostramos los palíndromos ordenados encontrados

# %%  
"""17. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que tienen una longitud 
determinada y están ordenadas de menor a mayor."""

def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras y una longitud, y devuelve las palabras con la longitud especificada, ordenadas
    palabras_longitud = sorted({palabra for palabra in conjunto_palabras if len(palabra) == longitud})
    return palabras_longitud

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
longitud_deseada = 5
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palabras_longitud = palabras_longitud_ordenadas(conjunto_de_palabras, longitud_deseada)  # Llamamos a la función
print("Palabras de longitud {} ordenadas:".format(longitud_deseada), palabras_longitud)  # Mostramos las palabras de longitud deseada ordenadas

# %%  
"""18. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que contienen una letra 
determinada y están ordenadas de mayor a menor."""

def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    # Función que recibe un conjunto de palabras y una letra, y devuelve las palabras que contienen la letra especificada, ordenadas
    palabras_con_letra = sorted({palabra for palabra in conjunto_palabras if letra in palabra}, reverse=True)
    return palabras_con_letra

# Ejemplo de uso:
conjunto_de_palabras = {"Hola", "Python", "Programación", "lápiz", "avión", "Manzana"}
letra_deseada = 'a'
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palabras_con_letra = palabras_con_letra_ordenadas(conjunto_de_palabras, letra_deseada)  # Llamamos a la función
print("Palabras con la letra '{}' ordenadas de mayor a menor:".format(letra_deseada), palabras_con_letra)  # Mostramos las palabras con la letra deseada ordenadas de mayor a menor

# %%
"""19. Escriba una función que reciba un conjunto de números y 
devuelva un conjunto con los números que están ordenados de menor 
a mayor y que no están duplicados."""

def numeros_ordenados_no_duplicados(conjunto_numeros):
    # Función que recibe un conjunto de números y devuelve los números ordenados de menor a mayor y no duplicados
    numeros_ordenados = sorted(set(conjunto_numeros))  # Convertimos el conjunto en una lista, eliminando duplicados, y luego la ordenamos
    return numeros_ordenados

# Ejemplo de uso:
conjunto_de_numeros = {5, 2, 8, 1, 9, 3, 5, 8, 2}  # Ejemplo con duplicados
print("Conjunto de números original:", conjunto_de_numeros)  # Mostramos el conjunto original
numeros_ordenados_no_duplicados = numeros_ordenados_no_duplicados(conjunto_de_numeros)  # Llamamos a la función
print("Números ordenados y no duplicados:", numeros_ordenados_no_duplicados)  # Mostramos los números ordenados y no duplicados

# %% 
"""20. Escriba una función que reciba un conjunto de palabras y 
devuelva un conjunto con las palabras que son palíndromos, tienen
 una longitud determinada y están ordenadas de menor a mayor."""

def es_palindromo(palabra):
    # Función que verifica si una palabra es un palíndromo
    return palabra == palabra[::-1]

def palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud):
    # Función que recibe un conjunto de palabras, una longitud y devuelve los palíndromos de esa longitud ordenados
    palindromos_ordenados = sorted({palabra for palabra in conjunto_palabras if es_palindromo(palabra) and len(palabra) == longitud})
    return palindromos_ordenados

# Ejemplo de uso:
conjunto_de_palabras = {"radar", "oso", "cívico", "sol", "anana", "python", "reconocer"}
longitud_deseada = 5
print("Conjunto de palabras original:", conjunto_de_palabras)  # Mostramos el conjunto original
palindromos_longitud_ordenados = palabras_palindromos_longitud_ordenadas(conjunto_de_palabras, longitud_deseada)  # Llamamos a la función
print("Palíndromos de longitud {} ordenados:".format(longitud_deseada), palindromos_longitud_ordenados)  # Mostramos los palíndromos de longitud deseada ordenados

#%% SEMANA 8 Y 9

# #problema1
# #EJERCICIO PARTE1
# # 1. Validar la edad de un usuario.
from datetime import datetime

def validar_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year

    if fecha_actual.month < fecha_nacimiento.month:
        edad -= 1

    return edad >= 18

# Ejemplo de uso

fecha_nacimiento = input("Introduce tu fecha de nacimiento (YYYY-MM-DD): ")

if validar_edad(fecha_nacimiento):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#%%
# # 2. Verificar el tipo de dato de una variable.
    
# # Definir una variable
edad = 20

# Verificar el tipo de dato de la variable
tipo_dato = type(edad)

# Imprimir el tipo de dato
print(tipo_dato)

# 2.1
# Verificar si la variable edad es un número entero
es_numero_entero = isinstance(edad, int)

# Imprimir el resultado
print(es_numero_entero)


 #%%   
# # 3. Validar el rango de una calificación.
def validar_calificacion(calificacion):
    """
    Valida una calificación.

    Args:
        calificacion: La calificación a validar.

    Returns:
        True si la calificación es válida, False en caso contrario.
    """

    rango_calificacion_valido = (0, 100)
    return calificacion >= rango_calificacion_valido[0] and calificacion <= rango_calificacion_valido[1]

# Ejemplo de uso

calificacion = float(input("Introduce tu calificación: "))

if validar_calificacion(calificacion):
    print("Tu calificación es válida.")
else:
    print("Tu calificación está fuera del rango válido.")

#%%
# # 4. Asegurar que una lista no esté vacía.
lista = []

for elemento in lista:
    # La lista no está vacía
    print("La lista no está vacía.")
    break
else:
    # La lista está vacía
    print("La lista está vacía.")
#%%
# # 5. Validar la igualdad de dos objetos.
objeto1 = float(input("Ingrese el objeto 1: "))
objeto2 = float(input("Ingrese el objeto 2: "))

if objeto1 == objeto2:
    print("Los objetos son iguales.")
else:
    print("Los objetos son diferentes.")
#%%
# # 6. Asegurar que un ciclo while se ejecuta al menos una vez.
# # Definir una variable
edad = 0

# Definir una bandera
se_ha_ejecutado = False

# Bucle while
while not se_ha_ejecutado:
    # Mostrar un mensaje al usuario
    print("Introduce tu edad: ")

    # Solicitar la edad al usuario
    edad = int(input())

    # Verificar si la edad es válida
    if edad > 0:
        # Cambiar la bandera a True
        se_ha_ejecutado = True

# Imprimir la edad
print("Tu edad es:", edad)
#%%
# # 7. Asegurar que una función retorna un valor específico.
def sumar(a, b):
    """
    Esta función suma dos números.

    Args:
        a: El primer número.
        b: El segundo número.

    Returns:
        La suma de los dos números.
    """
    resultado = a + b
    return resultado

# Ejemplo de uso
resultado = sumar(1, 2)
print("El resultado es:", resultado)
#%%
# # 8. Validar el estado de una variable después de una operación.
# # Definir una variable
variable = 10

# Imprimir el valor de la variable antes de la operación
print("Valor antes de la operación:", variable)

# Realizar una operación
variable += 5

# Imprimir el valor de la variable después de la operación
print("Valor después de la operación:", variable)

# Verificar si el valor de la variable ha cambiado
if variable > 10:
    print("El valor de la variable ha cambiado.")
else:
    print("El valor de la variable no ha cambiado.")
    
#%%
# 9. Asegurar que un módulo se ha importado correctamente.
# Importar el módulo
try:
    # Importar el módulo
    import mi_modulo
except ImportError as error:
    print(error)
else:
    print("El módulo se ha importado correctamente.")


#%%
# Ejercicios parte 02:
# 10. Desarrollar el código de buscar nodo en la lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def buscar_nodo(lista, valor):
    """
    Esta función busca un nodo en una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.
        valor: El valor del nodo que se busca.

    Returns:
        El nodo encontrado o None si no se encuentra el nodo.
    """

    actual = lista
    while actual is not None:
        if actual.valor == valor:
            return actual
        actual = actual.siguiente

    return None

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

valor_a_buscar = 20

nodo_encontrado = buscar_nodo(nodo1, valor_a_buscar)

if nodo_encontrado is not None:
    print("El nodo con el valor", valor_a_buscar, "se ha encontrado.")
else:
    print("No se ha encontrado un nodo con el valor", valor_a_buscar)
#%%
# Suma de Nodos
# 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def sumar_nodos(lista):
    """
    Esta función suma todos los nodos de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La suma de todos los nodos de la lista.
    """

    suma = 0
    actual = lista
    while actual is not None:
        suma += actual.valor
        actual = actual.siguiente

    return suma

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

suma_nodos = sumar_nodos(nodo1)

print("La suma de todos los nodos es:", suma_nodos)

#%%
# Longitud de la Lista
# 12. Crea una función que devuelva la longitud de una lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def obtener_longitud(lista):
    """
    Esta función calcula la longitud de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La longitud de la lista.
    """

    longitud = 0
    actual = lista
    while actual is not None:
        longitud += 1
        actual = actual.siguiente

    return longitud

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

longitud = obtener_longitud(nodo1)

print("La longitud de la lista es:", longitud)

#%%
# Concatenar Listas
# 13. Implementa una función que concatene dos listas enlazadas simples.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def concatenar_listas(lista1, lista2):
    """
    Esta función concatena dos listas enlazadas simples.

    Args:
        lista1: La primera lista enlazada simple.
        lista2: La segunda lista enlazada simple.

    Returns:
        La lista concatenada.
    """

    actual = lista1
    while actual.siguiente is not None:
        actual = actual.siguiente

    actual.siguiente = lista2

    return lista1

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo4 = Nodo(40)
nodo5 = Nodo(50)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

nodo4.siguiente = nodo5

lista_concatenada = concatenar_listas(nodo1, nodo4)

actual = lista_concatenada
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
    
#%%
# Eliminar Duplicados
# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def eliminar_nodos_duplicados(lista):
    """
    Esta función elimina los nodos duplicados de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La lista sin nodos duplicados.
    """

    nodos_visitados = set()
    actual = lista
    anterior = None
    while actual is not None:
        if actual.valor in nodos_visitados:
            # Eliminar el nodo duplicado
            anterior.siguiente = actual.siguiente
        else:
            # Agregar el nodo a la lista de nodos visitados
            nodos_visitados.add(actual.valor)
            anterior = actual
        actual = actual.siguiente

    return lista

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(10)
nodo4 = Nodo(30)
nodo5 = Nodo(20)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

lista_sin_duplicados = eliminar_nodos_duplicados(nodo1)

actual = lista_sin_duplicados
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente
    
#%%
# Invertir Lista
# 15. Implementa una función que invierta el orden de una lista enlazada simple
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def invertir_lista(lista):
    """
    Esta función invierte el orden de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La lista con el orden invertido.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    return anterior

# Ejemplo de uso
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

lista_invertida = invertir_lista(nodo1)

actual = lista_invertida
while actual is not None:
    print(actual.valor)
    actual = actual.siguiente

#%% LABORATORIO DE 10 Y 11
#%%bn
# Ejercicio parte 01 – Listas Enlazadas Dobles:
# Duplicar Nodos:
# 1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista 
# duplicada hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 4 nodos.

    Returns:
        La lista con al menos 4 nodos.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4

    return nodo1

def duplicar_lista(lista):
    """
    Esta función duplica cada nodo de una lista.

    Args:
        lista: La lista que se desea duplicar.

    Returns:
        La lista duplicada.
    """

    lista_duplicada = None
    actual = lista
    while actual is not None:
        nuevo_nodo = Nodo(actual.valor)
        if lista_duplicada is None:
            lista_duplicada = nuevo_nodo
        else:
            # Al final del bucle, "actual_duplicado" apuntará al último nodo de la lista duplicada.
            actual_duplicado = lista_duplicada
            while actual_duplicado.siguiente is not None:
                actual_duplicado = actual_duplicado.siguiente
            actual_duplicado.siguiente = nuevo_nodo
        actual = actual.siguiente

    return lista_duplicada

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    # No necesitamos invertir la lista para imprimir hacia atrás, simplemente podemos imprimir los nodos en el orden actual.
    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

# Ejemplo de uso
lista_original = crear_lista()

print("Lista original hacia adelante:")
imprimir_lista_adelante(lista_original)

print("Lista original hacia atrás:")
imprimir_lista_atras(lista_original)

lista_duplicada = duplicar_lista(lista_original)

print("Lista duplicada hacia adelante:")
imprimir_lista_adelante(lista_duplicada)

print("Lista duplicada hacia atrás:")
imprimir_lista_atras(lista_duplicada)

#%%bn
# Contar Nodos Pares e Impares:
# 2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato 
# impar e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 9 nodos.

    Returns:
        La lista con al menos 9 nodos.
    """

    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)
    nodo7 = Nodo(7)
    nodo8 = Nodo(8)
    nodo9 = Nodo(9)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo6
    nodo6.siguiente = nodo7
    nodo7.siguiente = nodo8
    nodo8.siguiente = nodo9

    return nodo1

def contar_pares_impares(lista):
    """
    Esta función cuenta cuántos nodos tienen un dato par y cuántos tienen un dato impar en una lista.

    Args:
        lista: La lista que se desea analizar.

    Returns:
        Una tupla con el número de nodos pares y el número de nodos impares.
    """

    pares = 0
    impares = 0
    actual = lista
    while actual is not None:
        if actual.valor % 2 == 0:
            pares += 1
        else:
            impares += 1
        actual = actual.siguiente

    return pares, impares

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """

    # No necesitamos invertir la lista para imprimir hacia atrás, simplemente podemos imprimir los nodos en el orden actual.
    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

# Ejemplo de uso
lista = crear_lista()

pares, impares = contar_pares_impares(lista)

print(f"Número de nodos pares: {pares}")
print(f"Número de nodos impares: {impares}")

print("Lista hacia adelante:")
imprimir_lista_adelante(lista)

print("Lista hacia atrás:")
imprimir_lista_atras(lista)

#%%bn
# Insertar Nodo en Posición Específica:
# 3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la 
# lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 5 nodos.

    Returns:
        La lista con al menos 5 nodos.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)
    nodo5 = Nodo(50)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5

    return nodo1

def insertar_nodo(lista, posicion, valor):
    """
    Esta función inserta un nuevo nodo en una lista enlazada simple.

    Args:
        lista: La lista en la que se desea insertar el nuevo nodo.
        posicion: La posición en la que se desea insertar el nuevo nodo.
        valor: El valor del nuevo nodo.

    Returns:
        La lista con el nuevo nodo insertado.
    """

    if posicion < 0:
        raise ValueError("La posición debe ser un número positivo")

    nuevo_nodo = Nodo(valor)
    actual = lista
    anterior = None
    for i in range(posicion):
        anterior = actual
        actual = actual.siguiente

    if anterior is None:
        nuevo_nodo.siguiente = lista
        lista = nuevo_nodo
    else:
        anterior.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = actual

    return lista

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """
    # No necesitamos invertir la lista para imprimir hacia atrás, simplemente podemos imprimir los nodos en el orden actual.
    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

# Ejemplo de uso
lista = crear_lista()

print("Lista original:")
imprimir_lista_adelante(lista)

lista = insertar_nodo(lista, 3, 15)

print("Lista con el nuevo nodo insertado:")
imprimir_lista_adelante(lista)

print("Lista hacia atrás:")
imprimir_lista_atras(lista)

#%% bn
# Eliminar Nodos Duplicados:
# 4. Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando 
# solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con nodos que contienen datos duplicados.

    Returns:
        La lista con nodos que contienen datos duplicados.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)
    nodo5 = Nodo(20)
    nodo6 = Nodo(50)
    nodo7 = Nodo(10)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo6
    nodo6.siguiente = nodo7

    return nodo1

def eliminar_duplicados(lista):
    """
    Esta función elimina todos los nodos duplicados de una lista, dejando solo una instancia de cada dato.

    Args:
        lista: La lista con nodos duplicados.

    Returns:
        La lista sin nodos duplicados.
    """
    # Utilizamos un conjunto para realizar un seguimiento de los valores que hemos visto.
    nodos_visitados = set()
    actual = lista
    anterior = None
    while actual is not None:
        if actual.valor in nodos_visitados:
            # Si el valor ya está en el conjunto, eliminamos el nodo duplicado.
            anterior.siguiente = actual.siguiente
        else:
            # Si el valor no está en el conjunto, lo agregamos y avanzamos al siguiente nodo.
            nodos_visitados.add(actual.valor)
            anterior = actual
        actual = actual.siguiente

    return lista

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """
    # No necesitamos invertir la lista para imprimir hacia atrás, simplemente podemos imprimir los nodos en el orden actual.
    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

# Ejemplo de uso
lista = crear_lista()

print("Lista original:")
imprimir_lista_adelante(lista)

lista = eliminar_duplicados(lista)

print("Lista sin nodos duplicados:")
imprimir_lista_adelante(lista)

print("Lista hacia atrás:")
imprimir_lista_atras(lista)
#%% bn
# Invertir la Lista:
# 5. Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el 
# primero y viceversa) e imprime la lista hacia adelante y hacia atrás
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def crear_lista():
    """
    Esta función crea una lista con al menos 6 nodos.

    Returns:
        La lista con al menos 6 nodos.
    """

    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo3 = Nodo(30)
    nodo4 = Nodo(40)
    nodo5 = Nodo(50)
    nodo6 = Nodo(60)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo6

    return nodo1

def invertir_lista(lista):
    """
    Esta función invierte el orden de una lista enlazada simple.

    Args:
        lista: La lista enlazada simple.

    Returns:
        La lista con el orden invertido.
    """

    anterior = None
    actual = lista
    while actual is not None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    return anterior

def imprimir_lista_adelante(lista):
    """
    Esta función imprime una lista hacia adelante.

    Args:
        lista: La lista que se desea imprimir.
    """

    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

def imprimir_lista_atras(lista):
    """
    Esta función imprime una lista hacia atrás.

    Args:
        lista: La lista que se desea imprimir.
    """
    # Aquí necesitamos avanzar hasta el final de la lista original.
    # No podemos simplemente invertir la lista original como se hizo anteriormente.
    # En lugar de eso, podemos simplemente imprimir la lista de forma normal.
    actual = lista
    while actual is not None:
        print(actual.valor)
        actual = actual.siguiente

# Ejemplo de uso
lista = crear_lista()

print("Lista original:")
imprimir_lista_adelante(lista)

lista_invertida = invertir_lista(lista)

print("Lista con el orden invertido:")
imprimir_lista_adelante(lista_invertida)

print("Lista original hacia atrás:")
imprimir_lista_atras(lista)
#%%
# Ejercicios parte 02:
#%% bn
# Invertir una cadena:
 # 6. Utilizar una pila para invertir el orden de los caracteres de una cadena.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

    def esta_vacia(self):
        return self.cima is None

def invertir_cadena(cadena):
    """
    Esta función invierte el orden de los caracteres de una cadena utilizando una pila.

    Args:
        cadena: La cadena que se desea invertir.
    Returns:
        La cadena con el orden de los caracteres invertido.
    """
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)

    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida

# Ejemplo de uso
cadena = "Hola, mundo!"

cadena_invertida = invertir_cadena(cadena)

print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {cadena_invertida}")
#%% bn
# # Convertir número decimal a binario:
# # 7. Implementar un programa que convierta un número decimal a su representación en sistema binario 
# # utilizando una pila.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

    def esta_vacia(self):
        return self.cima is None

def convertir_a_binario(numero):
    """
    Esta función convierte un número decimal a su representación en sistema binario utilizando una pila.

    Args:
        numero: El número decimal que se desea convertir.
    Returns:
        La representación en sistema binario del número decimal.
    """
    pila = Pila()
    while numero > 0:
        resto = numero % 2
        numero //= 2
        pila.apilar(resto)

    numero_binario = ""
    while not pila.esta_vacia():
        numero_binario += str(pila.desapilar())

    return numero_binario

# Ejemplo de uso
numero = 10

numero_binario = convertir_a_binario(numero)

print(f"Número decimal: {numero}")
print(f"Número binario: {numero_binario}")
#%%
# # Evaluar expresión posfija:
# # 8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

def evaluar_posfija(expresion):
    """
    Esta función evalúa una expresión matemática en notación posfija utilizando una pila.

    Args:
        expresion: La expresión en notación posfija.

    Returns:
        El resultado de la evaluación de la expresión.
    """

    pila = Pila()
    for caracter in expresion.split():
        if caracter.isdigit():
            pila.apilar(int(caracter))
        else:
            operador2 = pila.desapilar()
            operador1 = pila.desapilar()
            if caracter == "+":
                resultado = operador1 + operador2
            elif caracter == "-":
                resultado = operador1 - operador2
            elif caracter == "*":
                resultado = operador1 * operador2
            elif caracter == "/":
                resultado = operador1 / operador2
            pila.apilar(resultado)

    return pila.desapilar()

# Ejemplo de uso
expresion = "12 3 + 4 2 * -"

resultado = evaluar_posfija(expresion)

print(f"Expresión: {expresion}")
print(f"Resultado: {resultado}")

#%%bn
# # Validar operadores anidados:
# # 9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una 
# # pila.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

    def esta_vacia(self):
        return self.cima is None

def estan_bien_anidados(expresion):
    """
    Esta función verifica si los operadores en una expresión matemática están correctamente anidados utilizando una pila.

    Args:
        expresion: La expresión matemática.

    Returns:
        True si los operadores están correctamente anidados, False en caso contrario.
    """
    pila = Pila()
    for caracter in expresion:
        if caracter in "()[]{}":
            if caracter == "(" or caracter == "[" or caracter == "{":
                pila.apilar(caracter)
            else:
                if pila.esta_vacia():
                    return False
                operador_apertura = pila.desapilar()
                if (caracter == ")" and operador_apertura != "(") or \
                    (caracter == "]" and operador_apertura != "[") or \
                    (caracter == "}" and operador_apertura != "{"):
                    return False
    return pila.esta_vacia()

# Ejemplo de uso
expresion = "(a + b) * (c - d)"

if estan_bien_anidados(expresion):
    print(f"Los operadores en la expresión '{expresion}' están correctamente anidados.")
else:
    print(f"Los operadores en la expresión '{expresion}' no están correctamente anidados.")
    

#%% bn
# # Ordenar una pila:
# # 10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.
def ordenar_pila(pila):
    """
    Esta función ordena los elementos de una pila de manera ascendente utilizando una lista como estructura adicional.

    Args:
        pila: La pila que se desea ordenar.

    Returns:
        La pila con los elementos ordenados de manera ascendente.
    """

    lista = []
    while not pila.esta_vacia():
        lista.append(pila.desapilar())

    lista.sort()

    for elemento in lista:
        pila.apilar(elemento)

    return pila

# Ejemplo de uso
pila = Pila()
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)
pila.apilar(40)
pila.apilar(50)

pila_ordenada = ordenar_pila(pila)

while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar())
     
#%%
# # Eliminar duplicados:
# # 11. Eliminar los elementos duplicados de una pila.
def eliminar_duplicados(pila):
    """
    Esta función elimina los elementos duplicados de una pila utilizando una lista como estructura adicional.

    Args:
        pila: La pila que se desea eliminar los elementos duplicados.

    Returns:
        La pila con los elementos duplicados eliminados.
    """

    lista = []
    elementos_vistos = set()
    while not pila.esta_vacia():
        elemento_actual = pila.desapilar()
        if elemento_actual not in elementos_vistos:
            lista.append(elemento_actual)
            elementos_vistos.add(elemento_actual)

    for elemento in lista[::-1]:
        pila.apilar(elemento)

    return pila

# Ejemplo de uso
pila = Pila()
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)
pila.apilar(40)
pila.apilar(20)

pila_sin_duplicados = eliminar_duplicados(pila)

while not pila_sin_duplicados.esta_vacia():
    print(pila_sin_duplicados.desapilar())
    


#%%
# # Implementar una calculadora sencilla:
# # 12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar 
# # expresiones.
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

def evaluar_expresion(expresion):
    """
    Esta función evalúa una expresión matemática utilizando una pila.

    Args:
        expresion: La expresión matemática.

    Returns:
        El resultado de la evaluación de la expresión.
    """
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operador2 = pila.desapilar()
            operador1 = pila.desapilar()
            if token == "+":
                resultado = operador1 + operador2
            elif token == "-":
                resultado = operador1 - operador2
            elif token == "*":
                resultado = operador1 * operador2
            elif token == "/":
                resultado = operador1 / operador2
            pila.apilar(resultado)

    return pila.desapilar()

# Ejemplo de uso
expresion = "12 3 + 4 2 * -"

resultado = evaluar_expresion(expresion)

print(f"Expresión: {expresion}")
print(f"Resultado: {resultado}")

#%%
# # Comprobar palíndromos:
# # 13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
# class Nodo:
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

    def esta_vacia(self):
        return self.cima is None

def es_palindromo(texto):
    """
    Esta función comprueba si una palabra o frase es un palíndromo utilizando una pila.

    Args:
        texto: La palabra o frase que se desea comprobar.

    Returns:
        True si la palabra o frase es un palíndromo, False en caso contrario.
    """

    # Limpiar el texto eliminando espacios en blanco y convirtiéndolo todo a minúsculas
    texto = texto.replace(" ", "").lower()

    pila = Pila()
    for caracter in texto:
        pila.apilar(caracter)

    texto_invertido = ""
    while not pila.esta_vacia():
        texto_invertido += pila.desapilar()

    return texto == texto_invertido

# Ejemplo de uso
texto = "Anita lava la tina"

if es_palindromo(texto):
    print(f"El texto '{texto}' es un palíndromo.")
else:
    print(f"El texto '{texto}' no es un palíndromo.")
#%%
# # Simular el proceso de deshacer (undo):
# # 14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los 
# # deshaceres
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Pila:
    def __init__(self):
        self.cima = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        if self.cima is None:
            raise ValueError("La pila está vacía")
        valor_desapilado = self.cima.valor
        self.cima = self.cima.siguiente
        return valor_desapilado

def deshacer(pila_acciones, pila_deshaceres):
    """
    Esta función realiza la acción de "deshacer" utilizando dos pilas.

    Args:
        pila_acciones: La pila que contiene las acciones realizadas.
        pila_deshaceres: La pila que contiene las acciones que se pueden deshacer.

    Returns:
        El valor de la acción deshecha.
    """

    accion_deshecha = pila_acciones.desapilar()
    pila_deshaceres.apilar(accion_deshecha)
    return accion_deshecha

def rehacer(pila_acciones, pila_deshaceres):
    """
    Esta función realiza la acción de "rehacer" utilizando dos pilas.

    Args:
        pila_acciones: La pila que contiene las acciones realizadas.
        pila_deshaceres: La pila que contiene las acciones que se pueden deshacer.

    Returns:
        El valor de la acción rehecha.
    """

    accion_rehecha = pila_deshaceres.desapilar()
    pila_acciones.apilar(accion_rehecha)
    return accion_rehecha

# Ejemplo de uso
pila_acciones = Pila()
pila_deshaceres = Pila()

# Apilamos algunas acciones
pila_acciones.apilar("Acción 1")
pila_acciones.apilar("Acción 2")
pila_acciones.apilar("Acción 3")

# Deshacemos una acción
accion_deshecha = deshacer(pila_acciones, pila_deshaceres)
print(f"Acción deshecha: {accion_deshecha}")

# Rehacemos la acción deshecha
accion_rehecha = rehacer(pila_acciones, pila_deshaceres)
print(f"Acción rehecha: {accion_rehecha}")







