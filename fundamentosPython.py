# Esto es un comentario.
''' Este es un comentario 
de varias líneas '''

def nuevoTema(tema, relleno = '*', caracteres = 40):   
    largo = len(tema)
    espacios = caracteres - largo - 2
    print("\n╔", end = "")
    for i in range(caracteres - 2):
        print("═", end = "")
    print("╗\n║", end = "")
    espacios2 = espacios // 2
    for i in range(espacios2 - 1):
        print(relleno, end = "")
    print(" " + tema + " ", end = "")
    for i in range(espacios2 - 1):
        print(relleno, end = "")
    if espacios % 2 == 1:
        print(relleno, end = "")
    print("║\n╚", end = "")
    for i in range(caracteres - 2):
        print("═", end = "")
    print("╝")  

if __name__ == "__main__":
    # nuevoTema("Operadores Aritméticos")
    nuevoTema("Operadores Aritméticos")
    print("Operador Exponente, 2 ** 9  = ", 2 ** 9) #Jerarquía más alta: 1 

    print("Operador Cambio de Signo, -(3) = ", -(3)) #Jerarquía 2

    print("Operador Multiplicación, 3 * 4 = ", 3 * 4) #Jerarquía 3
    print("Operador División, 20 / 3 = ", 20 / 3) #Jerarquía 3
    print("Operador División Entera, 20 // 3 = ", 20 // 3) #Jerarquía 3
    print("Operador Módulo, 20 % 3 = ", 20 % 3) #Jerarquía 3

    print("Operador Suma, 5 + 3 = ", 5 + 3) #Jerarquía 4
    print("Operador Resta, 10 - 2 = ", 10 - 2) #Jerarquía 4

    # nuevoTema("Operadores Lógicos")
    nuevoTema("Operadores Lógicos")
    print("Operador and, True and True = ", True and True) #Jerarquía 1
    print("Operador or, True or False = ", True or False) #Jerarquía 2
    print("Operador not, not True = ", not True) #Jerarquía 3

    # nuevoTema("Tabla de verdad del and")
    nuevoTema("Tabla de verdad del and")
    print("False and False = ", False and False)
    print("False and True = ", False and True)
    print("True and False = ", True and False)
    print("True and True = ", True and True)

    # nuevoTema("Tabla de verdad del or")
    nuevoTema("Tabla de verdad del or")
    print("False or False = ", False or False)
    print("False or True = ", False or True)
    print("True or False = ", True or False)
    print("True or True = ", True or True)
    
    # nuevoTema("Tabla de verdad del operardor Lógico not")
    nuevoTema("Tabla de verdad del operardor Lógico not")
    print("not False = ", not False)
    print("not True = ", not True)

    # nuevoTema("Operadores de Comparación")
    nuevoTema("Operadores de Comparación")
    print("Operador igualdad, 5 == 4 = ", 5 == 4)
    print("Operador desigual, 5 != 4 = ", 5 != 4)
    print("Operador menor que, 5 < 4 = ", 5 < 4)
    print("Operador menor o igual que, 5 <= 4 = ", 5 <= 4)
    print("Operador mayor que, 5 > 4 = ", 5 > 4)
    print("Operador mayor o igual que, 5 >= 4 = ", 5 >= 4)

    # nuevoTema("Impresión de variables")
    nuevoTema("Impresión de variables")
    nombre_variable1 = 25
    nombre_variable2 = 25.3
    nombre_variable3 = "Pepe"
    print(nombre_variable1, nombre_variable2, nombre_variable3)

    a, b, c = 5, 10.8, "Hola"
    print(a, b, c)

    # nuevoTema("Numéricos Enteros")
    nuevoTema("Numéricos Enteros")
    w, x, y, z, h  = 105, 123456789, -58, 0b000110011, 0xff
    print("La variable 'w' tiene un valor de", w ,type(w))
    print("La variable 'x' tiene un valor de", x ,type(x))
    print("La variable 'y' tiene un valor de", y ,type(y))
    print("La variable 'z' tiene un valor de", z ,type(z))
    print("La variable 'h' tiene un valor de", h ,type(h))

    # nuevoTema("Numéricos Flotantes")
    nuevoTema("Numéricos Flotantes")
    x, y = 105.0, 12345.6789
    print("La variable 'x' tiene un valor de", x ,type(x))
    print("La variable 'y' tiene un valor de", y ,type(y))

    # nuevoTema("Números Complejos")
    nuevoTema("Números Complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print("La variable 'x' tiene un valor de", x ,type(x))
    print("La variable 'y' tiene un valor de", y ,type(y))
    print("La variable 'z' tiene un valor de", z ,type(z))

    # nuevoTema("Booleanos")
    nuevoTema("Booleanos")
    lis = []
    print(lis, "is", bool(lis))
    t = ()
    print(t, "is", bool(t))
    new = 'Hello'
    print(new, "is", bool(new))
    num = 99
    print(num, "is", bool(num))
    comp = 0 + 0j
    print(comp, "is", bool(comp))
    val = None
    print(val, "is", bool(val))

    # nuevoTema("Listas")
    nuevoTema("Listas") # Mutables
    a = [10, 20.5, "Pytohn List"] # Se define entre corchetes
    print(a)
    print(a[1])
    a[1] = "Hola"
    print(a)
    lista_ejemplo = [1, -2.2, 3 + 4j, None, "Hola"]
    print(lista_ejemplo, type(lista_ejemplo))
    print(lista_ejemplo[0]) # 1

    # nuevoTema("Tuplas")
    nuevoTema("Tuplas") # Inmutables
    t = (10, 20.5, "Pytohn List") # Se define entre paréntesis
    print("Tupla 't' =", t)
    print("t[1] =", t[1])
    # t[1] = "Hola" # Operación no válida en tuplas por ser inmutable
    t = (25,'tuple', 1 + 10j)
    print("Tupla 't' =", t)
    print("t[1] =", t[1])
    print("t[0:3] =", t[0:3])
    tupla_ejemplo = (1, -2.2, 3 + 4j, None, "Hola")
    print(tupla_ejemplo, type(tupla_ejemplo))
    print(tupla_ejemplo[0]) # 1

    # nuevoTema("Cadenas")
    nuevoTema("Cadenas")
    s = "This is a single line string"
    print(s)
    s2 = '''A multiline
        string''' # En esta caso el tab al inicio forma parte de la cadena 
    print(s2)
    cadena1 = "Esto es una cadena" # Entre comillas
    cadena2 = 'Esto también es una cadena' # Entre comillas simples
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena1[5])
    cadenaMultilinea = '''Esto es una cadena
    de varias líneas    con tabulares y
    saltos
    de
    línea'''
    print(cadenaMultilinea, type(cadenaMultilinea))
    cadena3 = "Hola" * 5
    print(cadena3)

    # nuevoTema("Conjuntos")
    nuevoTema("Conjuntos") # Iterables, mutables y elementos únicos
    conjunto = {10, 20, 30, 40, 10, 50} # Se define entre llaves
    print(conjunto) # No permite duplicar elementos
    a = {50, 20, 30, 10, 40}
    print("a =", a, "tipo =", type(a))

    # nuevoTema("Diccionarios")
    nuevoTema("Diccionarios") 
    diccionario = {"Nombre":"Omar",
                "Edad":36,
                "Telefono":"7711123456"} # Se define entre llaves
    # Pero consta de 2 datos identificador:valor 
    print(diccionario)
    print(diccionario["Nombre"]) # Indexable pero no bajo un consecutivo sino bajo el identificador
    d = {1:'val1', 2:'val2'}
    print(type(d))
    print("d[1] =", d[1])
    print("d[2] =", d[2])
