
from curses.ascii import isdigit
import re
import os 


# from sympy import *

# def lectura():
#     while True:
#         entrada = input("Numero: ")
#         try:
#             entrada = int(entrada)
#             return entrada
#         except ValueError:
#             print("It's not an Integer")


#1. Función que calcule el cubo de un número entero.

# def cubo():
#   x = lectura()
#   print(x * x)}

# cubo()

# 2. Función que calcule el valor factorial de un número entero positivo. 

# def factorial(x):
#     z = 1
#     for y in range(1, x + 1):
#         z*=y
#     print(z)

# x = lectura()
# while(x < 0):
#     print("It's not positive number.")
#     x = lectura()
# else: 
#     factorial(x)

# 3. Función que cuente cuantas veces se repite el patrón en una cadena de 
#    caracteres incluyendo si se superponen.

# def cuenta_patron():
#     x = input('Ingrese cadena: ')
#     z = input('Patrón: ')
#     y = re.findall(z, x)
#     print(y.count(z))

# cuenta_patron()

# 4. Función que devuelva una parte del árbol de acuerdo con su índice. 

# regex =  "^[(][0-3]{1}\,{1}(?:[0-2]\,){0,1}[0-2]{0,1}[)]$"
# tree = (((1,2), 3), (4, (5, 6)), 7, (8, 9 ,10))

# def arbol_ref(tree, x):
#     (rama1, rama2, rama3, rama4) = tree
#     (hoja1) = rama1[0]
#     (hoja2) = rama1[1]
#     (hojas3) = rama2[1]

#     if int(digitslist[0]) == 0:
#         if digitslist[1] == None:
#             print(rama1)
#         else:
#             if (int(digitslist[1]) == 0 or int(digitslist[1]) == 1):
#                 if int(digitslist[1]) == 0:
#                     if digitslist[2] == None:
#                         print(hoja1)
#                     else: 
#                         if (int(digitslist[2]) == 0 or int(digitslist[2]) == 1):
#                             if int(digitslist[2]) == 0:
#                                 print(hoja1[0])
#                             else: print(hoja1[1])
#                         else: print("Hoja no existe")
#                 else: 
#                     if digitslist[2] == None:
#                         print(hoja2)
#                     else: print("Hoja no existe")
#             else: 
#                 print("Hoja no existe")
        
#     else: 
#         if int(digitslist[0]) == 1: 
#             if digitslist[1] == None:
#                 print(rama2)
#             else:
#                 if (int(digitslist[1]) == 0 or int(digitslist[1]) == 1):
#                     if int(digitslist[1]) == 0:
#                         if digitslist[2] == None:
#                             print(rama2[0])
#                         else: print("Hoja no existe")
#                     else:
#                         if digitslist[2] == None:
#                             print(rama2[1])
#                         else:
#                             os.system("pause")
#                             if int(digitslist[2]) == 0:
#                                     print(hojas3[0])
#                             else: 
#                                 if int(digitslist[2]) == 1:
#                                     print(hojas3[1])
#                                 else: print("Hoja no existe")
#                 else: print("Hoja no existe")
#         else: 
#             if int(digitslist[0]) == 2:
#                 if digitslist[1] != None:
#                     print("Hoja no existe")
#                 else: print(rama3)
#             else: 
#                 if int(digitslist[0]) == 3:
#                     if digitslist[1] == None:
#                         print(rama4)
#                     else: 
#                         if (int(digitslist[1]) >= 0 or int(digitslist <= 2)) and digitslist[2] == None:
#                             print(rama4[int(digitslist[1])])
#                         else: print("Hoja no existe")



# x = (input("Rama: "))

# digitslist = [None, None, None]
# if re.fullmatch(regex, x):
#     cont = 0
#     for i in x:
#         if i.isdigit():
#             digitslist[cont] = i
#             cont +=1
#     arbol_ref(tree, digitslist)
# else: 
#     print("No concuerda con el formato (0-3,0-2,0-2)")

# 5. Función que desarrolle una expresión algebraica. 
# funcion = input("Expresión: ")
# x = Symbol ('x')
# y = Symbol ('y')
# print(expand(funcion))
